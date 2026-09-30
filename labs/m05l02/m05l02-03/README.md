# m05l02-03 · Search and minimum in a BST

**Lesson:** [Binary Search Trees: Search, Insert And Delete](https://learnsome.tech/learn/algorithms-course/m05l02) (lesson 5.2, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can insert and search in a binary search tree, implement all three delete cases using the in-order successor, read a sorted in-order traversal as a correctness check, and explain why sorted insertion produces a degenerate tree of linear height.

In the lesson: Search and minimum are two operations that naturally follow the invariant. The find function starts at the root: if the tree is empty, return false; if the current node matches, return true; otherwise follow the invariant down. If the target is smaller, recurse left; if larger, recurse right. The recursion terminates either at a matching node or at a null pointer, and the path it takes is exactly the sequence a binary search follows on a sorted array. Minimum is even simpler: walk leftward until no left child exists, then return the value at that node. That node is the smallest because the BST invariant guarantees everything in the left subtree is smaller. Searching for five finds it immediately at the root. Searching for nine never reaches nine because the tree holds no node with that value.

## Files

- [`starter/bstsearch.py`](starter/bstsearch.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-03/starter`
2. Read `bstsearch.py` the way the lesson builds it:
   - Lines 1–13: follow the invariant
   - Lines 14–17: walk leftward
   - Lines 18–22: never reaches nine
3. Run it: `python3 bstsearch.py`.
4. Check it from the repository root: `./check m05l02-03`.

## Expected output

```text
find five: True
find nine: False
minimum: 1
```

## How to check

`./check m05l02-03` copies `starter/` into a scratch directory and runs `python3 bstsearch.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
