# m07l02 · Greedy Algorithms: When Local Is Global

Module 7: Problem-Solving Techniques · lesson 7.2 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m07l02)

**Goal:** You can implement interval scheduling by earliest finish, explain why greedy coin change fails on some coin systems by comparing with the dynamic-programming optimum, and build a Huffman code using a priority queue.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m07l02-02](m07l02-02/) | Interval scheduling: always pick the earliest finish | Graded |
| [m07l02-03](m07l02-03/) | Coin change: greedy works for standard coins | Graded |
| [m07l02-04](m07l02-04/) | Coin change: greedy fails on arbitrary denominations | Graded |
| [m07l02-05](m07l02-05/) | Huffman coding: greedy by frequency | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Practice: scheduling and coin systems

1. Modify the interval scheduler to also return the index of each chosen interval.
2. Show that coins one, six, and ten give a greedy failure at amount twelve and verify with DP.
3. Change the Huffman function to return bit strings instead of code lengths and print them.

> **Hint:** For the coin counterexample, think about what happens when greedy picks the ten first. For Huffman codes, track the bit string built during the merge steps: append a zero when you go left and a one when you go right.

## Check yourself

- What is the greedy-choice property, and what proof technique is used to show that a greedy algorithm is optimal?
- Why does sorting by earliest finish time produce the maximum number of non-overlapping intervals?
- Give a coin system and an amount where greedy gives a worse answer than the optimal, and explain why greedy fails there.
- In Huffman coding, what is the greedy rule at each step, and why does merging the two lightest nodes never hurt?
- When should you use dynamic programming instead of greedy, and what is the key structural difference between the two?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
