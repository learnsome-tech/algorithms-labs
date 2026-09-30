# m06l01-02 · Adjacency list: a dictionary of neighbour lists

**Lesson:** [Representing A Graph: Matrix Or Adjacency List](https://learnsome.tech/learn/algorithms-course/m06l01) (lesson 6.1, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can represent a graph as either an adjacency list or a two-dimensional matrix, state the memory cost of each, explain when to prefer one over the other, and encode directed and weighted edges.

In the lesson: The adjacency list stores each vertex as a key in a dictionary, and the value is the list of vertices it connects to. This graph has five vertices and five undirected edges. Because the edges are undirected, each one appears in two lists: A's list contains B, and B's list contains A. That doubling is why the edge count on the last line divides by two after summing all the list lengths. When we print each vertex's neighbour list, the output shows the graph's structure immediately. Querying a vertex's neighbours is fast: it reads one list. Asking whether a specific edge exists requires a linear scan of that list, which is acceptable for sparse graphs where each vertex has few neighbours.

## Files

- [`starter/adj_list.py`](starter/adj_list.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-02/starter`
2. Read `adj_list.py` the way the lesson builds it:
   - Lines 1–6: adjacency list
   - Lines 7–13: edge count
3. Run it: `python3 adj_list.py`.
4. Check it from the repository root: `./check m06l01-02`.

## Expected output

```text
A -> ['B', 'C']
B -> ['A', 'D', 'E']
C -> ['A', 'D']
D -> ['B', 'C']
E -> ['B']
edges: 5
```

## How to check

`./check m06l01-02` copies `starter/` into a scratch directory and runs `python3 adj_list.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
