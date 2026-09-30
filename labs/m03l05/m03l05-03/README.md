# m03l05-03 · Benchmark: front insertion and index access

**Lesson:** [Choosing The Right Sequence](https://learnsome.tech/learn/algorithms-course/m03l05) (lesson 3.5, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Runs, not graded

## Goal

You can apply five diagnostic questions to select the right sequence structure, read a performance benchmark comparing list and deque, and explain why list and deque perform similarly for a pure stack workload.

In the lesson: The benchmark isolates the two operations where list and deque most sharply disagree. Both structures start with twenty thousand elements. The program times twenty thousand front insertions on each: a list shifts every element on every call, making the total work proportional to the square of the size; the deque updates a block pointer in constant time per call. Then the program times twenty thousand reads from the midpoint of each structure. A list delivers any element in constant time by simple arithmetic on the contiguous block; the deque must count across blocks to reach the midpoint, taking time proportional to the distance from the nearest end. The results are printed as booleans: deque wins front insertion, list wins middle access. Each result is guaranteed to be true by the structural properties of the two designs.

## Files

- [`starter/seqbench.py`](starter/seqbench.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-03/starter`
2. Read `seqbench.py` the way the lesson builds it:
   - Lines 1–12: times twenty thousand front insertions
   - Lines 13–21: printed as booleans
3. Run it: `python3 seqbench.py`.
4. Check it from the repository root: `./check m03l05-03`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
insert at front, deque faster: True
random access, list faster: True
```

## How to check

`./check m03l05-03` copies `starter/` into a scratch directory and runs `python3 seqbench.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
