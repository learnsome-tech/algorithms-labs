# m03l04 · Deques And Ring Buffers

Module 3: Sequences: Arrays, Lists, Stacks And Queues · lesson 3.4 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m03l04)

**Goal:** You can use a deque with maxlen as a sliding window, implement a ring buffer with head and tail indices and modulo wraparound, and compute a moving average over a data stream using the ring buffer.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l04-02](m03l04-02/) | Sliding window with deque maxlen | Graded |
| [m03l04-03](m03l04-03/) | Maximum value in each sliding window | Graded |
| [m03l04-05](m03l04-05/) | A ring buffer with head and tail indices | Graded |
| [m03l04-06](m03l04-06/) | Moving average over a live stream | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Sliding windows and ring buffers

1. Adapt the sliding window to compute a minimum and print it alongside the maximum per position.
2. Add peek_oldest and is_full to RingBuffer; peek_oldest reads the head value without removing it.
3. Use a maxlen-five deque to stream integers one at a time, printing the running mean after each.

> **Hint:** For peek_oldest on an empty buffer return None; for streaming mean, sum the deque and divide by its current length after each append.

## Check yourself

- What does the maxlen parameter of a deque do when a new item arrives and the deque is already at capacity?
- What two indices does a ring buffer maintain, and how does modulo arithmetic prevent them from going out of bounds?
- Why is middle-index access on a deque slower than on a list of the same length?
- In the moving-average program, what happens to the oldest measurement when a new one arrives and the buffer is full?
- When should you write a hand-rolled ring buffer instead of using a deque with maxlen?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
