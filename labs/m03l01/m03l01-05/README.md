# m03l01-05 · Slices as independent copies

**Lesson:** [Arrays: Contiguous Memory And Constant-Time Access](https://learnsome.tech/learn/algorithms-course/m03l01) (lesson 3.1, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can explain why array index access is constant time, measure the memory difference between a typed array and a list, predict the cost of front insertion versus appending, and describe why slicing produces a copy.

In the lesson: Slicing a list with square-bracket notation always returns a brand-new list, not a window into the original. Assign a slice of x from index one to index three and store it in s. The identity check returns false immediately: s and x are two separate objects in memory. Now assign ninety-nine to the first element of s. Go back and evaluate x: nothing in x changes, because the slice copied the pointer values into a fresh list rather than sharing storage. This is a frequent source of confusion for people arriving from environments where slicing may return a view. In standard Python lists, modifying a slice never touches the original. The final evaluation of s shows the mutation you made, while x stays exactly as it was created.

## Files

- [`starter/shell-slices-as-independent-copies.py`](starter/shell-slices-as-independent-copies.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-05/starter`
2. Read `shell-slices-as-independent-copies.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   x = [10, 20, 30, 40]
   s = x[1:3]
   s is x
   s[0] = 99
   x
   s
   ```
4. Run it: `python3 -i < shell-slices-as-independent-copies.py`.
5. Check it from the repository root: `./check m03l01-05`.

## Expected output

```text
False
[10, 20, 30, 40]
[99, 30]
```

## How to check

`./check m03l01-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-slices-as-independent-copies.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
