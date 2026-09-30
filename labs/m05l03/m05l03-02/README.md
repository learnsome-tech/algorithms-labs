# m05l03-02 · Left rotation: fixing a right-heavy chain

**Lesson:** [AVL Trees: Rotations That Keep The Guarantee](https://learnsome.tech/learn/algorithms-course/m05l03) (lesson 5.3, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can explain the AVL balance-factor invariant, implement single and double rotations, insert into an AVL tree with automatic rebalancing, and verify that sorted insertion keeps height logarithmic.

In the lesson: The helpers are compact because we cache height inside each node. The height function returns zero for a missing node, sidestepping a null check in every caller. Fix recomputes the stored height from the two children after any structural change, keeping the cache accurate. The balance factor function subtracts right height from left height; a negative value means the right side is heavier. To isolate the rotation, build a right-skewed three-node chain by hand: one, then two on its right, then three on two's right. Fix both internal heights so the stored values are correct. The balance factor at the root is now minus two, meaning the tree is imbalanced at the root. A single left rotation swaps the root and its right child, making two the top node. After the single left rotation, the root value is two, children are one and three, and height is two.

## Files

- [`starter/avlrotate.py`](starter/avlrotate.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-02/starter`
2. Read `avlrotate.py` the way the lesson builds it:
   - Lines 1–7: balance factor
   - Lines 8–12: imbalanced at the root
   - Lines 13–18: single left rotation
3. Run it: `python3 avlrotate.py`.
4. Check it from the repository root: `./check m05l03-02`.

## Expected output

```text
before rotation, bf at root: -2
after left rotation, root value: 2
left child: 1 right child: 3
new root height: 2
```

## How to check

`./check m05l03-02` copies `starter/` into a scratch directory and runs `python3 avlrotate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
