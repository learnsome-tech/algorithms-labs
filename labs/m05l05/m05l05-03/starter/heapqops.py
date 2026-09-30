import heapq

scores = [42, 17, 88, 5, 63, 31]
heapq.heapify(scores)
print('heapified:', scores)
heapq.heappush(scores, 50)
print('after push:', scores)
print('popped:', heapq.heappop(scores))
print('heap now:', scores)
print('three largest:', heapq.nlargest(3, scores))
