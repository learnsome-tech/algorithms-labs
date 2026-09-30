# m06l02-03 · BFS distance map on a social graph

**Lesson:** [Breadth-First Search And Shortest Paths By Hops](https://learnsome.tech/learn/algorithms-course/m06l02) (lesson 6.2, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement BFS with a deque to compute shortest hop distances and reconstruct paths, explain why BFS finds shortest paths in unweighted graphs, and use BFS to compute degrees of separation.

In the lesson: The social graph connects four people. Alice knows Bob and Carol; Dave is friends with both Bob and Carol but not directly with Alice. The bfs function places the source into the deque from the source with distance zero. Each iteration pops the front vertex, then loops over its neighbours. Any neighbour absent from the distance map receives a distance one greater than the current vertex and is pushed to the back. The output displays the hop count from Alice: Bob and Carol are one hop away because they are her direct friends, and Dave is two hops away because reaching him requires one intermediate step. The search cannot improve these distances later because BFS always processes shorter paths first - that is why checking whether the vertex is already in the map is enough.

## Files

- [`starter/bfs_dist.py`](starter/bfs_dist.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-03/starter`
2. Read `bfs_dist.py` the way the lesson builds it:
   - Lines 1–8: social graph
   - Lines 9–19: deque from the source
   - Lines 20–22: hop count
3. Run it: `python3 bfs_dist.py`.
4. Check it from the repository root: `./check m06l02-03`.

## Expected output

```text
Alice distance 0
Bob distance 1
Carol distance 1
Dave distance 2
```

## How to check

`./check m06l02-03` copies `starter/` into a scratch directory and runs `python3 bfs_dist.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
