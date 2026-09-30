import sys

data = list(range(8))
left, right = 0, len(data) - 1
while left < right:
    data[left], data[right] = data[right], data[left]
    left += 1
    right -= 1
print('reversed in place:', data)

n = 10000
lst = list(range(n))
before = sys.getsizeof(lst)
lst.reverse()
after = sys.getsizeof(lst)
print('size before:', before)
print('size after:', after)
print('same size:', before == after)
