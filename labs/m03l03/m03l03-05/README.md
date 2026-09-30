# m03l03-05 · Simulating a print queue with deque

**Lesson:** [Stacks And Queues: Last In Or First In](https://learnsome.tech/learn/algorithms-course/m03l03) (lesson 3.3, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can implement a stack using a Python list and a queue using a deque, explain the ordering discipline of each, use a stack to check balanced brackets, and measure why list.pop(0) is a poor queue implementation.

In the lesson: The print queue wraps a deque with two functions. Submitting a job appends it to the right end of the deque and prints a confirmation. Processing pops the leftmost element, which is the oldest job waiting, and prints it. When the deque is empty, process prints idle instead. The simulation submits three jobs, processes two, submits a fourth, then drains the queue with three final calls. You can see the jobs leaving in exactly the order they arrived: report, slides, photo, invoice. The fourth call after the queue empties prints idle. The deque enforces first-in, first-out automatically, and none of the code inside submit or process touches the middle of the deque at any point.

## Files

- [`starter/printqueue.py`](starter/printqueue.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-05/starter`
2. Read `printqueue.py` the way the lesson builds it:
   - Lines 1–6: submitting a job appends it
   - Lines 7–15: jobs leaving in exactly the order
3. Run it: `python3 printqueue.py`.
4. Check it from the repository root: `./check m03l03-05`.

## Expected output

```text
queued: report.pdf
queued: slides.pdf
queued: photo.jpg
printing: report.pdf
printing: slides.pdf
queued: invoice.pdf
printing: photo.jpg
printing: invoice.pdf
idle
```

## How to check

`./check m03l03-05` copies `starter/` into a scratch directory and runs `python3 printqueue.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
