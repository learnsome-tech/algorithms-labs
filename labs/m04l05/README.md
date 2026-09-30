# m04l05 · Searching With Hashes Versus Trees

Module 4: Sorting And Searching · lesson 4.5 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m04l05)

**Goal:** You can choose between a set, a sorted list with bisect, and a linear scan for membership and range queries, and explain when sorted order provides capabilities that hashing cannot.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l05-02](m04l05-02/) | Membership speed: set, bisect, and linear scan | Graded |
| [m04l05-03](m04l05-03/) | Range queries: where sorted order wins | Graded |
| [m04l05-04](m04l05-04/) | Bisect as a sorted-list interface | Graded |
| [m04l05-05](m04l05-05/) | Summary table: operations across three structures | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Choose and justify a structure for each scenario

1. Which structure handles one million IP addresses with frequent membership queries, and why?
2. Maintain a sorted leaderboard and retrieve the top ten scores after each insert using bisect.
3. Count events between two timestamps in a sorted list using bisect; write the solution.

> **Hint:** For the leaderboard, insort maintains sorted order on every insert; slicing the last ten elements from a sorted ascending list gives the top ten in constant time.

## Check yourself

- Why can a hash set not answer a range query efficiently, while a sorted list can?
- What is the time complexity of bisect-left and why?
- Give a concrete scenario where you would prefer a sorted list over a set.
- What is the cost of iterating over all elements in sorted order from a set versus a sorted list?
- What would you use if you needed both constant-time membership and log n range queries?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
