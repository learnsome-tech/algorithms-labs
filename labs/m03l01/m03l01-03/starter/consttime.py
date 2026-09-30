import time
data=list(range(100000))
n=50000
t0=time.perf_counter()
for _ in range(n): x=data[0]
t_front=time.perf_counter()-t0
t0=time.perf_counter()
for _ in range(n): x=data[99999]
t_back=time.perf_counter()-t0
ratio=t_back/t_front
print('constant-time access confirmed:', 0.5<ratio<2.0)
