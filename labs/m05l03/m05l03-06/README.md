# m05l03-06 · Logarithm bounds confirm the AVL heights

**Lesson:** [AVL Trees: Rotations That Keep The Guarantee](https://learnsome.tech/learn/algorithms-course/m05l03) (lesson 5.3, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can explain the AVL balance-factor invariant, implement single and double rotations, insert into an AVL tree with automatic rebalancing, and verify that sorted insertion keeps height logarithmic.

In the lesson: The logarithm confirms what the code measured. For fifteen nodes, rounding the base-two logarithm gives four, matching the AVL height after sorted insertion. For one hundred twenty-seven nodes, the rounded logarithm is seven, and the AVL tree reaches exactly height seven. For one thousand twenty-three nodes, the rounded logarithm is ten, the same height the AVL tree achieves. These specific sizes are no coincidence: each is one less than a power of two, so each exactly fills a perfect binary tree. Fifteen equals two to the fourth minus one, and one thousand twenty-three equals two to the tenth minus one. For these sizes, the AVL tree after sorted insertion is as compact as a perfect binary tree can possibly be, confirming that the rotations produce an optimal result.

## Files

- [`starter/shell-logarithm-bounds-confirm-the-avl-heights.py`](starter/shell-logarithm-bounds-confirm-the-avl-heights.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-06/starter`
2. Read `shell-logarithm-bounds-confirm-the-avl-heights.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   import math
   round(math.log2(15))
   round(math.log2(127))
   round(math.log2(1023))
   15 == 2**4 - 1
   1023 == 2**10 - 1
   ```
4. Run it: `python3 -i < shell-logarithm-bounds-confirm-the-avl-heights.py`.
5. Check it from the repository root: `./check m05l03-06`.

## Expected output

```text
4
7
10
True
True
```

## How to check

`./check m05l03-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-logarithm-bounds-confirm-the-avl-heights.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
