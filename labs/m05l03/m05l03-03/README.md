# m05l03-03 · AVL insert with single and double rotations

**Lesson:** [AVL Trees: Rotations That Keep The Guarantee](https://learnsome.tech/learn/algorithms-course/m05l03) (lesson 5.3, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can explain the AVL balance-factor invariant, implement single and double rotations, insert into an AVL tree with automatic rebalancing, and verify that sorted insertion keeps height logarithmic.

In the lesson: The full AVL insert is four conditions checked after every recursive descent. Two apply a single rotation: if the left subtree is too tall and the new value went further left, rotate right; if the right subtree is too tall and the new value went further right, rotate left. The remaining two cases each require a single or double rotation: if the left subtree is too tall but the value went right first, rotate the left child left and then rotate the node right; if the right subtree is too tall but the value went left first, rotate the right child right and then rotate the node left. The four conditions cover every imbalance that can occur. To demonstrate the right-left case, insert one, three, two in that order. The insertion of two creates imbalance at the root, and the code applies a right rotation to the right child followed by a left rotation to the root. The result is a perfectly balanced tree rooted at two.

## Files

- [`starter/avlins.py`](starter/avlins.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-03/starter`
2. Read `avlins.py` the way the lesson builds it:
   - Lines 1–7: single or double
   - Lines 8–17: four conditions
   - Lines 18–21: insert one, three, two
3. Run it: `python3 avlins.py`.
4. Check it from the repository root: `./check m05l03-03`.

## Expected output

```text
after rl rotation, root: 2 height: 2
root bf: 0 left: 1 right: 3
```

## How to check

`./check m05l03-03` copies `starter/` into a scratch directory and runs `python3 avlins.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
