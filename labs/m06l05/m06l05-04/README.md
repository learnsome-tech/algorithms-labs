# m06l05-04 · Prim's algorithm: growing from a root vertex

**Lesson:** [Minimum Spanning Trees: Kruskal And Prim](https://learnsome.tech/learn/algorithms-course/m06l05) (lesson 6.5, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement union-find with path compression and union by rank, run Kruskal's algorithm to build a minimum spanning tree edge by edge, and run Prim's algorithm from a starting vertex using a heap.

In the lesson: Prim's algorithm grows the MST from a single root, choosing at each step the cheapest edge that crosses the boundary between the tree and the rest of the graph. The undirected weighted graph uses tuples of neighbour and cost. The visited set starts with A, and the frontier heap holds all edges leaving A in the form of cost and destination pairs. Each iteration pops the cheapest frontier edge; if the destination is already in the tree, skip it; otherwise add the destination to the tree, record the weight, and push all its outgoing edges to the heap. The algorithm adds B at cost one, then C at cost two - the direct path A to C at cost three is already beaten by going through B - and finally D at cost four. The total of seven matches Kruskal, confirming both algorithms produce minimum spanning trees of the same weight.

## Files

- [`starter/prim.py`](starter/prim.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l05/m06l05-04/starter`
2. Read `prim.py` the way the lesson builds it:
   - Lines 1–7: undirected weighted graph
   - Lines 8–10: frontier heap
   - Lines 11–21: cheapest frontier
3. Run it: `python3 prim.py`.
4. Check it from the repository root: `./check m06l05-04`.

## Expected output

```text
add edge to B weight 1
add edge to C weight 2
add edge to D weight 4
total: 7
```

## How to check

`./check m06l05-04` copies `starter/` into a scratch directory and runs `python3 prim.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
