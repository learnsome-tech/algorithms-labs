# m05l04-05 · Printing B-tree keys level by level

**Lesson:** [B-Trees: The Structure Behind Every Database Index](https://learnsome.tech/learn/algorithms-course/m05l04) (lesson 5.4, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can explain the B-tree fan-out property, implement search and split-on-insert for a minimal B-tree, print node keys by level, and compute the maximum height for a million keys given a minimum degree.

In the lesson: Printing a B-tree by level uses the same breadth-first queue strategy as level-order traversal on a binary tree. The by-level function enqueues the root with depth zero, then dequeues nodes one at a time, extending the row for their depth with their key list, and enqueuing children at depth plus one. The result is a dictionary mapping depth to the key list collected at that depth. This level-by-level scan of the structure confirms balance and shows how keys distribute across levels. Build the same seven-key B-tree we searched earlier: the root holds four, the internal nodes at depth one hold two and six, and the leaves at depth two hold one, three, five, and seven. The level zero row shows just four. The rows below confirm the correct three-level shape.

## Files

- [`starter/btlevels.py`](starter/btlevels.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-05/starter`
2. Read `btlevels.py` the way the lesson builds it:
   - Lines 1–11: scan of the structure
   - Lines 12–15: we searched earlier
   - Lines 16–18: level zero
3. Run it: `python3 btlevels.py`.
4. Check it from the repository root: `./check m05l04-05`.

## Expected output

```text
level 0 : [4]
level 1 : [2, 6]
level 2 : [1, 3, 5, 7]
```

## How to check

`./check m05l04-05` copies `starter/` into a scratch directory and runs `python3 btlevels.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
