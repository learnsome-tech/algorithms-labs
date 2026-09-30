# m03l04-03 · Maximum value in each sliding window

**Lesson:** [Deques And Ring Buffers](https://learnsome.tech/learn/algorithms-course/m03l04) (lesson 3.4, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can use a deque with maxlen as a sliding window, implement a ring buffer with head and tail indices and modulo wraparound, and compute a moving average over a data stream using the ring buffer.

In the lesson: The sliding max function walks a data sequence and maintains a maxlen deque as the window. Each value is appended to the window. Once the window reaches its full size k, the current maximum of the window contents is recorded. The maxlen parameter handles eviction automatically: when the window is full and a new element arrives, the oldest element falls off the left without any explicit removal code. The data here starts at three and contains the value nine as its peak at position five. With a window size of three, there are eight windows in total. The output shows the maximum rising from four to nine as nine enters the window, staying at nine while nine is present in any of the three slots, then dropping to six once nine leaves. The deque holds exactly three elements throughout the scan.

## Files

- [`starter/sliding.py`](starter/sliding.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-03/starter`
2. Read `sliding.py` the way the lesson builds it:
   - Lines 1–9: window reaches its full size
   - Lines 10–13: nine enters the window
3. Run it: `python3 sliding.py`.
4. Check it from the repository root: `./check m03l04-03`.

## Expected output

```text
data: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
max per window: [4, 4, 5, 9, 9, 9, 6, 6]
```

## How to check

`./check m03l04-03` copies `starter/` into a scratch directory and runs `python3 sliding.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
