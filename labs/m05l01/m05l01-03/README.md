# m05l01-03 · In-order, pre-order and post-order traversals

**Lesson:** [Binary Trees And Their Traversals](https://learnsome.tech/learn/algorithms-course/m05l01) (lesson 5.1, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can build a binary tree with a node class, write recursive in-order, pre-order, and post-order traversals, implement level-order traversal with a deque, and compute height and node count.

In the lesson: A recursive traversal makes one decision: when to visit the current node relative to its children. Inorder defers the visit until after the left subtree: recurse left subtree first, then record this node, then recurse right. Applied to a binary search tree that order always produces a sorted sequence, which is why programmers use inorder output to verify that an insertion went where it should. Preorder visits the root before its children: root comes first, left subtree next, right subtree last. If you need to clone or serialize a tree, preorder gives you the insertion order that would reconstruct the same shape. Post-order delays the visit until both children have been processed: left, then right, then the current node. Compilers and garbage collectors rely on post-order because a node can only be freed or evaluated after all it depends on. We apply all three to produce three different sequences from the same data.

## Files

- [`starter/traversals.py`](starter/traversals.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-03/starter`
2. Read `traversals.py` the way the lesson builds it:
   - Lines 1–5: left subtree first
   - Lines 6–9: root comes first
   - Lines 10–12: delays the visit
   - Lines 13–19: three different sequences
3. Run it: `python3 traversals.py`.
4. Check it from the repository root: `./check m05l01-03`.

## Expected output

```text
inorder: [2, 5, 7, 10, 12, 15, 20]
preorder: [10, 5, 2, 7, 15, 12, 20]
postorder: [2, 7, 5, 12, 20, 15, 10]
```

## How to check

`./check m05l01-03` copies `starter/` into a scratch directory and runs `python3 traversals.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
