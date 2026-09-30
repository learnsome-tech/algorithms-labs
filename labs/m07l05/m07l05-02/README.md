# m07l05-02 · A rule table that classifies problems

**Lesson:** [Recognising The Pattern](https://learnsome.tech/learn/algorithms-course/m07l05) (lesson 7.5, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can apply a four-question decision procedure to classify an unfamiliar problem as divide-and-conquer, greedy, backtracking, or dynamic programming, implement a rule-table classifier in Python, and verify that three approaches to the same problem agree on the answer.

In the lesson: Four rules encode the decision procedure as a dictionary: each structural property maps directly to the technique that handles it.

Four problems each carry a structural trait matching exactly one rule. The weighted shortest path has the greedy-choice property because fixing the nearest unvisited node is always safe. Count arrangements requires enumerating all valid configurations, so backtracking applies. Common subsequence has overlapping subproblems: the same prefix pair appears in many recursive branches. Sort by comparison splits cleanly and reassembles without overlapping sub-solutions.

The classifier maps each problem to its technique with a single dictionary lookup. The output shows the connection between problem structure and solution structure, which is the decision you need to make before writing a single function.

## Files

- [`starter/classify.py`](starter/classify.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l05/m07l05-02/starter`
2. Read `classify.py` the way the lesson builds it:
   - Lines 1–6: four rules encode
   - Lines 7–13: four problems each
   - Lines 14–16: classifier maps each
3. Run it: `python3 classify.py`.
4. Check it from the repository root: `./check m07l05-02`.

## Expected output

```text
weighted shortest path: greedy algorithm
count arrangements: backtracking
common subsequence: dynamic programming
sort by comparison: divide and conquer
```

## How to check

`./check m07l05-02` copies `starter/` into a scratch directory and runs `python3 classify.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
