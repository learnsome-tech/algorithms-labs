# m05l02-04 · BST delete: three cases

**Lesson:** [Binary Search Trees: Search, Insert And Delete](https://learnsome.tech/learn/algorithms-course/m05l02) (lesson 5.2, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can insert and search in a binary search tree, implement all three delete cases using the in-order successor, read a sorted in-order traversal as a correctness check, and explain why sorted insertion produces a degenerate tree of linear height.

In the lesson: Delete is the most complex BST operation because removing a node can break the structure that took all those inserts to build. The insert helper here is the same recursive insert you saw before. Delete starts like search: if the tree is empty return nothing; if the target value is smaller, delete it from the left subtree; if larger, delete from the right. The interesting cases arise when you find the node. Case one: no left child, so return the right child directly. Case two: no right child, so return the left child. The two-child case needs the in-order successor: walk right once, then as far left as possible. Copy its value to this node, then delete the successor from the right subtree. The inorder function is a one-liner that makes it easy to verify with inorder output that the tree stays in correct order after each deletion.

## Files

- [`starter/bstdelete.py`](starter/bstdelete.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-04/starter`
2. Read `bstdelete.py` the way the lesson builds it:
   - Lines 1–7: recursive insert
   - Lines 8–16: walk right once
   - Lines 17–22: verify with inorder
3. Run it: `python3 bstdelete.py`.
4. Check it from the repository root: `./check m05l02-04`.

## Expected output

```text
initial: [1, 3, 4, 5, 6, 7, 8]
deleted three: [1, 4, 5, 6, 7, 8]
deleted five: [1, 4, 6, 7, 8]
```

## How to check

`./check m05l02-04` copies `starter/` into a scratch directory and runs `python3 bstdelete.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
