n = int(input())
arr = []
for _ in range(n):
    d, w = map(int, input().split())
    arr.append((d,w))
arr.sort()
remain = arr[-1][0]
ans = 0
answer = []
while True:
    if remain == 0:
        break
    while True:
        if arr and arr[-1][0] == remain:
            answer.append(arr.pop()[1])
        else:
            break
    remain -= 1
    answer.sort()
    if answer:
        ans += answer.pop()

print(ans)