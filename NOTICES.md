# Third-party notices

Jasiri is built with the work of many open-source projects. Thank you to everyone who writes and maintains them. This file lists what ships inside the app and how each part is licensed. Jasiri's own code is proprietary and covered by the [terms](https://jasiri.benlester.me/terms/).

## App components

| Component | License |
| --- | --- |
| Terminal emulator and terminal view (derived from the Android Terminal Emulator and Termux libraries) | Apache 2.0 |
| AndroidX and Material Components | Apache 2.0 |
| OkHttp | Apache 2.0 |
| Markwon (Markdown rendering) and Prism4j (syntax highlighting) | Apache 2.0 |
| Kotlin coroutines | Apache 2.0 |
| Mermaid (diagram rendering) | MIT |
| termux-exec (executable launcher shim) | Apache 2.0 |

## The Linux system

Jasiri ships a Linux user space built from the Termux packages project, plus packages installed later from its package servers. It contains many programs, among them the GNU core utilities, Bash, the Debian package tools (`apt` and `dpkg`), and others. Each program is distributed under its own license, many of them GPL or LGPL. Jasiri runs these as separate programs on the phone and does not combine them with its own code. For the build of the Linux system that Jasiri ships, file paths inside some binaries are adjusted so they work in Jasiri's own storage location. These are modifications under those licenses.

Full license texts for these programs are in the Linux system itself, under `usr/share/doc` and `usr/share/licenses`. The corresponding source code is published by the Termux packages project at <https://github.com/termux/termux-packages>. For a copy of the source of any program in Jasiri under its license, email [contact@benlester.me](mailto:contact@benlester.me).

Termux is a trademark of its owners. Jasiri is an independent product and is not affiliated with or endorsed by the Termux project.

## Website fonts

Bricolage Grotesque, Instrument Sans, and JetBrains Mono, under the SIL Open Font License 1.1. The license texts are in [`assets/fonts`](assets/fonts).

## Trademarks

Android is a trademark of Google LLC. Jasiri is an independent app and is not affiliated with Google. Other product names are trademarks of their respective owners.
