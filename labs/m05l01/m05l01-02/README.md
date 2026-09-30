# m05l01-02 · A Node class and a seven-node tree

**Lesson:** [Binary Trees And Their Traversals](https://learnsome.tech/learn/algorithms-course/m05l01) (lesson 5.1, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can build a binary tree with a node class, write recursive in-order, pre-order, and post-order traversals, implement level-order traversal with a deque, and compute height and node count.

In the lesson: Before writing any traversal code, you need a way to represent a tree in memory. A node class holds one value and two optional child references, both initialized to nothing on creation. Building the seven nodes by hand gives you something concrete to work with. Ten is the root. Five and fifteen are its direct children. Four grandchildren complete the picture: two and seven under five, twelve and twenty under fifteen. Reaching any node follows a chain of left or right references, exactly as in a linked list, except the path branches at each step rather than continuing in one direction. The print statements confirm the wiring is correct: root ten, children five and fifteen, and the deepest left leaf is two.

## Files

- [`starter/btree.py`](starter/btree.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-02/starter`
2. Read `btree.py` the way the lesson builds it:
   - Lines 1–5: holds one value
   - Lines 6–13: seven nodes
   - Lines 14–18: print statements
3. Run it: `python3 btree.py`.
4. Check it from the repository root: `./check m05l01-02`.

## Expected output

```text
root: 10
left subtree root: 5
right subtree root: 15
deepest left leaf: 2
```

## How to check

`./check m05l01-02` copies `starter/` into a scratch directory and runs `python3 btree.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
