# m03l04-06 · Moving average over a live stream

**Lesson:** [Deques And Ring Buffers](https://learnsome.tech/learn/algorithms-course/m03l04) (lesson 3.4, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can use a deque with maxlen as a sliding window, implement a ring buffer with head and tail indices and modulo wraparound, and compute a moving average over a data stream using the ring buffer.

In the lesson: The moving average applies the ring buffer to a monitoring task: tracking a rolling mean over the most recent k measurements in a stream. This version sizes the buffer at three, so it holds the three most recent values at most. For each new value, push places it into the buffer, advancing the tail with wraparound if necessary. The mean method reads all current items using the head and size, sums them, and divides by the count. When only one or two values have arrived, the mean is over the partial window. By the third value, the buffer is full and the mean tracks exactly three values. Each new arrival after that drops the oldest and pulls the mean toward the newest data: when forty arrives, ten leaves and the mean moves from twenty to thirty.

## Files

- [`starter/movavg.py`](starter/movavg.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-06/starter`
2. Read `movavg.py` the way the lesson builds it:
   - Lines 1–17: mean method reads all current items
   - Lines 18–22: pulls the mean toward the newest
3. Run it: `python3 movavg.py`.
4. Check it from the repository root: `./check m03l04-06`.

## Expected output

```text
add 10  mean=10.0
add 20  mean=15.0
add 30  mean=20.0
add 40  mean=30.0
add 50  mean=40.0
```

## How to check

`./check m03l04-06` copies `starter/` into a scratch directory and runs `python3 movavg.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
