# 이중 우선순위 큐

import heapq

t = int(input())
result = []
for _ in range(t):
    visited = [False] * 1_000_001
    minH, maxH = [], []

    for i in range(int(input())):
        order, num = input().split()
        if order == 'I':
            heapq.heappush(minH, (int(num), i))
            heapq.heappush(maxH, (-int(num), i))
            visited[i] = True
        elif num == '1':
            while maxH and not visited[maxH[0][1]]:
                heapq.heappop(maxH)
            if maxH:
                visited[maxH[0][1]] = False
                heapq.heappop(maxH)
        else:
            while minH and not visited[minH[0][1]]:
                heapq.heappop(minH)
            if minH:
                visited[minH[0][1]]=False
                heapq.heappop(minH)

        while minH and not visited[minH[0][1]]:heapq.heappop(minH)
        while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
        result.append(f'{-maxH[0][0]} {minH[0][0]}'if maxH and minH else'EMPTY')

print('\n'.join(result))