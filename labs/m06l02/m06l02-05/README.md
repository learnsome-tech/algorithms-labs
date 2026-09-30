# m06l02-05 · Level-order layers from the same BFS

**Lesson:** [Breadth-First Search And Shortest Paths By Hops](https://learnsome.tech/learn/algorithms-course/m06l02) (lesson 6.2, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement BFS with a deque to compute shortest hop distances and reconstruct paths, explain why BFS finds shortest paths in unweighted graphs, and use BFS to compute degrees of separation.

In the lesson: BFS traversal naturally groups vertices by their distance from the source. After the search, grouping the distance map by value produces layers, where each layer holds every vertex at exactly the same hop count from the source. Layer zero contains only Alice. Layer one contains Bob and Carol, who are direct neighbours. Layer two contains Dave, who requires one intermediate friend. In a real network these layers answer the degrees-of-separation question concretely: every person in layer two is two degrees from Alice. The same layered structure appears in tree algorithms under the name level-order traversal. The maximum layer index is the eccentricity of the source vertex in the graph: the furthest any other vertex is from Alice, measured in hops, is two.

## Files

- [`starter/bfs_layers.py`](starter/bfs_layers.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-05/starter`
2. Read `bfs_layers.py` the way the lesson builds it:
   - Lines 1–12: BFS traversal
   - Lines 13–18: layer zero
3. Run it: `python3 bfs_layers.py`.
4. Check it from the repository root: `./check m06l02-05`.

## Expected output

```text
layer 0 : ['Alice']
layer 1 : ['Bob', 'Carol']
layer 2 : ['Dave']
```

## How to check

`./check m06l02-05` copies `starter/` into a scratch directory and runs `python3 bfs_layers.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
