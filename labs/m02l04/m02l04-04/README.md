# m02l04-04 · Integer hashes are stable across all runs

**Lesson:** [Collisions In Practice And Hash Flooding](https://learnsome.tech/learn/algorithms-course/m02l04) (lesson 2.4, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can demonstrate how a constant-return hash degrades lookup to linear time, show how anagram-based keys exploit a sum hash, and explain how per-process hash randomisation defends against flooding attacks.

In the lesson: Integer hashes are deterministic and never affected by PYTHONHASHSEED. Hash of one hundred is one hundred, and calling it twice in the same process produces the same result both times. This stability is why integer keys are safe to use in hash tables that need reproducible behaviour. The randomisation only applies to strings, bytes, and datetime objects. So if you use integer identifiers as dict keys, the bucket assignment is consistent across every run of your program; if you use strings, it changes each time the interpreter starts. That distinction is exactly why the demonstrations in this module use hashlib for string-keyed tables rather than relying on the built-in hash: we need the bucket assignments to be predictable so the output shown on screen matches what Python actually prints.

## Files

- [`starter/shell-integer-hashes-are-stable-across-all-runs.py`](starter/shell-integer-hashes-are-stable-across-all-runs.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-04/starter`
2. Read `shell-integer-hashes-are-stable-across-all-runs.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   hash(100)
   hash(100) == hash(100)
   hash(0)
   ```
4. Run it: `python3 -i < shell-integer-hashes-are-stable-across-all-runs.py`.
5. Check it from the repository root: `./check m02l04-04`.

## Expected output

```text
100
True
0
```

## How to check

`./check m02l04-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-integer-hashes-are-stable-across-all-runs.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
