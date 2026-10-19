#!/usr/bin/env python3
"""Copy release facts from policy.json into the pages and the README.

Installed copies of Jasiri read policy.json. The website and the README
repeat the version, the download size, and the SHA-256 as ordinary text.
A reader who does not run JavaScript still sees the current release.

Markers, which this script fills:

  <span data-release="version">0.19.0</span>
  <span data-release="mib">about 55 MB</span>
  <p data-release="sha256">…</p>
  <a data-release="virustotal" href="https://www.virustotal.com/gui/file/…">

README lines, one of each:

  Version: 0.19.0
  Download size: about 55 MB
  SHA-256: `…`

The size is the APK length in sideload.bytes, divided by 1024 twice
and rounded to the nearest megabyte. 0.5 rounds up.

  python3 scripts/sync-release-facts.py --apply
  python3 scripts/sync-release-facts.py --check
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Jasiri for Android: A pocket computer, with an integrated AI assistant."


def about_mb(nbytes):
    rounded = int(nbytes / (1024 * 1024) + 0.5)
    return "about %d MB" % rounded


def load_facts():
    policy = json.loads((ROOT / "policy.json").read_text())
    version = policy.get("latestVersionName") or ""
    side = policy.get("sideload") or {}
    sha = (side.get("sha256") or "").lower()
    nbytes = side.get("bytes")
    errors = []
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("latestVersionName is missing")
    if not re.fullmatch(r"[0-9a-f]{64}", sha):
        errors.append("sideload.sha256 is missing")
    if not isinstance(nbytes, int) or nbytes < 1_000_000:
        errors.append("sideload.bytes is missing")
    if errors:
        raise SystemExit("policy.json: " + "; ".join(errors))
    return {
        "version": version,
        "sha": sha,
        "mib": about_mb(nbytes),
        "virustotal": "https://www.virustotal.com/gui/file/" + sha,
    }


def replace_inner(html, kind, value):
    pattern = re.compile(
        r"(<([a-zA-Z0-9]+)[^>]*\bdata-release=\"" + kind + r"\"[^>]*>)(.*?)(</\2>)",
        re.S,
    )

    def repl(match):
        return match.group(1) + value + match.group(4)

    return pattern.subn(repl, html)


def replace_href(html, url):
    pattern = re.compile(
        r"(<a\b[^>]*\bdata-release=\"virustotal\"[^>]*)(>)",
        re.S,
    )

    def repl(match):
        tag = match.group(1)
        if re.search(r"\bhref=\"[^\"]*\"", tag):
            tag = re.sub(r"\bhref=\"[^\"]*\"", 'href="%s"' % url, tag, count=1)
        else:
            tag += ' href="%s"' % url
        return tag + match.group(2)

    return pattern.subn(repl, html)


def apply_html(path, facts):
    text = path.read_text()
    counts = {}
    for kind in ("version", "mib", "sha256"):
        text, counts[kind] = replace_inner(text, kind, facts[kind if kind != "sha256" else "sha"])
    text, counts["virustotal"] = replace_href(text, facts["virustotal"])
    return text, counts


def apply_readme(text, facts):
    lines = {
        "Version: ": facts["version"],
        "Download size: ": facts["mib"],
        "SHA-256: ": "`%s`" % facts["sha"],
    }
    counts = {}
    for prefix, rest in lines.items():
        pattern = re.compile("^" + re.escape(prefix) + ".*$", re.M)
        text, counts[prefix] = pattern.subn(prefix + rest, text)
    return text, counts


def expected_pages():
    return [
        ROOT / "index.html",
        ROOT / "check" / "index.html",
    ]


def check_title(errors):
    home = (ROOT / "index.html").read_text()
    for label, pattern in (
        ("title", r"<title>(.*?)</title>"),
        ("og:title", r'<meta property="og:title" content="(.*?)">'),
        ("twitter:title", r'<meta name="twitter:title" content="(.*?)">'),
    ):
        found = re.search(pattern, home)
        if not found or found.group(1) != TITLE:
            errors.append("homepage %s is not the agreed sentence" % label)


def check_static(errors):
    js = (ROOT / "assets" / "site.js").read_text()
    if "policy.json" in js or "data-version-line" in js:
        errors.append("site.js still fills the version from policy.json")
    joined = "\n".join(p.read_text() for p in ROOT.glob("*.html"))
    joined += "\n".join(p.read_text() for p in ROOT.glob("*/*.html"))
    if "data-version-line" in joined:
        errors.append("a page still has data-version-line")
    readme = (ROOT / "README.md").read_text()
    if "sideload.sha256" in readme or "virustotal.com/gui/file/" in readme:
        errors.append("README still points at policy.json or a fixed VirusTotal file link")
    sitemap = (ROOT / "sitemap.xml").read_text()
    if "lastmod" in sitemap:
        errors.append("sitemap.xml still has lastmod")


def main():
    if "--apply" not in sys.argv and "--check" not in sys.argv:
        raise SystemExit("pass --apply, --check, or both")
    facts = load_facts()
    if "--apply" in sys.argv:
        for path in ROOT.rglob("*.html"):
            text, _counts = apply_html(path, facts)
            path.write_text(text)
        readme = ROOT / "README.md"
        text, counts = apply_readme(readme.read_text(), facts)
        if any(n != 1 for n in counts.values()):
            raise SystemExit("README is missing Version, Download size, or SHA-256")
        readme.write_text(text)
    errors = []
    home_counts = {}
    check_counts = {}
    for path in expected_pages():
        text, counts = apply_html(path, facts)
        if text != path.read_text():
            errors.append("%s does not match policy.json" % path.relative_to(ROOT))
        if path.name == "index.html" and path.parent == ROOT:
            home_counts = counts
        else:
            check_counts = counts
    if home_counts.get("version", 0) < 2 or home_counts.get("mib", 0) < 2:
        errors.append("homepage is missing the version or the size beside a download")
    if check_counts.get("sha256", 0) != 1 or check_counts.get("virustotal", 0) != 1:
        errors.append("check page is missing the hash or the VirusTotal link")
    if check_counts.get("version", 0) < 1 or check_counts.get("mib", 0) < 1:
        errors.append("check page is missing the version or the size")
    readme_text, readme_counts = apply_readme((ROOT / "README.md").read_text(), facts)
    if readme_text != (ROOT / "README.md").read_text() or any(n != 1 for n in readme_counts.values()):
        errors.append("README does not match policy.json")
    check_title(errors)
    check_static(errors)
    if errors:
        raise SystemExit("\n".join(errors))
    print("release facts match %s, %s, %s" % (facts["version"], facts["mib"], facts["sha"]))


if __name__ == "__main__":
    main()
