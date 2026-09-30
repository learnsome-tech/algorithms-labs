# m02l02-02 · A chaining hash map stores pairs in bucket lists

**Lesson:** [Hash Tables: Chaining, Open Addressing And Load Factor](https://learnsome.tech/learn/algorithms-course/m02l02) (lesson 2.2, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can implement a chaining hash map and a linear-probing open-addressed table, explain what the load factor measures, and identify when and why a table must resize.

In the lesson: Here is a minimal chaining hash map. The slot function derives a stable integer from any key using a cryptographic digest and takes the remainder with the bucket count. The class holds the bucket count and a list of empty lists, one per bucket. Put walks the chain at the computed slot: if it finds an existing entry with a matching key it updates the value, otherwise it appends a new pair. Get performs the same walk and returns the value on a match. Six words go in with their character counts, and the bucket list at the bottom shows how they spread across eight slots. Four buckets contain a single pair, one has two, and three are empty: that is normal for a lightly loaded table. The get call for cat returns three because cat is three letters long.

## Files

- [`starter/chain.py`](starter/chain.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-02/starter`
2. Read `chain.py` the way the lesson builds it:
   - Lines 1–4: stable integer
   - Lines 5–16: walks the chain
   - Lines 17–22: six words go in
3. Run it: `python3 chain.py`.
4. Check it from the repository root: `./check m02l02-02`.

## Expected output

```text
[1, 1, 0, 0, 2, 0, 1, 1]
3
```

## How to check

`./check m02l02-02` copies `starter/` into a scratch directory and runs `python3 chain.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
