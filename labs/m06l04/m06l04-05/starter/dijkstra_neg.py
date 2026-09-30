import heapq
G = {'s': [('v',10),('u',1)], 'u': [('t',2)],
     'v': [('t',-8)], 't': []}
def dijkstra_bad(G, src):
    dist = {src: 0}
    done = set()
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if u in done:
            continue
        done.add(u)
        for v, w in G[u]:
            if v not in done:
                nd = d + w
                if nd < dist.get(v, float('inf')):
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
    return dist
print(dijkstra_bad(G, 's'))
print('correct dist to t:', 10 + -8)
