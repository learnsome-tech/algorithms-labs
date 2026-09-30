# m05l04-03 · B-tree insert with node splitting

**Lesson:** [B-Trees: The Structure Behind Every Database Index](https://learnsome.tech/learn/algorithms-course/m05l04) (lesson 5.4, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can explain the B-tree fan-out property, implement search and split-on-insert for a minimal B-tree, print node keys by level, and compute the maximum height for a million keys given a minimum degree.

In the lesson: The compact B-tree uses bisect to locate the correct position in a node's sorted key list without a manual loop. The node class tracks keys, children, and a leaf flag; the full method checks whether the key list has reached the maximum size of two t minus one. The split function is the central structural operation: take the middle key and promote it to the parent, then divide the remaining keys and children into two halves across two sibling nodes. The insert non-full function locates the right child slot with bisect and descends. If the chosen child is full, split it first, then decide which of the two new children receives the new key. The top-level insert wraps the root in a new empty root when the root itself is full and splits immediately. Insert eight values and the root holds two keys with three children.

## Files

- [`starter/btinsert.py`](starter/btinsert.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-03/starter`
2. Read `btinsert.py` the way the lesson builds it:
   - Lines 1–10: split function
   - Lines 11–19: right child slot
   - Lines 20–22: eight values
3. Run it: `python3 btinsert.py`.
4. Check it from the repository root: `./check m05l04-03`.

## Expected output

```text
root keys: [3, 5] children: [[1, 2], [4], [6, 7, 8]]
```

## How to check

`./check m05l04-03` copies `starter/` into a scratch directory and runs `python3 btinsert.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
