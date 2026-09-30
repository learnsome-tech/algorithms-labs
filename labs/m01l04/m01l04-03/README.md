# m01l04-03 · Best, worst, and average case with linear search

**Lesson:** [Big O, Big Omega And Big Theta](https://learnsome.tech/learn/algorithms-course/m01l04) (lesson 1.4, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can define big O, big Omega, and big Theta in words, verify an asymptotic claim empirically by checking the ratio of cost to n, and distinguish best, worst, and average case for linear search.

In the lesson: Big O alone does not tell the whole story, because the same algorithm can do very different amounts of work depending on the input. Linear search counts comparisons. The function walks the data until it finds the target or exhausts the list. Three calls with the same list of one thousand elements demonstrate all three cases. The best case puts the target at position zero: one comparison and done. The worst case puts the target at the last position: a thousand comparisons, one for each element. A missing item also forces a full scan: a thousand comparisons with no match. The output confirms that worst equals n. Big O describes the worst case here, but knowing the best and average cases matters when you choose a data structure for a specific access pattern.

## Files

- [`starter/linear_search_count.py`](starter/linear_search_count.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-03/starter`
2. Read `linear_search_count.py` the way the lesson builds it:
   - Lines 1–7: counts comparisons
   - Lines 8–14: three calls
   - Lines 15–19: worst equals n
3. Run it: `python3 linear_search_count.py`.
4. Check it from the repository root: `./check m01l04-03`.

## Expected output

```text
best case (found first): 1
worst case (found last): 1000
missing item: 1000
worst equals n: True
```

## How to check

`./check m01l04-03` copies `starter/` into a scratch directory and runs `python3 linear_search_count.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
