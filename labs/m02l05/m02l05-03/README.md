# m02l05-03 · Measuring the false-positive rate on a fixed test set

**Lesson:** [Bloom Filters: Membership Without The Data](https://learnsome.tech/learn/algorithms-course/m02l05) (lesson 2.5, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can implement a Bloom filter using k hash functions derived from SHA two-fifty-six, measure its false-positive rate on a fixed word list, and explain why Bloom filters guarantee zero false negatives.

In the lesson: To measure the false-positive rate properly you need a fixed and deterministic test: insert a known set and then probe a completely disjoint set. Build a filter of one hundred and twenty-eight bits with three hash functions, insert twenty words whose names start with word, then probe one hundred non-members whose names start with test. Because the filter uses SHA two-fifty-six and the strings are fixed, the false-positive count is the same every time you run this program. Probe the one hundred non-members and find five false positives, giving a rate of five percent. The theoretical prediction for these parameters is about five percent as well - the expected rate falls as you increase the bit count, and rises as the number of inserted items grows relative to the bit array size.

## Files

- [`starter/bloom_rate.py`](starter/bloom_rate.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-03/starter`
2. Read `bloom_rate.py` the way the lesson builds it:
   - Lines 1–13: Build a filter
   - Lines 14–20: probe one hundred
3. Run it: `python3 bloom_rate.py`.
4. Check it from the repository root: `./check m02l05-03`.

## Expected output

```text
false positives: 5 out of 100
false positive rate: 0.05
```

## How to check

`./check m02l05-03` copies `starter/` into a scratch directory and runs `python3 bloom_rate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
