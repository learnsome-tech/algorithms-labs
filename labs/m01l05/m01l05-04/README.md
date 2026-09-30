# m01l05-04 · Python list sizes in the shell

**Lesson:** [Amortised Analysis: Why Append Is Cheap](https://learnsome.tech/learn/algorithms-course/m01l05) (lesson 1.5, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can explain why appending to a dynamic array is amortised constant time by tracing the doubling strategy, compare it to fixed-increment growth, and state the credit argument for the amortised bound.

In the lesson: The shell gives direct evidence of Python's own growth strategy. An empty list occupies fifty-six bytes: that is the object header, with capacity for zero elements. After nine appends the list holds nine elements and occupies one hundred and eighty-four bytes, which means Python reserved more capacity than strictly needed. After nine more appends the list has eighteen elements and occupies two hundred and forty-eight bytes. The list grew but not proportionally: the size grew by sixty-four bytes while the element count only doubled. Python over-allocates to avoid frequent resizes, and the getsizeof numbers confirm that the allocated block is larger than the element count alone would require.

## Files

- [`starter/shell-python-list-sizes-in-the-shell.py`](starter/shell-python-list-sizes-in-the-shell.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-04/starter`
2. Read `shell-python-list-sizes-in-the-shell.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   import sys
   lst = []
   sys.getsizeof(lst)
   for i in range(9): lst.append(i)
   len(lst), sys.getsizeof(lst)
   for i in range(9): lst.append(i)
   len(lst), sys.getsizeof(lst)
   ```
4. Run it: `python3 -i < shell-python-list-sizes-in-the-shell.py`.
5. Check it from the repository root: `./check m01l05-04`.

## Expected output

```text
56
(9, 184)
(18, 248)
```

## How to check

`./check m01l05-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-python-list-sizes-in-the-shell.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
