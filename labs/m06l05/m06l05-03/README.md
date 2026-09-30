# m06l05-03 · Kruskal's algorithm: growing the MST edge by edge

**Lesson:** [Minimum Spanning Trees: Kruskal And Prim](https://learnsome.tech/learn/algorithms-course/m06l05) (lesson 6.5, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement union-find with path compression and union by rank, run Kruskal's algorithm to build a minimum spanning tree edge by edge, and run Prim's algorithm from a starting vertex using a heap.

In the lesson: Kruskal's algorithm sorts the edge list by weight, then processes edges from cheapest to most expensive. For each edge, union-find decides whether adding it would create a cycle: if the two endpoints already share a root, skip it; otherwise merge their components and add the edge to the MST. The sorted edge list is processed from weight one upward. Edge A to B at weight one is chosen. Edge B to C at weight two is chosen. Edge A to C at weight three is skipped because A and C are already connected through B. Edge B to D at weight four is chosen, completing the spanning tree with three edges for four vertices. Edge C to D at weight five is then skipped. The total weight is seven, which matches Prim's result on the same graph. The MST uses exactly V minus one edges, and Kruskal always finds the minimum because of the cut property.

## Files

- [`starter/kruskal.py`](starter/kruskal.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l05/m06l05-03/starter`
2. Read `kruskal.py` the way the lesson builds it:
   - Lines 1–5: sorted edge list
   - Lines 6–15: create a cycle
   - Lines 16–21: chosen edge
3. Run it: `python3 kruskal.py`.
4. Check it from the repository root: `./check m06l05-03`.

## Expected output

```text
A - B weight 1
B - C weight 2
B - D weight 4
total: 7
```

## How to check

`./check m06l05-03` copies `starter/` into a scratch directory and runs `python3 kruskal.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
