# m03l03-02 · Stack operations on a Python list

**Lesson:** [Stacks And Queues: Last In Or First In](https://learnsome.tech/learn/algorithms-course/m03l03) (lesson 3.3, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Graded

## Goal

You can implement a stack using a Python list and a queue using a deque, explain the ordering discipline of each, use a stack to check balanced brackets, and measure why list.pop(0) is a poor queue implementation.

In the lesson: Python lists work as stacks straight away: append pushes to the top and pop removes from the top, both in constant amortised time. Push a string called a onto an empty stack. The list representation shows a at position zero. Push b, then push c. Evaluating the full list shows the stack state from bottom to top: a at the back, c on top. Pop the top and Python returns the string c and removes it from the list, leaving a and b. The list keeps the newest element at the back, which is where both append and pop without an argument operate. The discipline is consistent: when using a list as a stack, you never touch index zero. That constraint is what makes it a stack rather than an unordered bag.

## Files

- [`starter/shell-stack-operations-on-a-python-list.py`](starter/shell-stack-operations-on-a-python-list.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-02/starter`
2. Read `shell-stack-operations-on-a-python-list.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   stack = []
   stack.append('a')
   stack
   stack.append('b')
   stack.append('c')
   stack
   stack.pop()
   stack
   ```
4. Run it: `python3 -i < shell-stack-operations-on-a-python-list.py`.
5. Check it from the repository root: `./check m03l03-02`.

## Expected output

```text
['a']
['a', 'b', 'c']
'c'
['a', 'b']
```

## How to check

`./check m03l03-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-stack-operations-on-a-python-list.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
