# m06l02-04 · Path reconstruction using the parent map

**Lesson:** [Breadth-First Search And Shortest Paths By Hops](https://learnsome.tech/learn/algorithms-course/m06l02) (lesson 6.2, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement BFS with a deque to compute shortest hop distances and reconstruct paths, explain why BFS finds shortest paths in unweighted graphs, and use BFS to compute degrees of separation.

In the lesson: Path reconstruction adds only a parent map to BFS. Instead of recording distance, the compact graph search records who discovered each vertex: when BFS discovers a new vertex, it stores the vertex that enqueued it as its parent. The source maps to None because it has no predecessor. The search stops as soon as the destination is dequeued. Backtracking from the destination by following parent pointers builds the path in reverse; reversing the accumulated list gives the correct forward order. The output confirms the shortest path to Dave runs Alice, Bob, Dave, covering two edges. A path through Carol would also use two edges, but the algorithm finds one valid shortest path and stops. The pattern - record parent on discovery, follow pointers, reverse - applies to any BFS that needs to produce a route.

## Files

- [`starter/bfs_path.py`](starter/bfs_path.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-04/starter`
2. Read `bfs_path.py` the way the lesson builds it:
   - Lines 1–3: compact graph
   - Lines 4–14: parent map
   - Lines 15–20: shortest path to Dave
3. Run it: `python3 bfs_path.py`.
4. Check it from the repository root: `./check m06l02-04`.

## Expected output

```text
['Alice', 'Bob', 'Dave']
```

## How to check

`./check m06l02-04` copies `starter/` into a scratch directory and runs `python3 bfs_path.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
