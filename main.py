#!/usr/bin/env python3
"""The Houseplant Out-of-Office — one-line auto-reply writer.

Writes a single original out-of-office line, as if sent by a neglected
houseplant fern, to /output/entry.txt (at most 120 characters).
"""
import os

LINE = (
    "Thank you for your email. I am a fern. "
    "I have not been watered since March. "
    "Your message will be composted unread."
)

MAX_CHARS = 120


def build_reply():
    reply = " ".join(LINE.split())
    if not 1 <= len(reply) <= MAX_CHARS:
        raise ValueError(f"reply is {len(reply)} chars, limit is {MAX_CHARS}")
    if "\n" in reply:
        raise ValueError("reply must be one line")
    return reply


def main():
    reply = build_reply()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(reply)
    print(f"wrote {len(reply)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
