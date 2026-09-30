# m04l04-04 · Stability composition: sort secondary then primary

**Lesson:** [Sorting In Real Systems: Stability, Keys And External Sort](https://learnsome.tech/learn/algorithms-course/m04l04) (lesson 4.4, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can sort with key functions and tuple keys, compose sorts by chaining stable passes, and implement a k-way external merge using heapq.merge over temporary files.

In the lesson: Stability composition is a powerful technique when you need a sort that is complex to express as a single key function. Sort by the secondary criterion first, then sort by the primary criterion. Because the second sort is stable, elements with equal primary keys preserve the order that the first sort gave them. The five employee records are sorted first by department in step one, producing engineering alphabetically before marketing, and within each department the original input order is preserved. The two sorted lists appear after step two sorts by descending score: bob and dave both have ninety, and bob came before dave in step one, so bob comes first. Alice and eve both have eighty-five; alice preceded eve in step one, so alice comes first. Carol, the only seventy-five, comes last. The result is: highest score first, ties broken by the earlier department sort.

## Files

- [`starter/stability_comp.py`](starter/stability_comp.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-04/starter`
2. Read `stability_comp.py` the way the lesson builds it:
   - Lines 1–9: five employee records
   - Lines 10–15: two sorted lists appear
3. Run it: `python3 stability_comp.py`.
4. Check it from the repository root: `./check m04l04-04`.

## Expected output

```text
after dept sort: ['alice', 'bob', 'eve', 'carol', 'dave']
after score sort: ['bob', 'dave', 'alice', 'eve', 'carol']
```

## How to check

`./check m04l04-04` copies `starter/` into a scratch directory and runs `python3 stability_comp.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
