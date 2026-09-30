# m06l04-03 · Dijkstra: distances on a weighted road graph

**Lesson:** [Dijkstra: Shortest Paths With A Priority Queue](https://learnsome.tech/learn/algorithms-course/m06l04) (lesson 6.4, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement Dijkstra with a min-heap and lazy deletion, compute shortest weighted paths and their costs, explain why the greedy step fails on negative edges, and state the complexity in plain terms.

In the lesson: The road graph stores five cities, each edge is a tuple of destination and cost. The algorithm starts with only the source in the distance map and pushes it onto the heap with cost zero. Each iteration pops the cheapest entry; if its cost exceeds the recorded best for that vertex, lazy deletion skips it. Otherwise, every outgoing edge is relaxed: if the new cost via this vertex beats the current best for the neighbour, update the map and push a new entry. The output shows the shortest distance from A. Reaching B costs three, not four, because the path through C and then B via C's edge of cost one is cheaper than the direct edge of cost four. The algorithm discovered this cheaper route when it processed C with cost two and found an edge to B costing one.

## Files

- [`starter/dijkstra.py`](starter/dijkstra.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-03/starter`
2. Read `dijkstra.py` the way the lesson builds it:
   - Lines 1–3: road graph
   - Lines 4–16: lazy deletion
   - Lines 17–18: shortest distance
3. Run it: `python3 dijkstra.py`.
4. Check it from the repository root: `./check m06l04-03`.

## Expected output

```text
A distance 0
B distance 3
C distance 2
D distance 8
E distance 4
```

## How to check

`./check m06l04-03` copies `starter/` into a scratch directory and runs `python3 dijkstra.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
