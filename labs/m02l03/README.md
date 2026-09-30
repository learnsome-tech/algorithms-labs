# m02l03 · Python Dicts And Sets Under The Hood

Module 2: Hashing: Structure Behind Everything Fast · lesson 2.3 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m02l03)

**Goal:** You can explain how Python dicts preserve insertion order, why set membership beats list membership in cost, how to implement a hashable class correctly, and what the hash-equals contract requires.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l03-02](m02l03-02/) | Insertion order and membership cost in practice | Graded |
| [m02l03-03](m02l03-03/) | Trying to hash a list raises TypeError | Graded |
| [m02l03-04](m02l03-04/) | Implementing the hash-equals contract on a class | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Build and test a hashable value type

1. Write a Fraction class with numerator and denominator, reduced to lowest terms.
2. Implement __eq__ and __hash__ so that Fraction(one, two) equals Fraction(two, four).
3. Verify that two equal fractions can be used interchangeably as dict keys.

> **Hint:** Reduce to lowest terms in __init__ using math.gcd so that equal fractions always have identical numerators and denominators. Then hash and compare those stored values.

## Check yourself

- Why does checking membership in a set cost order one while checking a list costs order n?
- Why does Python raise TypeError when you try to hash a list but not a tuple?
- What are the two parts of the hash-equals contract, and what breaks when either part is violated?
- What happens in Python if you define __eq__ on a class but do not define __hash__?
- In the Point demo, why does looking up p2 in a dict that stored p1 succeed?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
