# m03l01-02 · Measuring storage with array and list

**Lesson:** [Arrays: Contiguous Memory And Constant-Time Access](https://learnsome.tech/learn/algorithms-course/m03l01) (lesson 3.1, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can explain why array index access is constant time, measure the memory difference between a typed array and a list, predict the cost of front insertion versus appending, and describe why slicing produces a copy.

In the lesson: The standard library ships a module called array that gives you typed sequences where every slot holds a value in its raw binary form rather than as a Python object. The typecode i stands for a signed integer stored in four bytes. Create one from a hundred integers and build an equivalent Python list from the same values. When you measure both with getsizeof, you see the array uses roughly four hundred bytes plus overhead while the list stores a pointer per element rather than the value itself: pointers on a sixty-four-bit system are eight bytes each, so the list takes almost twice as much space. Ask whether the array is smaller and Python confirms the comparison with a boolean. The difference comes from the representation, not from any overhead in the object structure.

## Files

- [`starter/shell-measuring-storage-with-array-and-list.py`](starter/shell-measuring-storage-with-array-and-list.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-02/starter`
2. Read `shell-measuring-storage-with-array-and-list.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   import array, sys
   a = array.array('i', range(100))
   sys.getsizeof(a)
   b = list(range(100))
   sys.getsizeof(b)
   sys.getsizeof(a) < sys.getsizeof(b)
   ```
4. Run it: `python3 -i < shell-measuring-storage-with-array-and-list.py`.
5. Check it from the repository root: `./check m03l01-02`.

## Expected output

```text
488
856
True
```

## How to check

`./check m03l01-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-measuring-storage-with-array-and-list.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
