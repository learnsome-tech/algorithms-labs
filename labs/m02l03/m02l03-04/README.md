# m02l03-04 · Implementing the hash-equals contract on a class

**Lesson:** [Python Dicts And Sets Under The Hood](https://learnsome.tech/learn/algorithms-course/m02l03) (lesson 2.3, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can explain how Python dicts preserve insertion order, why set membership beats list membership in cost, how to implement a hashable class correctly, and what the hash-equals contract requires.

In the lesson: This Point class demonstrates the contract. The equals method compares coordinates. The hash method takes the coordinates as a tuple and hands the hashing work to the built-in, choosing to delegate to a tuple because two equal points must produce equal hashes, and the tuple of their coordinates is both stable and equal for equal points. Now create two distinct objects with the same coordinates. Because their hashes agree and their equals method returns true, they behave as the same key: one can be added to a set and the other will be found in it, and you can look up by one and retrieve a value stored under the other. Breaking this contract - defining equals but leaving hash unchanged, or changing the hash after storing - produces silently wrong behaviour that is extremely hard to debug.

## Files

- [`starter/hashcontract.py`](starter/hashcontract.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-04/starter`
2. Read `hashcontract.py` the way the lesson builds it:
   - Lines 1–7: delegate to a tuple
   - Lines 8–9: two distinct objects
   - Lines 10–15: look up
3. Run it: `python3 hashcontract.py`.
4. Check it from the repository root: `./check m02l03-04`.

## Expected output

```text
True
True
True
origin
```

## How to check

`./check m02l03-04` copies `starter/` into a scratch directory and runs `python3 hashcontract.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
