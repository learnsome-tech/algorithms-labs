# Exercises — Python Dicts And Sets Under The Hood

Lesson `m02l03` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m02l03)

## Exercise 1: Build and test a hashable value type

1. Write a Fraction class with numerator and denominator, reduced to lowest terms.
2. Implement __eq__ and __hash__ so that Fraction(one, two) equals Fraction(two, four).
3. Verify that two equal fractions can be used interchangeably as dict keys.

> **Hint**: Reduce to lowest terms in __init__ using math.gcd so that equal fractions always have identical numerators and denominators. Then hash and compare those stored values.


---

© LearnSome.tech · support@iwantto.learnsome.tech
