# m05l04-04 · Height arithmetic for a million keys

**Lesson:** [B-Trees: The Structure Behind Every Database Index](https://learnsome.tech/learn/algorithms-course/m05l04) (lesson 5.4, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can explain the B-tree fan-out property, implement search and split-on-insert for a minimal B-tree, print node keys by level, and compute the maximum height for a million keys given a minimum degree.

In the lesson: The arithmetic for a production-scale B-tree is worth working through once. With minimum degree t equal to five hundred twelve, each internal node holds up to one thousand and twenty-three keys and branches up to one thousand and twenty-four ways; that number is the fan-out. The maximum number of levels needed to hold n keys is the ceiling of the logarithm of n plus one in base fan-out. For one million keys at fan-out one thousand and twenty-four, the formula yields just two levels. Two disk reads to reach any key, no matter how large the dataset grows. Two disk reads to serve any point lookup in a table of a million rows is the bargain that explains why every relational database engine uses a B-tree variant for its primary index.

## Files

- [`starter/btheight.py`](starter/btheight.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-04/starter`
2. Read `btheight.py` the way the lesson builds it:
   - Lines 1–5: ceiling of the logarithm
   - Lines 6–8: two disk reads
3. Run it: `python3 btheight.py`.
4. Check it from the repository root: `./check m05l04-04`.

## Expected output

```text
fanout with t equal to 512 is 1024
levels for a million keys: 2
disk reads for any search: 2
```

## How to check

`./check m05l04-04` copies `starter/` into a scratch directory and runs `python3 btheight.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
