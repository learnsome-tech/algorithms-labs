# m05l02-05 · Sorted insertion: the degenerate tree

**Lesson:** [Binary Search Trees: Search, Insert And Delete](https://learnsome.tech/learn/algorithms-course/m05l02) (lesson 5.2, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can insert and search in a binary search tree, implement all three delete cases using the in-order successor, read a sorted in-order traversal as a correctness check, and explain why sorted insertion produces a degenerate tree of linear height.

In the lesson: The worst-case scenario for a BST is a tree built from sorted input. The height function reveals how bad this gets. Two trees receive the same seven values: the first uses a balanced insertion order and the second inserts ascending one through seven. Inserting in balanced order gives a tree of height three, matching a complete binary tree of that size. Inserting in sorted input produces a degenerate tree: each new value is larger than all previous ones, so every node attaches as the right child of the previous last node, forming a linked list disguised as a tree. The height equals seven, matching the node count exactly. That means sorted input makes every BST operation cost linear in n rather than logarithmic, eliminating the advantage a tree should have over a list.

## Files

- [`starter/degenerate.py`](starter/degenerate.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-05/starter`
2. Read `degenerate.py` the way the lesson builds it:
   - Lines 1–12: height function
   - Lines 13–22: sorted input
3. Run it: `python3 degenerate.py`.
4. Check it from the repository root: `./check m05l02-05`.

## Expected output

```text
balanced insert height: 3
sorted insert height: 7
sorted is linear in n: True
```

## How to check

`./check m05l02-05` copies `starter/` into a scratch directory and runs `python3 degenerate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
