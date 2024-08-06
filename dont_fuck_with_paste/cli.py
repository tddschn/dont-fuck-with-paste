#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2024-07-20
Purpose: Use keyboard.write() to simulate pasting
"""

import argparse

from dont_fuck_with_paste import __version__


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Uses keyboard.write() to simulate pasting",
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
    parser.add_argument(
        "-d",
        "--delay",
        help="Delay in second(s) between simulated keypresses",
        default=0.02,
        type=float,
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    # import pyautogui
    import keyboard
    import pyperclip

    text = args.text if args.text else pyperclip.paste()
    if not args.no_strip:
        text = text.strip()

    if text:
        # pyautogui.write(text)
        import time

        time.sleep(0.1)
        keyboard.write(text, delay=args.delay, exact=True)
    else:
        print(
            "No text to paste. Please provide text with -t option or ensure clipboard is not empty."
        )


if __name__ == "__main__":
    main()
