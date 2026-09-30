# m06l05-05 · Inspecting the MST edge list

**Lesson:** [Minimum Spanning Trees: Kruskal And Prim](https://learnsome.tech/learn/algorithms-course/m06l05) (lesson 6.5, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement union-find with path compression and union by rank, run Kruskal's algorithm to build a minimum spanning tree edge by edge, and run Prim's algorithm from a starting vertex using a heap.

In the lesson: The three chosen MST edges are already sorted by weight. Their weights sum to seven, which is the minimum cost to connect all four vertices. The edge count is three, which is exactly V minus one for a four-vertex graph. A spanning tree of V vertices always has exactly V minus one edges: one fewer than the vertex count. This is the structural invariant you can check whenever you run a spanning-tree algorithm. If the output contains more or fewer edges, either the algorithm produced a cycle or failed to reach every vertex. Sorting the MST edges by weight also lets you verify greedily that no cheaper spanning tree exists: a cheaper tree would need at least one edge replaced by one with lower weight, but every such swap would violate the cut property.

## Files

- [`starter/shell-inspecting-the-mst-edge-list.py`](starter/shell-inspecting-the-mst-edge-list.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l05/m06l05-05/starter`
2. Read `shell-inspecting-the-mst-edge-list.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   edges = [(1,'A','B'), (2,'B','C'), (4,'B','D')]
   sorted(edges)
   sum(w for w,_,_ in edges)
   len(edges)
   ```
4. Run it: `python3 -i < shell-inspecting-the-mst-edge-list.py`.
5. Check it from the repository root: `./check m06l05-05`.

## Expected output

```text
[(1, 'A', 'B'), (2, 'B', 'C'), (4, 'B', 'D')]
7
3
```

## How to check

`./check m06l05-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-inspecting-the-mst-edge-list.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
