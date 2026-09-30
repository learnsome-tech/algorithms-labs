# m03l05-02 · Decision table for common scenarios

**Lesson:** [Choosing The Right Sequence](https://learnsome.tech/learn/algorithms-course/m03l05) (lesson 3.5, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can apply five diagnostic questions to select the right sequence structure, read a performance benchmark comparing list and deque, and explain why list and deque perform similarly for a pure stack workload.

In the lesson: This program applies the five-question framework to five concrete scenarios and prints the result as an aligned table. A task queue sends work to a pool of workers in arrival order: the deque suits this because front pops are constant time. An undo history needs both stack ordering and random access to the most recent state: a list used as a stack is the natural match. A stream log retains only the last k messages in bounded memory: a ring buffer fits exactly. A lookup table that fetches data by name is not a sequence at all: a dictionary answers key lookups in constant time and belongs in a different lesson. A fixed numeric buffer needs compact typed storage: an array from the standard library uses four or eight bytes per element rather than a full object pointer. The program renders these five rows in an aligned table so you can scan the reasoning at a glance.

## Files

- [`starter/decision.py`](starter/decision.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-02/starter`
2. Read `decision.py` the way the lesson builds it:
   - Lines 1–7: five concrete scenarios
   - Lines 8–11: scan the reasoning at a glance
3. Run it: `python3 decision.py`.
4. Check it from the repository root: `./check m03l05-02`.

## Expected output

```text
Scenario         Structure  Reason
------------------------------------------------------------
task queue       deque      FIFO, grows at both ends
undo history     list       stack LIFO, random access
stream log       ring       bounded, overwrites oldest
lookup table     dict       keyed, not a sequence
fixed buffer     array      typed, contiguous memory
```

## How to check

`./check m03l05-02` copies `starter/` into a scratch directory and runs `python3 decision.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
