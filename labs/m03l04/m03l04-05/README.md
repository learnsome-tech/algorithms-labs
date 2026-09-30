# m03l04-05 · A ring buffer with head and tail indices

**Lesson:** [Deques And Ring Buffers](https://learnsome.tech/learn/algorithms-course/m03l04) (lesson 3.4, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can use a deque with maxlen as a sliding window, implement a ring buffer with head and tail indices and modulo wraparound, and compute a moving average over a data stream using the ring buffer.

In the lesson: The ring buffer class initialises with a fixed-size list of none values, setting head, tail, and size to zero. When you push a value into a full buffer, the head advances by one modulo the capacity, discarding the oldest element while keeping size constant. When the buffer still has room, size increments instead, and the head stays where it is. The value is always written at the tail slot, and the tail then advances by one modulo the capacity. The items method reads from head for size steps, wrapping indices around using modulo arithmetic to stay within the allocated slots. Pushing four values into a capacity-four buffer fills it exactly. Head advances when fifty arrives, and the oldest element ten is overwritten. The wraparound works correctly when sixty follows: thirty, forty, fifty, sixty is the final window.

## Files

- [`starter/ringbuf.py`](starter/ringbuf.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-05/starter`
2. Read `ringbuf.py` the way the lesson builds it:
   - Lines 1–7: ring buffer class initialises
   - Lines 8–14: Head advances when fifty arrives
   - Lines 15–22: wraparound works correctly
3. Run it: `python3 ringbuf.py`.
4. Check it from the repository root: `./check m03l04-05`.

## Expected output

```text
[10, 20, 30, 40]
[20, 30, 40, 50]
[30, 40, 50, 60]
```

## How to check

`./check m03l04-05` copies `starter/` into a scratch directory and runs `python3 ringbuf.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
