# m02l04-02 · Counting comparisons: constant hash versus polynomial hash

**Lesson:** [Collisions In Practice And Hash Flooding](https://learnsome.tech/learn/algorithms-course/m02l04) (lesson 2.4, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can demonstrate how a constant-return hash degrades lookup to linear time, show how anagram-based keys exploit a sum hash, and explain how per-process hash randomisation defends against flooding attacks.

In the lesson: The bad hash always returns zero, placing every key in the same bucket. The good polynomial hash multiplies by thirty-one and accumulates each digit character. The insert function counts how many existing entries the arriving key must step past before appending to its chain - those are the comparisons. Insert twelve keys into sixteen slots and read the comparisons on screen. The constant hash costs sixty-six comparisons for twelve insertions: zero for the first, one for the second, two for the third, and so on up to eleven, summing to sixty-six. The polynomial hash costs exactly one comparison because the twelve string representations of those integers happen to scatter perfectly, with only a single collision in the final pair. This side-by-side comparison is the clearest illustration of why hash function quality matters for correctness as well as performance.

## Files

- [`starter/badhash.py`](starter/badhash.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-02/starter`
2. Read `badhash.py` the way the lesson builds it:
   - Lines 1: always returns zero
   - Lines 2–8: good polynomial
   - Lines 9–20: twelve keys into sixteen
3. Run it: `python3 badhash.py`.
4. Check it from the repository root: `./check m02l04-02`.

## Expected output

```text
bad hash comparisons: 66
good hash comparisons: 1
```

## How to check

`./check m02l04-02` copies `starter/` into a scratch directory and runs `python3 badhash.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
