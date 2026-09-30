# m02l01-03 · Stable string digests with SHA two-fifty-six

**Lesson:** [What A Hash Function Promises](https://learnsome.tech/learn/algorithms-course/m02l01) (lesson 2.1, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can explain the three core properties a hash function must have, implement a polynomial rolling hash, and reason about why Python randomises string hashing.

In the lesson: Instead of Python's built-in hash, which mixes in a per-process secret and produces a different value on every interpreter launch, we use hashlib. The SHA two-fifty-six function accepts any byte string and returns a digest that never varies: the same text in gives the same hex string out, today, next week, and on a different machine. We encode the text to bytes, compute the digest, and slice off the first sixteen hex characters as a compact identifier. The four print calls below test apple twice and banana and Apple once each. Run it and watch the output panel. The first two calls use different words and land at completely different hex prefixes. The third call repeats apple and gets back the identical prefix as the first call: determinism confirmed. The fourth call shifts just the first letter to upper case and the prefix changes entirely, showing that even a single character difference sends the digest to a far corner of the output space.

## Files

- [`starter/stable_hash.py`](starter/stable_hash.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-03/starter`
2. Read `stable_hash.py` the way the lesson builds it:
   - Lines 1: we use hashlib
   - Lines 2–4: sixteen hex characters
   - Lines 5–9: four print calls
3. Run it: `python3 stable_hash.py`.
4. Check it from the repository root: `./check m02l01-03`.

## Expected output

```text
3a7bd3e2360a3d29
b493d48364afe44d
3a7bd3e2360a3d29
f223faa96f229162
```

## How to check

`./check m02l01-03` copies `starter/` into a scratch directory and runs `python3 stable_hash.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
