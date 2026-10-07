<p align="center">
  <img src="assets/icon.svg" alt="Jasiri" width="96">
</p>

<h1 align="center">Jasiri</h1>

<p align="center"><strong>Put your phone to work.</strong><br>
An AI agent with its own Linux computer inside your Android phone.</p>

<p align="center">
  <a href="https://jasiri.benlester.me">Website</a> ·
  <a href="https://jasiri-dl.benlester.me/jasiri-sideload.apk">Download for Android</a> ·
  <a href="https://github.com/lester-01/aaae/releases">Releases</a> ·
  <a href="https://jasiri.benlester.me/plugins/">Plugins</a>
</p>

---

Ask in plain English and the agent builds, fixes, organizes, and tests your ideas inside a real Linux system on your phone. Power user? Open the terminal and take the wheel. One app, nothing else to install.

## Install

1. Download the APK from the [latest release](https://github.com/lester-01/aaae/releases/latest) or the link above. Android 8 or later, 64-bit.
2. Open it and allow the install when Android asks.
3. Open Jasiri, add an AI key (OpenRouter, OpenAI, or any compatible service), and ask for something.

Each release lists a SHA-256 checksum for the APK. Jasiri is not on Google Play yet.

## Check the APK

The release page lists the SHA-256 of `jasiri-sideload.apk`. After you download the file:

```
sha256sum jasiri-sideload.apk
```

On Windows:

```
Get-FileHash jasiri-sideload.apk -Algorithm SHA256
```

The hash should match the release notes and the `sideload.sha256` value in `policy.json`. The same hash can be opened on VirusTotal as `https://www.virustotal.com/gui/file/` followed by the lowercase hex, with no spaces. That page shows what public scanners reported for the file.

## What it does today

- Builds sites, scripts, and tools from a description, runs them, and shows you.
- Turns photos and documents into spreadsheets and notes (with a model that can see images).
- Gives every chat its own project folder you can open and keep.
- Includes a full terminal on the same system, with a normal package manager.
- Works with your clipboard, and reachable over SSH from your laptop.

Plugins (search your media in plain language, notes, backups, video shrinking, learning labs) are planned. See the [plugin plans](https://jasiri.benlester.me/plugins/).

## Privacy

No account, no ads, no analytics. Your project files stay on your phone. Messages go to the AI provider you choose, with your own key. Details: [privacy](https://jasiri.benlester.me/privacy/).

## License

Free for individuals, including for your own professional work. Teams and companies need a license. This is closed-source software distributed in binary form. See the [terms](https://jasiri.benlester.me/terms/), the [license summary](LICENSE), and the [third-party notices](NOTICES.md).

## Feedback

Bugs, ideas, and plugin requests are welcome through [issues](https://github.com/lester-01/aaae/issues) or at [contact@benlester.me](mailto:contact@benlester.me).

## About this repository

This repository hosts the website at [jasiri.benlester.me](https://jasiri.benlester.me) and the release downloads. It does not contain the app's source code.

`policy.json` is read by installed copies of the app to check for updates. Please do not move or rename it.

---

Built by [Ben Lester](https://benlester.me), a software and systems engineer available for new projects.
