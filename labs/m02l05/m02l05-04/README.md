# m02l05-04 · Larger bit arrays produce fewer false positives

**Lesson:** [Bloom Filters: Membership Without The Data](https://learnsome.tech/learn/algorithms-course/m02l05) (lesson 2.5, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can implement a Bloom filter using k hash functions derived from SHA two-fifty-six, measure its false-positive rate on a fixed word list, and explain why Bloom filters guarantee zero false negatives.

In the lesson: Run the same experiment at three different bit array sizes with the same twenty insertions and one hundred probes. The three rows of output tell the story clearly. At sixty-four bits the filter is cramped: twenty-six out of one hundred non-members appear as false positives, which is far too high for production use. Doubling to one hundred and twenty-eight bits drops the rate to five percent: acceptable for many pre-filter applications. At five hundred and twelve bits - eight times the smallest size - zero false positives appear in the test set. The underlying item count has not changed, so the improvement comes entirely from having more bits to distribute the k hash positions across, reducing the chance that all three bits for a non-member happen to be already set by previously inserted items.

## Files

- [`starter/bloom_compare.py`](starter/bloom_compare.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-04/starter`
2. Read `bloom_compare.py` the way the lesson builds it:
   - Lines 1–13: three different bit array sizes
   - Lines 14–18: twenty insertions
3. Run it: `python3 bloom_compare.py`.
4. Check it from the repository root: `./check m02l05-04`.

## Expected output

```text
m=64: 26 false positives per hundred
m=128: 5 false positives per hundred
m=512: 0 false positives per hundred
```

## How to check

`./check m02l05-04` copies `starter/` into a scratch directory and runs `python3 bloom_compare.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
