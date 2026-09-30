# m04l04-02 · key=, reverse=, and operator.itemgetter

**Lesson:** [Sorting In Real Systems: Stability, Keys And External Sort](https://learnsome.tech/learn/algorithms-course/m04l04) (lesson 4.4, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can sort with key functions and tuple keys, compose sorts by chaining stable passes, and implement a k-way external merge using heapq.merge over temporary files.

In the lesson: The key argument takes any callable, including the built-in len, a lambda, or a function from the operator module. Sorting the word list by character count gives a sort by character count, putting the shortest word first. Adding reverse equals true inverts the order without changing what the key computes. The operator dot itemgetter function returns a callable that pulls a specific index from each element; itemgetter of one extracts the score field, and the sort puts the two eighty-five scores before ninety because eighty-five is smaller. Stability is visible in the result: alice and carol both have score eighty-five, and alice appears first in the input, so alice appears first in the output. Switching to itemgetter of zero sorts by name, alphabetically. The operator module is preferred over lambdas for extracting fields because it is faster and serializable across process boundaries.

## Files

- [`starter/shell-key-reverse-and-operator-itemgetter.py`](starter/shell-key-reverse-and-operator-itemgetter.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-02/starter`
2. Read `shell-key-reverse-and-operator-itemgetter.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   words = ['banana', 'fig', 'apple', 'cherry']
   sorted(words, key=len)
   sorted(words, key=len, reverse=True)
   import operator
   data = [('alice', 85), ('bob', 90), ('carol', 85)]
   sorted(data, key=operator.itemgetter(1))
   sorted(data, key=operator.itemgetter(0))
   ```
4. Run it: `python3 -i < shell-key-reverse-and-operator-itemgetter.py`.
5. Check it from the repository root: `./check m04l04-02`.

## Expected output

```text
['fig', 'apple', 'banana', 'cherry']
['banana', 'cherry', 'apple', 'fig']
[('alice', 85), ('carol', 85), ('bob', 90)]
[('alice', 85), ('bob', 90), ('carol', 85)]
```

## How to check

`./check m04l04-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-key-reverse-and-operator-itemgetter.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
