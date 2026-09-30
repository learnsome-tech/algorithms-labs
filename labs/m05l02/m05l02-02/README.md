# m05l02-02 · BST insert and in-order verification

**Lesson:** [Binary Search Trees: Search, Insert And Delete](https://learnsome.tech/learn/algorithms-course/m05l02) (lesson 5.2, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can insert and search in a binary search tree, implement all three delete cases using the in-order successor, read a sorted in-order traversal as a correctness check, and explain why sorted insertion produces a degenerate tree of linear height.

In the lesson: A node class holds one value and two optional child references, both set to nothing on creation. The insert function is recursion on the BST invariant: if the tree is empty, return a new leaf; if the new value is smaller than the root, recurse into the left subtree and replace the left child with the result; if larger, do the same on the right. Inorder traversal follows the left-root-right order: visit the left subtree, record this node, visit the right subtree. For any tree that satisfies the BST property, that order produces every value in ascending sequence. Insert five, three, seven, one, four, six, eight in that order. The printed list shows the values are now sorted regardless of insertion order, and the root is five with children three and seven.

## Files

- [`starter/bstinsert.py`](starter/bstinsert.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-02/starter`
2. Read `bstinsert.py` the way the lesson builds it:
   - Lines 1–5: holds one value
   - Lines 6–14: ascending sequence
   - Lines 15–21: now sorted
3. Run it: `python3 bstinsert.py`.
4. Check it from the repository root: `./check m05l02-02`.

## Expected output

```text
in-order: [1, 3, 4, 5, 6, 7, 8]
root: 5
root left: 3 right: 7
```

## How to check

`./check m05l02-02` copies `starter/` into a scratch directory and runs `python3 bstinsert.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
