# m03l02-05 · Sentinel head removes special cases

**Lesson:** [Linked Lists: Nodes, Pointers And Sentinels](https://learnsome.tech/learn/algorithms-course/m03l02) (lesson 3.2, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can implement a singly linked list with push-front, append, delete, and find; explain why a sentinel head eliminates edge cases; and identify workloads where a linked list outperforms a Python list.

In the lesson: The sentinel list class initialises by creating a dummy head node whose value is none. Every operation starts from the sentinel rather than from the actual first data node. Push front inserts the new node after the sentinel by pointing the new node's next at the sentinel's next, then updating the sentinel's next to the new node. Delete walks forward from the sentinel until it finds a node whose next holds the target value, then rewires that next to skip over the target. No special case for an empty list and no special case for deleting the head appear anywhere in the code. The test appends ten, twenty, and thirty, prepends five to make the chain five, ten, twenty, thirty, then deletes ten. The result is five, twenty, thirty: the sentinel absorbed the edge case invisibly.

## Files

- [`starter/sentinel.py`](starter/sentinel.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-05/starter`
2. Read `sentinel.py` the way the lesson builds it:
   - Lines 1–4: sentinel list class initialises
   - Lines 5–22: sentinel absorbed the edge case
3. Run it: `python3 sentinel.py`.
4. Check it from the repository root: `./check m03l02-05`.

## Expected output

```text
5 -> 10 -> 20 -> 30
5 -> 20 -> 30
```

## How to check

`./check m03l02-05` copies `starter/` into a scratch directory and runs `python3 sentinel.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
