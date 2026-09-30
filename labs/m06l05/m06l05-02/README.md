# m06l05-02 · Union-find: path compression and union by rank

**Lesson:** [Minimum Spanning Trees: Kruskal And Prim](https://learnsome.tech/learn/algorithms-course/m06l05) (lesson 6.5, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement union-find with path compression and union by rank, run Kruskal's algorithm to build a minimum spanning tree edge by edge, and run Prim's algorithm from a starting vertex using a heap.

In the lesson: Union-find answers one question efficiently: are two elements in the same component? The parent array starts with every element pointing to itself. The find operation follows the parent chain upward to reach the root. Path compression rewires each visited node to point directly to the root on the way back, flattening the tree so future finds are nearly instant. Union by rank attaches the shallower tree under the taller one, keeping the tree height small. Together, these two optimisations give an amortised cost so close to constant that it is written as the inverse Ackermann function, which is effectively a fixed cost for any practical input size. After three union calls that merge all four nodes into one component, every call to find returns the same root, which is zero. Kruskal's algorithm uses union-find to detect whether an edge would create a cycle: if both endpoints share a root, adding the edge would close a loop.

## Files

- [`starter/union_find.py`](starter/union_find.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l05/m06l05-02/starter`
2. Read `union_find.py` the way the lesson builds it:
   - Lines 1–8: path compression
   - Lines 9–18: union by rank
   - Lines 19–22: same root
3. Run it: `python3 union_find.py`.
4. Check it from the repository root: `./check m06l05-02`.

## Expected output

```text
[0, 0, 0, 0]
```

## How to check

`./check m06l05-02` copies `starter/` into a scratch directory and runs `python3 union_find.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
