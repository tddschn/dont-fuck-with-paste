#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2024-07-20
Purpose: Use pyautogui.write() to simulate pasting
"""

import argparse

from dont_fuck_with_paste import __version__


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Uses pyautogui.write() to simulate pasting",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-t",
        "--text",
        help="Text to simulate pasting, uses copied text if not provided",
        type=str,
        default=None,
    )

    parser.add_argument(
        "-S",
        "--no-strip",
        help="Do not strip leading/trailing whitespace",
        action="store_true",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    import pyautogui
    import pyperclip

    text = args.text if args.text else pyperclip.paste()
    if not args.no_strip:
        text = text.strip()

    if text:
        pyautogui.write(text)
    else:
        print(
            "No text to paste. Please provide text with -t option or ensure clipboard is not empty."
        )


if __name__ == "__main__":
    main()
