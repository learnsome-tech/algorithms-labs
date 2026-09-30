# m07l03-03 · Subset sum: how pruning cuts the search tree

**Lesson:** [Backtracking: Search With Pruning](https://learnsome.tech/learn/algorithms-course/m07l03) (lesson 7.3, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can implement backtracking with pruning, count solutions for N-queens and compare solution counts across board sizes, measure how much pruning reduces the nodes visited versus exhaustive search, and generate permutations with a recursive generator.

In the lesson: Subset sum asks whether any subset of a list sums to a given target. The pruned version adds one constraint: if the running total already exceeds the target, adding more positive numbers cannot help, so the branch is abandoned. When cur exceeds the target, return immediately without exploring further.

The unpruned version checks whether the running total equals the target when all items are exhausted. It always explores both the include-this-item and skip-this-item choices at every step, generating a full binary tree of depth equal to the list length.

For the list of ten, twenty, thirty, forty, and fifty with a target of fifteen, the pruned version visits nineteen nodes while the unpruned version visits all sixty-three. The target is fifteen and every element is at least ten, so including any two elements immediately exceeds the target. Measuring both approaches in the same run shows the concrete saving.

## Files

- [`starter/subsum.py`](starter/subsum.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l03/m07l03-03/starter`
2. Read `subsum.py` the way the lesson builds it:
   - Lines 1–9: cur exceeds the target
   - Lines 10–16: unpruned version
   - Lines 17–22: measuring both
3. Run it: `python3 subsum.py`.
4. Check it from the repository root: `./check m07l03-03`.

## Expected output

```text
pruned nodes: 19
unpruned nodes: 63
```

## How to check

`./check m07l03-03` copies `starter/` into a scratch directory and runs `python3 subsum.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
