def linear_search(data, target):
    comparisons = 0
    for item in data:
        comparisons += 1
        if item == target:
            return comparisons
    return comparisons

n = 1000
data = list(range(n))

found_first = linear_search(data, 0)
found_last = linear_search(data, n - 1)
not_found = linear_search(data, -1)

print('best case (found first):', found_first)
print('worst case (found last):', found_last)
print('missing item:', not_found)
print('worst equals n:', not_found == n)
