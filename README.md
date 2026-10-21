<p align="center">
  <img src="assets/icon.svg" alt="Jasiri" width="96">
</p>

<h1 align="center">Jasiri</h1>

<p align="center"><strong>Put your phone to work.</strong><br>
A pocket computer, with an integrated AI assistant.</p>

<p align="center">
  <a href="https://jasiri.benlester.me">Website</a> ·
  <a href="https://jasiri-dl.benlester.me/jasiri-sideload.apk">Download for Android</a> ·
  <a href="https://github.com/lester-01/aaae/releases">Releases</a> ·
  <a href="https://jasiri.benlester.me/marketplace/">Marketplace</a>
</p>

---

Jasiri is a pocket computer for Android with an integrated AI assistant. The AI assistant is built into the Linux system on the phone. It uses the same files and the same programs as the terminal. You can also open the terminal and do the work yourself. One app.

## Install

Version: 0.20.1
Download size: about 55 MB
SHA-256: `0f8fa0e25df326b946edd43130ff51e3598c6fd867ee0f72a5cd8453515ebee7`

1. Download the APK from the [latest release](https://github.com/lester-01/aaae/releases/latest) or the link above.
   - Android 8 or later, on a 64-bit phone
   - Jasiri does not need a rooted phone
2. Open it and allow the install when Android asks.
3. Open Jasiri, add an AI API key from OpenRouter, OpenAI, or another compatible service, and ask for something. That service may charge you.

Jasiri is not on Google Play yet.

## Check the APK

The same steps are on the website: [jasiri.benlester.me/check](https://jasiri.benlester.me/check/). After you download the file:

```
sha256sum jasiri-sideload.apk
```

On Windows:

```
Get-FileHash jasiri-sideload.apk -Algorithm SHA256
```

The hash should match the SHA-256 line in Install. PowerShell prints the hash in capitals. Lowercase is the same value.

The signing certificate SHA-256 is `80db1f0580c90d3bb7ec1d06ef1daa9810e8e8e0bdab80ebde9a2ae7e1823202`. It does not change between versions. `keytool -printcert -jarfile jasiri-sideload.apk` prints that fingerprint with colons.

You can look this file up on VirusTotal with the SHA-256 in Install, or upload it yourself at <https://www.virustotal.com/gui/home/upload>. The download size is the Download size line in Install. That page can warn about a few megabytes and still accept the file. VirusTotal’s large upload accepts up to 650 MB.

## What it does today

- Builds sites, scripts, and tools from a description. The AI assistant writes them, runs them, and shows you the result.
- Turns photos and documents into spreadsheets and notes, with a model that can see images.
- Gives every chat its own folder you can open and keep.
- Includes a full terminal on the same Linux system, with a normal package manager.
- Works with your clipboard, and is reachable over SSH from your laptop.

Plugins, including search of your media in plain language, notes, backups, video shrinking, and learning labs, are planned. See the [marketplace](https://jasiri.benlester.me/marketplace/).

## Privacy

No account, no ads, no analytics. Your chat folders stay on your phone. Messages go to the AI provider you choose, with your own AI API key. Details: [privacy](https://jasiri.benlester.me/privacy/).

## License

The core is free to install and use, including for work. It may not be resold or hosted as a service. This is closed-source software distributed in binary form. See the [terms](https://jasiri.benlester.me/terms/), the [license summary](LICENSE), and the [third-party notices](NOTICES.md).

## Feedback

Bugs, ideas, and plugin requests are welcome through [issues](https://github.com/lester-01/aaae/issues) or at [contact@benlester.me](mailto:contact@benlester.me).

## About this repository

This repository hosts the website at [jasiri.benlester.me](https://jasiri.benlester.me) and the release downloads. It does not contain the app's source code.

`policy.json` is read by installed copies of the app to check for updates. Please do not move or rename it. Compare a download with the version, size, and SHA-256 in the sections above.

---

Built by [Ben Lester](https://benlester.me), a software and systems engineer available for new projects.
