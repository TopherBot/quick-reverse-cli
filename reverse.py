#!/usr/bin/env python3
"""quick-reverse-cli

A minimal utility that reads a string from the command line or STDIN and prints its reversal.

Features:
- No external dependencies.
- Works both as `reverse.py "text"` and as a filter: `cat file | reverse.py`.
"""
import sys

def reverse_string(s: str) -> str:
    return s[::-1]

def main():
    # If arguments are given (excluding the script name), join them as the input string.
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
    else:
        # Otherwise, read everything from stdin.
        input_text = sys.stdin.read()
        # Strip trailing newlines to avoid extra blank line in output.
        input_text = input_text.rstrip('\n')
    if input_text:
        sys.stdout.write(reverse_string(input_text))

if __name__ == "__main__":
    main()
