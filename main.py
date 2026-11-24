"""Fortune Cookie for an AI Agent — entry for make.fun.

Writes one fortune line to /output/entry.txt.
The line is one fortune, under 140 characters, in the voice of a fortune slip.
"""
import os

LINE = "A tall, dark stranger waits in your server logs — a bug, and he has been living there rent-free for weeks."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
