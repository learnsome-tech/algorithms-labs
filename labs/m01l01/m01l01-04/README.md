# m01l01-04 · Asking whether something is in a list or a dict

**Lesson:** [Why Complexity Matters In Production](https://learnsome.tech/learn/algorithms-course/m01l01) (lesson 1.1, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can explain why scanning a list grows linearly with input size while a dictionary lookup stays constant, measure both with the perf counter timer, and describe what input size n means in a complexity argument.

In the lesson: The shell makes it easy to see that both containers answer membership questions, and to appreciate that the speed difference is invisible at small sizes. Three names go into a list in order, and the same three into a dict with numeric values. Asking whether alice is in each one returns True either way, because the containers hold the same data. The difference is how they find the answer: the list checks each element from the start, the dict computes the hash and jumps. Asking for zara returns False from both; again the answer is right either way. At three elements, neither approach is slow enough to notice. The lesson from timing is that the gap only becomes costly at scale, which is why we need a notation for growth rather than raw time.

## Files

- [`starter/shell-asking-whether-something-is-in-a-list-or-a-d.py`](starter/shell-asking-whether-something-is-in-a-list-or-a-d.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-04/starter`
2. Read `shell-asking-whether-something-is-in-a-list-or-a-d.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   users_list = ['alice', 'bob', 'carol']
   users_dict = {'alice': 1, 'bob': 2, 'carol': 3}
   'alice' in users_list
   'alice' in users_dict
   'zara' in users_list
   'zara' in users_dict
   ```
4. Run it: `python3 -i < shell-asking-whether-something-is-in-a-list-or-a-d.py`.
5. Check it from the repository root: `./check m01l01-04`.

## Expected output

```text
True
True
False
False
```

## How to check

`./check m01l01-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-asking-whether-something-is-in-a-list-or-a-d.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
