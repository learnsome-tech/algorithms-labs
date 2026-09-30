# m03l02-03 · Deletion and linear search

**Lesson:** [Linked Lists: Nodes, Pointers And Sentinels](https://learnsome.tech/learn/algorithms-course/m03l02) (lesson 3.2, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can implement a singly linked list with push-front, append, delete, and find; explain why a sentinel head eliminates edge cases; and identify workloads where a linked list outperforms a Python list.

In the lesson: The second program separates the operations into standalone functions to keep the pointer logic visible without class scaffolding. The push function creates a new node, points its next at the current head, and returns the new head. Delete walks the list looking for a node whose next field holds the target value; when found, it wires the current node's next over the target and stops. Find uses a short-circuit loop to advance while the current value does not match, then returns whether the current pointer is not none. Building the list by pushing thirty, then twenty, then ten produces ten, twenty, thirty in order. Deleting twenty links ten directly to thirty. The final print shows true and false for the two find calls, confirming ten is present and twenty is gone.

## Files

- [`starter/sll_ops.py`](starter/sll_ops.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-03/starter`
2. Read `sll_ops.py` the way the lesson builds it:
   - Lines 1–11: Delete walks the list
   - Lines 12–22: shows true and false
3. Run it: `python3 sll_ops.py`.
4. Check it from the repository root: `./check m03l02-03`.

## Expected output

```text
10 -> 20 -> 30
10 -> 30
True False
```

## How to check

`./check m03l02-03` copies `starter/` into a scratch directory and runs `python3 sll_ops.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
