# m05l03-04 · Sorted insertion: AVL height stays logarithmic

**Lesson:** [AVL Trees: Rotations That Keep The Guarantee](https://learnsome.tech/learn/algorithms-course/m05l03) (lesson 5.3, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can explain the AVL balance-factor invariant, implement single and double rotations, insert into an AVL tree with automatic rebalancing, and verify that sorted insertion keeps height logarithmic.

In the lesson: The height comparison runs for three values of n that are each one less than a power of two: fifteen, one hundred twenty-seven, and one thousand twenty-three. Each fills a perfect binary tree exactly, so the expected AVL height is the exponent. Inserting them in sorted ascending order into a plain BST produces a linked chain with height equal to n. Inserting the same sequences into the AVL tree keeps height logarithmic because each rotation that fires restores the local balance factor before the insertion returns. For one thousand twenty-three sorted elements, the AVL tree reaches height ten while the plain BST reaches height one thousand twenty-three. That difference is the practical reason self-balancing trees exist in production databases and search indexes where the insertion order cannot be controlled.

## Files

- [`starter/avlheight.py`](starter/avlheight.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-04/starter`
2. Read `avlheight.py` the way the lesson builds it:
   - Lines 1–17: three values
   - Lines 18–21: practical reason
3. Run it: `python3 avlheight.py`.
4. Check it from the repository root: `./check m05l03-04`.

## Expected output

```text
n=15: avl height 4, sorted bst height 15
n=127: avl height 7, sorted bst height 127
n=1023: avl height 10, sorted bst height 1023
```

## How to check

`./check m05l03-04` copies `starter/` into a scratch directory and runs `python3 avlheight.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
