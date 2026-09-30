# m03l04-02 · Sliding window with deque maxlen

**Lesson:** [Deques And Ring Buffers](https://learnsome.tech/learn/algorithms-course/m03l04) (lesson 3.4, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can use a deque with maxlen as a sliding window, implement a ring buffer with head and tail indices and modulo wraparound, and compute a moving average over a data stream using the ring buffer.

In the lesson: A deque with a maximum length set to four behaves like a fixed-capacity sliding window. Fill it with four elements and the deque shows all four. Append a fifth and the oldest element, the one at the left, is silently discarded to keep the length at four: only two, three, four, and five remain. Append a sixth and the oldest of the remaining four drops again: only three, four, five, and six stay. The length is always four or fewer regardless of how many items have been appended. This behaviour is exactly what you need when you want to keep only the most recent k items from a data stream without writing any eviction logic yourself. The deque enforces the window boundary automatically on every append.

## Files

- [`starter/shell-sliding-window-with-deque-maxlen.py`](starter/shell-sliding-window-with-deque-maxlen.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-02/starter`
2. Read `shell-sliding-window-with-deque-maxlen.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   from collections import deque
   w = deque(maxlen=4)
   for v in [1,2,3,4]: w.append(v)
   w
   w.append(5)
   w
   w.append(6)
   w
   ```
4. Run it: `python3 -i < shell-sliding-window-with-deque-maxlen.py`.
5. Check it from the repository root: `./check m03l04-02`.

## Expected output

```text
deque([1, 2, 3, 4], maxlen=4)
deque([2, 3, 4, 5], maxlen=4)
deque([3, 4, 5, 6], maxlen=4)
```

## How to check

`./check m03l04-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-sliding-window-with-deque-maxlen.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
