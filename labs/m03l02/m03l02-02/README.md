# m03l02-02 · Building a singly linked list

**Lesson:** [Linked Lists: Nodes, Pointers And Sentinels](https://learnsome.tech/learn/algorithms-course/m03l02) (lesson 3.2, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can implement a singly linked list with push-front, append, delete, and find; explain why a sentinel head eliminates edge cases; and identify workloads where a linked list outperforms a Python list.

In the lesson: This program defines two classes. The Node class holds a value and a next pointer set to none on construction. The list class wraps a head pointer and exposes two ways to add elements: push front prepends a new node by pointing its next at the current head and then updating head to the new node; append walks to the tail and attaches the new node there. The show method traverses the chain, collecting each value into a list of strings and joining them with arrows for display. After appending ten, twenty, and thirty in order, push front with five inserts a node before ten. The printed chain reads five, ten, twenty, thirty from left to right, which is the physical order of the pointers.

## Files

- [`starter/sll_build.py`](starter/sll_build.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-02/starter`
2. Read `sll_build.py` the way the lesson builds it:
   - Lines 1–2: Node class holds a value
   - Lines 3–16: show method traverses
   - Lines 17–22: five, ten, twenty, thirty
3. Run it: `python3 sll_build.py`.
4. Check it from the repository root: `./check m03l02-02`.

## Expected output

```text
5 -> 10 -> 20 -> 30
```

## How to check

`./check m03l02-02` copies `starter/` into a scratch directory and runs `python3 sll_build.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
