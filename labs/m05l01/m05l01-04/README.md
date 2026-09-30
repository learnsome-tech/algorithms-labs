# m05l01-04 · Level-order traversal with a deque

**Lesson:** [Binary Trees And Their Traversals](https://learnsome.tech/learn/algorithms-course/m05l01) (lesson 5.1, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can build a binary tree with a node class, write recursive in-order, pre-order, and post-order traversals, implement level-order traversal with a deque, and compute height and node count.

In the lesson: The three recursive traversals all follow a depth-first pattern: they sink into one subtree and exhaust it before visiting a sibling. Level-order reverses that priority and scans level by level across every row from the root down. The algorithm uses a queue: enqueue the root, then repeat, dequeuing a node, recording it, and enqueuing its children. The deque from the collections module gives popleft in constant time; popping the front of a plain list costs linear time per step. Load the same seven-node tree and run the function: ten comes out first, then five and fifteen side by side on the second level, then the four grandchildren across the bottom in breadth-first order. That visit sequence is the foundation of breadth-first search on general graphs, which arrives in the module on graph algorithms.

## Files

- [`starter/levelorder.py`](starter/levelorder.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-04/starter`
2. Read `levelorder.py` the way the lesson builds it:
   - Lines 1–6: level by level
   - Lines 7–15: popleft in constant
   - Lines 16–21: run the function
3. Run it: `python3 levelorder.py`.
4. Check it from the repository root: `./check m05l01-04`.

## Expected output

```text
level-order: [10, 5, 15, 2, 7, 12, 20]
```

## How to check

`./check m05l01-04` copies `starter/` into a scratch directory and runs `python3 levelorder.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
