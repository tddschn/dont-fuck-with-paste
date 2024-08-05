# dont-fuck-with-paste

Annoying login window that doesn't allow you to paste your 128-char long password?  
`dfwp` to the rescue!

`dfwp` uses `keyboard.write()` to simulate pasting.

https://github.com/user-attachments/assets/3bbf4ec0-981d-42ed-ae7b-f17d9c664d12

Demo: using `dfwp` to deal with trading software's unpastable login text fields.

- [dont-fuck-with-paste](#dont-fuck-with-paste)
  - [Installation](#installation)
    - [pipx](#pipx)
    - [pip](#pip)
  - [Usage](#usage)
    - [On the Command Line](#on-the-command-line)
    - [Invoking `dfwp` without A Terminal](#invoking-dfwp-without-a-terminal)
  - [Develop](#develop)
  - [Credits](#credits)

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

### On the Command Line

Either `dfwp` or `dont-fuck-with-paste` works.

```plain
$ dfwp -h

usage: dfwp [-h] [-t TEXT] [-S] [-V]

Uses keyboard.write() to simulate pasting

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Text to simulate pasting, uses copied text if not provided (default: None)
  -S, --no-strip        Do not strip leading/trailing whitespace (default: False)
  -V, --version         show program's version number and exit
```

### Invoking `dfwp` without A Terminal

You can install the tool using `pipx install dont-fuck-with-paste` and use software like Alfred / Keyboard Maestro / Raycast to invoke the simulated pasting by running `dfwp` or `~/.local/bin/dfwp` with a keyboard shortcut or keyword.

## Develop

```
$ git clone https://github.com/tddschn/dont-fuck-with-paste.git
$ cd dont-fuck-with-paste
$ poetry install
```

## Credits

The naming was inspired by a browser extension with a similar name.