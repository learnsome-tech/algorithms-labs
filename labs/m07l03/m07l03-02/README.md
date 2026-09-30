# m07l03-02 · N-queens: count solutions and find one example

**Lesson:** [Backtracking: Search With Pruning](https://learnsome.tech/learn/algorithms-course/m07l03) (lesson 7.3, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can implement backtracking with pruning, count solutions for N-queens and compare solution counts across board sizes, measure how much pruning reduces the nodes visited versus exhaustive search, and generate permutations with a recursive generator.

In the lesson: Three sets track which columns and diagonals are occupied. At each row, a column is safe when it does not appear in any of the three sets: the columns set, the sum-diagonal set, and the difference-diagonal set. Both diagonals are captured by the row-plus-column sum and the row-minus-column difference, which remain constant for every cell on the same diagonal.

The base case returns one solution and the current placement tuple when every row has been filled. Otherwise the function counts all solutions and remembers the first one found, so the output shows both the total count and an example arrangement.

The solution tuple is a column index per row: the first number is which column holds the queen in row zero, and so on. Trying each board size from four to eight reveals how rapidly the solution count grows and how the example placements differ at each size.

## Files

- [`starter/nqueens.py`](starter/nqueens.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l03/m07l03-02/starter`
2. Read `nqueens.py` the way the lesson builds it:
   - Lines 1: three sets track
   - Lines 2–13: base case returns
   - Lines 14–17: trying each board size
3. Run it: `python3 nqueens.py`.
4. Check it from the repository root: `./check m07l03-02`.

## Expected output

```text
n=4: 2 solutions, e.g. [1, 3, 0, 2]
n=5: 10 solutions, e.g. [0, 2, 4, 1, 3]
n=6: 4 solutions, e.g. [1, 3, 5, 0, 2, 4]
n=7: 40 solutions, e.g. [0, 2, 4, 6, 1, 3, 5]
n=8: 92 solutions, e.g. [0, 4, 7, 5, 2, 6, 1, 3]
```

## How to check

`./check m07l03-02` copies `starter/` into a scratch directory and runs `python3 nqueens.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
