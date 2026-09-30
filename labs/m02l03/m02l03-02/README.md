# m02l03-02 · Insertion order and membership cost in practice

**Lesson:** [Python Dicts And Sets Under The Hood](https://learnsome.tech/learn/algorithms-course/m02l03) (lesson 2.3, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can explain how Python dicts preserve insertion order, why set membership beats list membership in cost, how to implement a hashable class correctly, and what the hash-equals contract requires.

In the lesson: Build a dict with keys in a non-alphabetical order and then ask for the key list. Python returns them in insertion order: b, a, c - exactly the sequence you typed. Add a fourth key and the list grows at the end: insertion order is maintained as the table grows. Now compare membership costs. Asking whether nine thousand nine hundred and ninety-nine is in a list of ten thousand integers returns true, and so does asking whether it is in a set of the same integers - the same answer, but the list scanned up to ten thousand items while the set computed a hash and checked one slot. Tuples are hashable because they are immutable: asking whether a tuple is in a set of tuples works as you would expect.

## Files

- [`starter/shell-insertion-order-and-membership-cost-in-pract.py`](starter/shell-insertion-order-and-membership-cost-in-pract.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-02/starter`
2. Read `shell-insertion-order-and-membership-cost-in-pract.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   d = {'b': 2, 'a': 1, 'c': 3}
   list(d.keys())
   d['d'] = 4
   list(d.keys())
   9999 in list(range(10000))
   9999 in set(range(10000))
   (3, 4) in {(1, 2), (3, 4)}
   ```
4. Run it: `python3 -i < shell-insertion-order-and-membership-cost-in-pract.py`.
5. Check it from the repository root: `./check m02l03-02`.

## Expected output

```text
['b', 'a', 'c']
['b', 'a', 'c', 'd']
True
True
True
```

## How to check

`./check m02l03-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-insertion-order-and-membership-cost-in-pract.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
