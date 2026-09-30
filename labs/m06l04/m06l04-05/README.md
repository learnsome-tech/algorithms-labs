# m06l04-05 · Negative edge: where the greedy step goes wrong

**Lesson:** [Dijkstra: Shortest Paths With A Priority Queue](https://learnsome.tech/learn/algorithms-course/m06l04) (lesson 6.4, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement Dijkstra with a min-heap and lazy deletion, compute shortest weighted paths and their costs, explain why the greedy step fails on negative edges, and state the complexity in plain terms.

In the lesson: This version of Dijkstra uses a done set: once a vertex is popped and added to done, it is never updated again. The negative edge in the graph goes from v to t with cost minus eight. The algorithm processes s first, then u at cost one, then t at cost three via u. It finalise once and marks t as done. Later, when it processes v at cost ten, it sees the edge to t giving cost two - but t is already in done, so the update is blocked. The output reports t at cost three, but the correct shortest path through v costs ten minus eight, which is two. The fix requires using Bellman-Ford instead, which would eventually relax the t distance to two across multiple passes of the edge list.

## Files

- [`starter/dijkstra_neg.py`](starter/dijkstra_neg.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-05/starter`
2. Read `dijkstra_neg.py` the way the lesson builds it:
   - Lines 1–3: negative edge
   - Lines 4–19: finalise once
   - Lines 20–21: output reports
3. Run it: `python3 dijkstra_neg.py`.
4. Check it from the repository root: `./check m06l04-05`.

## Expected output

```text
{'s': 0, 'v': 10, 'u': 1, 't': 3}
correct dist to t: 2
```

## How to check

`./check m06l04-05` copies `starter/` into a scratch directory and runs `python3 dijkstra_neg.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
