# m03l01-04 · Counting the cost of front insertion

**Lesson:** [Arrays: Contiguous Memory And Constant-Time Access](https://learnsome.tech/learn/algorithms-course/m03l01) (lesson 3.1, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can explain why array index access is constant time, measure the memory difference between a typed array and a list, predict the cost of front insertion versus appending, and describe why slicing produces a copy.

In the lesson: Every time you insert at position zero, Python must shift every existing element one slot to the right to make room. With ten thousand insertions, the first call shifts zero elements, the second shifts one, the third shifts two, and so on. The total is the sum from zero up to nine thousand nine hundred and ninety-nine, which is just under fifty million shifts. Appending to the back never shifts anything: the next available slot is already there. Ten thousand appends cost ten thousand operations in total. This program models the cost by counting shifts rather than timing them, so the result is exact rather than approximate. It then prints a boolean confirming that the front insert total is larger than the append total. Ten thousand appends cost ten thousand operations. Ten thousand front inserts cost nearly fifty million. The structure of the problem, not the language, determines that gap.

## Files

- [`starter/frontappend.py`](starter/frontappend.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-04/starter`
2. Read `frontappend.py` the way the lesson builds it:
   - Lines 1–3: ten thousand insertions
   - Lines 4–6: Ten thousand appends cost
3. Run it: `python3 frontappend.py`.
4. Check it from the repository root: `./check m03l01-04`.

## Expected output

```text
inserting at front, 10000 calls: 49995000 shifts
appending, 10000 calls: 10000 ops
front insert is costlier: True
```

## How to check

`./check m03l01-04` copies `starter/` into a scratch directory and runs `python3 frontappend.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
