import heapq

tasks = []
heapq.heappush(tasks, (3, 'deploy database'))
heapq.heappush(tasks, (1, 'page on-call engineer'))
heapq.heappush(tasks, (2, 'notify team'))
heapq.heappush(tasks, (1, 'open incident channel'))

print('processing in priority order:')
while tasks:
    pri, name = heapq.heappop(tasks)
    print(' priority', pri, ':', name)
