# m02l05-02 · A Bloom filter built on SHA two-fifty-six

**Lesson:** [Bloom Filters: Membership Without The Data](https://learnsome.tech/learn/algorithms-course/m02l05) (lesson 2.5, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can implement a Bloom filter using k hash functions derived from SHA two-fifty-six, measure its false-positive rate on a fixed word list, and explain why Bloom filters guarantee zero false negatives.

In the lesson: This Bloom filter uses SHA two-fifty-six to generate k independent positions for each item. The prefix trick - prepending a distinct integer before a colon to the item string - gives k different hash values from one cryptographic function, which is a standard technique for building independent hash functions cheaply. The filter holds sixty-four bits and three hash functions. Add four words, then query all four plus two words that were never added. Every inserted word reports true: zero false negatives, as guaranteed. Elderberry and fig both report false: they are genuinely absent and the filter correctly says so. This is the lucky case - with only four words in a sixty-four-bit array, few bits overlap, so non-members rarely satisfy all three bit checks. A denser filter would start producing false positives.

## Files

- [`starter/bloom_basic.py`](starter/bloom_basic.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-02/starter`
2. Read `bloom_basic.py` the way the lesson builds it:
   - Lines 1–12: k independent positions
   - Lines 13–16: Add four words
   - Lines 17–19: two words that were never added
3. Run it: `python3 bloom_basic.py`.
4. Check it from the repository root: `./check m02l05-02`.

## Expected output

```text
apple in filter: True
banana in filter: True
cherry in filter: True
date in filter: True
elderberry in filter: False
fig in filter: False
```

## How to check

`./check m02l05-02` copies `starter/` into a scratch directory and runs `python3 bloom_basic.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
