# m06l02-02 · The deque as a FIFO queue

**Lesson:** [Breadth-First Search And Shortest Paths By Hops](https://learnsome.tech/learn/algorithms-course/m06l02) (lesson 6.2, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement BFS with a deque to compute shortest hop distances and reconstruct paths, explain why BFS finds shortest paths in unweighted graphs, and use BFS to compute degrees of separation.

In the lesson: The collections module ships a double-ended queue called deque. Creating one with Alice, then appending Bob and Carol, leaves three items in order of arrival. Calling popleft returns the first in, Alice, which was enqueued first; the next call returns Bob. That first-in first-out discipline is what makes BFS expand in distance order. After two pops, only Carol remains in the deque. In BFS, each vertex enters the deque exactly once when it is first discovered and leaves exactly once when it is processed; the visited set or distance map prevents any vertex from entering twice. Using a plain list and pop from the front would also work but costs proportional to the list length for each removal; the deque pops in constant time from either end.

## Files

- [`starter/shell-the-deque-as-a-fifo-queue.py`](starter/shell-the-deque-as-a-fifo-queue.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-02/starter`
2. Read `shell-the-deque-as-a-fifo-queue.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   from collections import deque
   q = deque(['Alice'])
   q.append('Bob')
   q.append('Carol')
   q.popleft()
   q.popleft()
   q
   ```
4. Run it: `python3 -i < shell-the-deque-as-a-fifo-queue.py`.
5. Check it from the repository root: `./check m06l02-02`.

## Expected output

```text
'Alice'
'Bob'
deque(['Carol'])
```

## How to check

`./check m06l02-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-deque-as-a-fifo-queue.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
