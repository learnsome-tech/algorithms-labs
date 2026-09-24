# Exercises — Backtracking: Search With Pruning

Lesson `m07l03` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m07l03)

## Exercise 1: Practice: backtracking and pruning

1. Change N-queens to stop at the first solution found and verify it returns for n equal to twelve.
2. Add a lower-bound pruning rule: abandon when remaining items cannot reach the target.
3. Use the permutations generator to show all arrangements of three letters that start with 'a'.

> **Hint**: For the second task, precompute the suffix sums before the recursion starts: at position i the remaining sum available is the sum of all elements from i to the end. If cur plus that remaining sum is less than target, the branch can be pruned.


---

© LearnSome.tech · support@iwantto.learnsome.tech
