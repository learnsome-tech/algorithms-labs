# m02l01-04 · A rolling hash maps keys to buckets

**Lesson:** [What A Hash Function Promises](https://learnsome.tech/learn/algorithms-course/m02l01) (lesson 2.1, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can explain the three core properties a hash function must have, implement a polynomial rolling hash, and reason about why Python randomises string hashing.

In the lesson: This is a polynomial rolling hash, the workhorse of string hashing in most production systems. Start with zero, then for each character multiply the running total by a small prime - here thirty-one - and add the character's numeric code before taking the remainder with the bucket count. The rolling multiplication separates characters that appear in the same positions in different strings, giving far better spread than a simple sum would. Feed eight words into eight buckets and count which bucket each one lands in. The distribution printed on screen shows that no bucket is catastrophically overloaded: most hold one or two words, close to the ideal of one each. A perfect hash function would fill every bucket exactly once, but with only eight words and a general-purpose function this result is entirely acceptable for a real implementation at this scale.

## Files

- [`starter/poly_hash.py`](starter/poly_hash.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-04/starter`
2. Read `poly_hash.py` the way the lesson builds it:
   - Lines 1–5: rolling multiplication
   - Lines 6–9: into eight buckets
   - Lines 10–13: count which bucket
3. Run it: `python3 poly_hash.py`.
4. Check it from the repository root: `./check m02l01-04`.

## Expected output

```text
bucket 0: 0
bucket 1: 1
bucket 2: 1
bucket 3: 0
bucket 4: 2
bucket 5: 0
bucket 6: 2
bucket 7: 2
```

## How to check

`./check m02l01-04` copies `starter/` into a scratch directory and runs `python3 poly_hash.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
