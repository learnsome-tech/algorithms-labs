import bisect, time
n = 100000
data = list(range(n))
data_set = set(data)
target = n - 1
def time_it(fn, reps=2000):
    t0 = time.perf_counter()
    for _ in range(reps): fn()
    return time.perf_counter() - t0
def in_set():    return target in data_set
def in_bisect():
    i = bisect.bisect_left(data, target)
    return i < len(data) and data[i] == target
def in_list():   return target in data
t_set    = time_it(in_set)
t_bisect = time_it(in_bisect)
t_list   = time_it(in_list, 20)
print('set faster than linear:', t_set < t_list)
print('bisect faster than linear:', t_bisect < t_list)
