# m02l04-03 · Anagram keys all land in the same weak-hash bucket

**Lesson:** [Collisions In Practice And Hash Flooding](https://learnsome.tech/learn/algorithms-course/m02l04) (lesson 2.4, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can demonstrate how a constant-return hash degrades lookup to linear time, show how anagram-based keys exploit a sum hash, and explain how per-process hash randomisation defends against flooding attacks.

In the lesson: Here is the simplest exploitable hash function: sum the numeric codes of all characters and take the remainder. Any two strings that are anagrams of each other have the same character sum, so they always land in the same slot. The polynomial slot function multiplies the running total by thirty-one at each step, which breaks the symmetry. Feed five words that are all anagrams of the same letters - star, arts, tars, rats, and tsar - into the table below. The weak hash sends all five to slot ten: one distinct slot, five words, instant chain of length five. The polynomial hash spreads them across three distinct slots, which is still imperfect but already far better. An adversary with a dictionary can generate hundreds of anagram groups and flood a server using only the sum-hash vulnerability - that is why sum hashing appears in no serious production code.

## Files

- [`starter/collision.py`](starter/collision.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-03/starter`
2. Read `collision.py` the way the lesson builds it:
   - Lines 1–2: sum the numeric codes
   - Lines 3–8: polynomial slot
   - Lines 9–18: Feed five words
3. Run it: `python3 collision.py`.
4. Check it from the repository root: `./check m02l04-03`.

## Expected output

```text
words: ['star', 'arts', 'tars', 'rats', 'tsar']
weak slots (sum of codes): [10, 10, 10, 10, 10]
distinct weak slots: 1
poly slots (base-31): [2, 0, 14, 14, 0]
distinct poly slots: 3
```

## How to check

`./check m02l04-03` copies `starter/` into a scratch directory and runs `python3 collision.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
