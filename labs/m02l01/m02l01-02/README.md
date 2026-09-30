# m02l01-02 · How Python hashes small integers

**Lesson:** [What A Hash Function Promises](https://learnsome.tech/learn/algorithms-course/m02l01) (lesson 2.1, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can explain the three core properties a hash function must have, implement a polynomial rolling hash, and reason about why Python randomises string hashing.

In the lesson: Python's built-in hash function maps small integers to themselves, which you can confirm in the Shell right now. Hash of zero is zero, hash of forty-two is forty-two. That mapping is cheap and stable: the hash of an integer does not change between runs of the same interpreter. There is one famous quirk worth knowing: hash of negative one returns negative two. The Python runtime reserves the value negative one internally as an error signal inherited from C, so when an integer's natural hash would be negative one, it quietly shifts the result to negative two to avoid confusion. That edge case aside, integer hashing is deterministic and constant-time, and you will see it used as a building block when we implement hash tables later in this module.

## Files

- [`starter/shell-how-python-hashes-small-integers.py`](starter/shell-how-python-hashes-small-integers.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-02/starter`
2. Read `shell-how-python-hashes-small-integers.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   hash(0)
   hash(42)
   hash(-1)
   ```
4. Run it: `python3 -i < shell-how-python-hashes-small-integers.py`.
5. Check it from the repository root: `./check m02l01-02`.

## Expected output

```text
0
42
-2
```

## How to check

`./check m02l01-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-how-python-hashes-small-integers.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
