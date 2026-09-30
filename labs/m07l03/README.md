# m07l03 · Backtracking: Search With Pruning

Module 7: Problem-Solving Techniques · lesson 7.3 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m07l03)

**Goal:** You can implement backtracking with pruning, count solutions for N-queens and compare solution counts across board sizes, measure how much pruning reduces the nodes visited versus exhaustive search, and generate permutations with a recursive generator.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m07l03-02](m07l03-02/) | N-queens: count solutions and find one example | Graded |
| [m07l03-03](m07l03-03/) | Subset sum: how pruning cuts the search tree | Graded |
| [m07l03-04](m07l03-04/) | Generating all permutations with a recursive generator | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Practice: backtracking and pruning

1. Change N-queens to stop at the first solution found and verify it returns for n equal to twelve.
2. Add a lower-bound pruning rule: abandon when remaining items cannot reach the target.
3. Use the permutations generator to show all arrangements of three letters that start with 'a'.

> **Hint:** For the second task, precompute the suffix sums before the recursion starts: at position i the remaining sum available is the sum of all elements from i to the end. If cur plus that remaining sum is less than target, the branch can be pruned.

## Check yourself

- What are the three conditions checked at each queen placement in the N-queens algorithm, and why can each be tested in constant time?
- How does the subset-sum pruning condition know when to abandon a branch, and what makes it correct to do so for lists of positive numbers?
- For a list of four items, the permutation generator produces twenty-four results. What determines that count, and why does the recursive structure guarantee no duplicates?
- In the pruning comparison, why does the unpruned subset-sum visit sixty-three nodes for a five-element list, and how does that relate to the tree structure?
- What is the difference between backtracking that finds one solution and backtracking that counts all solutions, in terms of when the recursion returns?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
