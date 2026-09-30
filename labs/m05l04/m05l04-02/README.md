# m05l04-02 · Searching in a manually built B-tree

**Lesson:** [B-Trees: The Structure Behind Every Database Index](https://learnsome.tech/learn/algorithms-course/m05l04) (lesson 5.4, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can explain the B-tree fan-out property, implement search and split-on-insert for a minimal B-tree, print node keys by level, and compute the maximum height for a million keys given a minimum degree.

In the lesson: The B-tree search function captures the core logic compactly. Each node is a tuple of keys, children, and a leaf flag. The search walks the key list left to right until it reaches a slot where the target is not larger than the current key. If that slot holds the exact key, return true. If the node is a leaf, return false because the key is nowhere in the tree. Otherwise recurse into the child at that position. Build the tree by hand to have a concrete structure: the root holds key four, its left child holds two with leaves one and three, its right child holds six with leaves five and seven. Running four searches confirms the logic: one, four, and five are found, and nine is absent because the tree holds only the seven values we put into it.

## Files

- [`starter/btsearch.py`](starter/btsearch.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-02/starter`
2. Read `btsearch.py` the way the lesson builds it:
   - Lines 1–8: search walks
   - Lines 9–13: build the tree
   - Lines 14–16: four searches
3. Run it: `python3 btsearch.py`.
4. Check it from the repository root: `./check m05l04-02`.

## Expected output

```text
search 1 : True
search 4 : True
search 5 : True
search 9 : False
```

## How to check

`./check m05l04-02` copies `starter/` into a scratch directory and runs `python3 btsearch.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
