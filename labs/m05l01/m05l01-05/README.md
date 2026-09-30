# m05l01-05 · Height and node count

**Lesson:** [Binary Trees And Their Traversals](https://learnsome.tech/learn/algorithms-course/m05l01) (lesson 5.1, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can build a binary tree with a node class, write recursive in-order, pre-order, and post-order traversals, implement level-order traversal with a deque, and compute height and node count.

In the lesson: Two measurements that come up constantly are height and node count. The height function is recursive: at a null node return zero, otherwise return one plus the max of the left and right subtree heights. Taking the max picks the deeper branch, not the average, because the height of a subtree is limited by its deepest path. Count follows the same pattern: at a null node return zero, otherwise return one plus left plus right, summing all descendants in one pass. For the seven-node example, height returns three because the tree has three levels of edges, and count returns seven. A complete binary tree of height three would hold fifteen nodes, so seven tells you this tree is missing positions. These two numbers together quickly characterize whether a tree is dense or sparse.

## Files

- [`starter/treesize.py`](starter/treesize.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-05/starter`
2. Read `treesize.py` the way the lesson builds it:
   - Lines 1–6: one plus the max
   - Lines 7–10: one plus left plus right
   - Lines 11–17: height returns three
3. Run it: `python3 treesize.py`.
4. Check it from the repository root: `./check m05l01-05`.

## Expected output

```text
height: 3
node count: 7
```

## How to check

`./check m05l01-05` copies `starter/` into a scratch directory and runs `python3 treesize.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
