# m05l05-05 · Task scheduler: priority queue in action

**Lesson:** [Heaps And Priority Queues](https://learnsome.tech/learn/algorithms-course/m05l05) (lesson 5.5, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can build an array-backed min-heap with sift-up and sift-down, use the heapq module for push, pop, heapify, and nlargest, implement heap sort, and model a priority queue as a task scheduler.

In the lesson: Priority queues model any problem where items have different urgency. The heapq module turns a list into a priority queue directly: push tuples where the first element is the priority number and heapq keeps the lowest number at the front. Python's tuple comparison handles ties by comparing the second element, so two tasks with equal priority come out alphabetically by name. Push four incident tasks with different urgencies: opening the incident channel and paging the on-call engineer are both priority one, notifying the team is priority two, and deploying the database is priority three. Pull tasks from the queue in priority order, and each heappop returns the most urgent item first. The two priority-one tasks emerge in alphabetical order because of tuple comparison, then priority two, then priority three, exactly as an incident response should proceed.

## Files

- [`starter/scheduler.py`](starter/scheduler.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l05/m05l05-05/starter`
2. Read `scheduler.py` the way the lesson builds it:
   - Lines 1–7: four incident tasks
   - Lines 8–12: pull tasks
3. Run it: `python3 scheduler.py`.
4. Check it from the repository root: `./check m05l05-05`.

## Expected output

```text
processing in priority order:
 priority 1 : open incident channel
 priority 1 : page on-call engineer
 priority 2 : notify team
 priority 3 : deploy database
```

## How to check

`./check m05l05-05` copies `starter/` into a scratch directory and runs `python3 scheduler.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
