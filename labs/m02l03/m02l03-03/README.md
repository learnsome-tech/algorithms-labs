# m02l03-03 · Trying to hash a list raises TypeError

**Lesson:** [Python Dicts And Sets Under The Hood](https://learnsome.tech/learn/algorithms-course/m02l03) (lesson 2.3, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can explain how Python dicts preserve insertion order, why set membership beats list membership in cost, how to implement a hashable class correctly, and what the hash-equals contract requires.

In the lesson: Hashing a list raises a type error because lists are mutable. An object that can change after you hash it would move to the wrong bucket on the next lookup, breaking the whole contract. The error message says exactly what the problem is: unhashable type list. A tuple, however, is immutable and is perfectly hashable. Calling hash on the same tuple twice in the same process returns the same value both times, so the second print confirms that tuples satisfy the determinism requirement. The rule is not that only primitives are hashable: any immutable object, including custom classes that implement the protocol correctly, can serve as a dict key or set member. The next segment shows what implementing that protocol correctly requires.

## Files

- [`starter/hashability.py`](starter/hashability.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-03/starter`
2. Read `hashability.py`.
3. Run it: `python3 hashability.py`.
4. Check it from the repository root: `./check m02l03-03`.

## Expected output

```text
unhashable type: 'list'
tuple is hashable: True
```

## How to check

`./check m02l03-03` copies `starter/` into a scratch directory and runs `python3 hashability.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
