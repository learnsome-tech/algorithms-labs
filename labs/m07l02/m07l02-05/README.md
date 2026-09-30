# m07l02-05 · Huffman coding: greedy by frequency

**Lesson:** [Greedy Algorithms: When Local Is Global](https://learnsome.tech/learn/algorithms-course/m07l02) (lesson 7.2, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can implement interval scheduling by earliest finish, explain why greedy coin change fails on some coin systems by comparing with the dynamic-programming optimum, and build a Huffman code using a priority queue.

In the lesson: Huffman coding assigns shorter bit strings to more frequent symbols. The greedy rule is always to merge the two lightest nodes in a priority queue into a combined node whose weight is their sum. Repeat until one node remains: that is the code tree.

The heap here holds five-tuples with the weight first so the smallest weight rises to the top. Merging the two lightest nodes is exactly the greedy choice: any alternative merge produces a code where at least one frequent symbol is assigned more bits than necessary. An exchange argument proves the greedy merge is optimal.

After building the tree, measuring depths by recursing from the root reveals how many bits each symbol needs. Printing each symbol alongside its code length confirms the pattern: the most frequent symbol needs only one bit, while the rarest two need four.

## Files

- [`starter/huffman.py`](starter/huffman.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l02/m07l02-05/starter`
2. Read `huffman.py` the way the lesson builds it:
   - Lines 1–13: merging the two lightest
   - Lines 14–19: measuring depths
   - Lines 20–22: printing each symbol
3. Run it: `python3 huffman.py`.
4. Check it from the repository root: `./check m07l02-05`.

## Expected output

```text
a 1
b 3
c 3
d 3
e 4
f 4
```

## How to check

`./check m07l02-05` copies `starter/` into a scratch directory and runs `python3 huffman.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
