# The LearnSome.tech >>> session replayer (workers/labs/repl_session.py on the platform), copied unchanged.
"""Replays a Python session typed at the >>> prompt (run_lab.py's `python-repl` runner, as the learner).

  python3 repl_session.py <session.py>

The listing is a recorded session: the lines typed at the prompt, each followed by what Python answered as
`#   ` comments. Every typed line goes to an interactive interpreter in order, which echoes expression
values and errors as the prompt does. The comments are the expected output (grading.js `repl`), so they are
not typed. Errors go to stdout with everything else: the prompt shows them in place, between the answers.
"""
import builtins
import code
import codeop
import os
import re
import sys

# Lines that carry on the block above them at its own indentation.
CONTINUES = re.compile(r'(?:else|elif|except|finally)\b|[)\]}]')


def typed_lines(source):
    for line in source.splitlines():
        # Comments are the recorded answers (or notes); blank lines only ever ended a block, which the
        # next unindented line does here.
        if line.strip() and not line.lstrip().startswith('#'):
            yield line.rstrip()


def block_ends(buffer, line):
    """True when `line` starts a new statement after an unfinished block: at the prompt, the blank line
    typed to end the block is not in the transcript."""
    if line[0].isspace() or CONTINUES.match(line) or buffer[-1].lstrip().startswith('@'):
        return False
    try:
        # Still incomplete with the blank line: an open bracket, and the line continues it.
        return codeop.compile_command('\n'.join(buffer) + '\n', '<console>', 'single') is not None
    except (SyntaxError, ValueError, OverflowError):
        return True


class Screen:
    """stdout as the terminal shows it: remembers whether the output so far ends a line, because the next
    prompt starts on a line of its own in the recorded session (`print(x, end='!')` then `>>>`)."""

    def __init__(self, stream):
        self.stream = stream
        self.at_line_start = True

    def write(self, text):
        if text:
            self.at_line_start = text.endswith('\n')
        return self.stream.write(text)

    def end_line(self):
        if not self.at_line_start:
            self.write('\n')

    def __getattr__(self, name):
        return getattr(self.stream, name)


def main():
    with open(sys.argv[1], encoding='utf-8') as f:
        source = f.read()
    sys.path[0] = ''  # the prompt imports from the current directory
    # One stream, line by line, as on the terminal: errors appear between the answers where they happened.
    sys.stdout.reconfigure(line_buffering=True)
    os.dup2(1, 2)
    screen = Screen(sys.stdout)
    sys.stdout = sys.stderr = screen
    console = code.InteractiveConsole({'__name__': '__main__', '__doc__': None, '__builtins__': builtins})
    more = False
    for line in typed_lines(source):
        if more and block_ends(console.buffer, line):
            console.push('')
        more = console.push(line)
        if not more:
            screen.end_line()
    if more:
        console.push('')
    screen.end_line()


if __name__ == '__main__':
    main()
