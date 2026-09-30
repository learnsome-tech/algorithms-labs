# m03l03-03 · Balanced brackets with a stack

**Lesson:** [Stacks And Queues: Last In Or First In](https://learnsome.tech/learn/algorithms-course/m03l03) (lesson 3.3, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can implement a stack using a Python list and a queue using a deque, explain the ordering discipline of each, use a stack to check balanced brackets, and measure why list.pop(0) is a poor queue implementation.

In the lesson: A stack is the natural tool for checking whether brackets balance, because the most recently opened bracket must be the first one closed. The function builds a dictionary that maps each opener to its expected closer. When the loop sees an opening bracket, it pushes that character onto the stack. When it sees a closing bracket, it checks two things: the stack must not be empty, and the top of the stack must be the opener that matches this closer. Either failure returns false immediately. When the loop finishes, the stack must be empty: any remaining items represent openers that never found their closers. The four test strings show a balanced arithmetic expression, a nested mixed-bracket structure, an unclosed double opening, and a mismatched pair where round and square brackets are interleaved incorrectly.

## Files

- [`starter/brackets.py`](starter/brackets.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-03/starter`
2. Read `brackets.py` the way the lesson builds it:
   - Lines 1–3: that maps each opener
   - Lines 4–11: stack must be empty
   - Lines 12–15: four test strings
3. Run it: `python3 brackets.py`.
4. Check it from the repository root: `./check m03l03-03`.

## Expected output

```text
(a+b)*(c-d) -> True
[1,{2,3}] -> True
((open -> False
([)] -> False
```

## How to check

`./check m03l03-03` copies `starter/` into a scratch directory and runs `python3 brackets.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
