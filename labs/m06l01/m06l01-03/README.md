# m06l01-03 · Adjacency matrix: a two-dimensional grid

**Lesson:** [Representing A Graph: Matrix Or Adjacency List](https://learnsome.tech/learn/algorithms-course/m06l01) (lesson 6.1, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can represent a graph as either an adjacency list or a two-dimensional matrix, state the memory cost of each, explain when to prefer one over the other, and encode directed and weighted edges.

In the lesson: The adjacency matrix stores the same five-vertex graph as a five-by-five grid of zeros and ones. The index dictionary maps each vertex name to its row and column number. Setting a cell to one for both directions captures the undirected edge. The adjacency matrix shines at the neighbour query: to find all neighbours of A, scan its row and collect the positions where the value is one. That scan is always proportional to V, the vertex count, regardless of how many neighbours the vertex actually has. The bottom line prints the total number of cells in the matrix, which is twenty-five; that number grows as V squared, while the adjacency list grows as V plus twice E.

## Files

- [`starter/adj_matrix.py`](starter/adj_matrix.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-03/starter`
2. Read `adj_matrix.py` the way the lesson builds it:
   - Lines 1–7: adjacency matrix
   - Lines 8–11: neighbour query
3. Run it: `python3 adj_matrix.py`.
4. Check it from the repository root: `./check m06l01-03`.

## Expected output

```text
A neighbours: ['B', 'C']
B neighbours: ['A', 'D', 'E']
matrix cells: 25
```

## How to check

`./check m06l01-03` copies `starter/` into a scratch directory and runs `python3 adj_matrix.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
