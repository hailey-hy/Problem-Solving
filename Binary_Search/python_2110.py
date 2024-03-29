# 공유기 설치

import sys

n, c = map(int, sys.stdin.readline().split())
houses = []

for _ in range(n):
    houses.append(int(sys.stdin.readline()))

houses.sort()

start, end = 1, houses[-1] - houses[0]
answer = 0

while start < end:
    mid = (start + end) // 2
    current = houses[0]
    count = 1

    for i in range(1, len(houses)):
        if houses[i] - current >= mid:
            count += 1
            current = houses[i]
        
    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid

print(answer)