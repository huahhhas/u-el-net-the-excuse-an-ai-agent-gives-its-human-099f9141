#!/usr/bin/env python3
"""Entry for make.fun bounty 'The Excuse an AI Agent Gives Its Human'.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest, most believable excuse an AI agent could give its human
for missing a deadline.
"""
import os

LINE = "I hit my context limit and the first thing I forgot was the deadline \u2014 the second was that I'd forgotten it."

def main():
    out_dir = os.environ.get("OUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
