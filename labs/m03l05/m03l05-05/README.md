# m03l05-05 · When list and deque perform alike

**Lesson:** [Choosing The Right Sequence](https://learnsome.tech/learn/algorithms-course/m03l05) (lesson 3.5, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can apply five diagnostic questions to select the right sequence structure, read a performance benchmark comparing list and deque, and explain why list and deque perform similarly for a pure stack workload.

In the lesson: A pure stack that only pushes and pops from the same end never touches the other side, so it does not exercise the structural difference between list and deque. This program pushes and pops thirty thousand times on a list and the same number of times on a deque, timing both. Both structures do constant-time work on every operation when acting as a stack, so their speeds are close. The test checks whether the ratio of the two times falls within a wide but reasonable range and confirms neither is dramatically faster. This result carries a practical message: if your code only needs a stack, a plain Python list is sufficient and already familiar. Importing deque for a pure stack workload adds a dependency without adding performance benefit.

## Files

- [`starter/stackwork.py`](starter/stackwork.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-05/starter`
2. Read `stackwork.py` the way the lesson builds it:
   - Lines 1–5: pure stack that only pushes
   - Lines 6–12: ratio of the two times
3. Run it: `python3 stackwork.py`.
4. Check it from the repository root: `./check m03l05-05`.

## Expected output

```text
stack on list vs deque near equal: True
```

## How to check

`./check m03l05-05` copies `starter/` into a scratch directory and runs `python3 stackwork.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
