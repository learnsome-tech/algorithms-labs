# m06l01-06 · Weighted directed graph with tuple adjacency lists

**Lesson:** [Representing A Graph: Matrix Or Adjacency List](https://learnsome.tech/learn/algorithms-course/m06l01) (lesson 6.1, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can represent a graph as either an adjacency list or a two-dimensional matrix, state the memory cost of each, explain when to prefer one over the other, and encode directed and weighted edges.

In the lesson: This road graph stores every directed edge as a tuple pair of destination and cost. City A has two outgoing roads: one to B at cost four and one to C at cost two. City D is a sink with no outgoing edges. The inner loop unpacks each tuple into destination and cost, and prints one line per directed edge. Notice that A to B and C to B are separate edges; nothing forces a symmetric return. The final line sums the list lengths without halving, giving the exact count of five directed edges. This tuple representation feeds naturally into shortest-path algorithms, which need to read both the destination and the weight at every step.

## Files

- [`starter/weighted_graph.py`](starter/weighted_graph.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-06/starter`
2. Read `weighted_graph.py` the way the lesson builds it:
   - Lines 1–6: tuple pair
   - Lines 7–12: inner loop
3. Run it: `python3 weighted_graph.py`.
4. Check it from the repository root: `./check m06l01-06`.

## Expected output

```text
A -> B weight 4
A -> C weight 2
B -> D weight 5
C -> B weight 1
C -> D weight 8
directed edges: 5
```

## How to check

`./check m06l01-06` copies `starter/` into a scratch directory and runs `python3 weighted_graph.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
