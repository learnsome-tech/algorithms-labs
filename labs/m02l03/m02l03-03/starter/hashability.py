try:
    hash([1, 2, 3])
except TypeError as e:
    print(e)
print('tuple is hashable:', hash((1, 2, 3)) == hash((1, 2, 3)))
