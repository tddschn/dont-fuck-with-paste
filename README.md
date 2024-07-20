# dont-fuck-with-paste

Annoying login window that doesn't allow you to paste your 128-char long password?  
`dfwp` to the rescue!

`dfwp` uses `pyautogui.write()` to simulate pasting.

https://github.com/user-attachments/assets/3bbf4ec0-981d-42ed-ae7b-f17d9c664d12

- [dont-fuck-with-paste](#dont-fuck-with-paste)
  - [Installation](#installation)
    - [pipx](#pipx)
    - [pip](#pip)
  - [Usage](#usage)
  - [Develop](#develop)

## Installation

Requires Python>=3.10, <4.0.

### pipx

This is the recommended installation method.

```
$ pipx install dont-fuck-with-paste
```

### [pip](https://pypi.org/project/dont-fuck-with-paste/)

```
$ pip install dont-fuck-with-paste
```

## Usage

```plain
$ dfwp -h

usage: dfwp [-h] [-t TEXT] [-S] [-V]

Uses pyautogui.write() to simulate pasting

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Text to simulate pasting, uses copied text if not provided (default: None)
  -S, --no-strip        Do not strip leading/trailing whitespace (default: False)
  -V, --version         show program's version number and exit
```

## Develop

```
$ git clone https://github.com/tddschn/dont-fuck-with-paste.git
$ cd dont-fuck-with-paste
$ poetry install
```