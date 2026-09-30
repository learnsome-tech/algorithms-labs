# m01l01-02 · Scanning a list to find a user

**Lesson:** [Why Complexity Matters In Production](https://learnsome.tech/learn/algorithms-course/m01l01) (lesson 1.1, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can explain why scanning a list grows linearly with input size while a dictionary lookup stays constant, measure both with the perf counter timer, and describe what input size n means in a complexity argument.

In the lesson: The function on screen is a request handler stripped to its core. It takes a user identifier and a list of known users, and walks the list one element at a time. When it finds a match it returns immediately, so a user near the front is cheap to find. A user near the end, or one that is missing entirely, forces the handler to check every element before it can answer. That is a linear scan: work proportional to the length of the list. Below the function, five names serve as test input and the handler is called twice: once asking for carol and once for zara. Carol returns True after three comparisons, and zara returns False after exhausting all five entries.

## Files

- [`starter/handler_list.py`](starter/handler_list.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-02/starter`
2. Read `handler_list.py` the way the lesson builds it:
   - Lines 1–5: its core
   - Lines 6–7: five names
   - Lines 8–9: twice
3. Run it: `python3 handler_list.py`.
4. Check it from the repository root: `./check m01l01-02`.

## Expected output

```text
True
False
```

## How to check

`./check m01l01-02` copies `starter/` into a scratch directory and runs `python3 handler_list.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
