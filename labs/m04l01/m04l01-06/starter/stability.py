records = [(3,'b'), (1,'x'), (3,'a'), (1,'y'), (2,'c')]

def ins_stable(arr, key):
    arr = arr[:]
    for i in range(1, len(arr)):
        tmp = arr[i]; j = i - 1
        while j >= 0 and key(arr[j]) > key(tmp):
            arr[j+1] = arr[j]; j -= 1
        arr[j+1] = tmp
    return arr

by_first = ins_stable(records, lambda r: r[0])
print('insertion sort:', by_first)
builtin = sorted(records, key=lambda r: r[0])
print('sorted() builtin:', builtin)
print('order matches:', by_first == builtin)
