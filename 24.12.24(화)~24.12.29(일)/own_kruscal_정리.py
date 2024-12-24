def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    boss[a] = b

def find(n):
    if boss[n] != n:
        boss[n] = find(boss[n])
    return boss[n]

n, node = map(int, input().split())
lst = []
boss = [i for i in range(91)]
for _ in range(n):
    a, b, price = input().split()
    lst.append((ord(a), ord(b), int(price)))

# price를 기준으로 오름차순 정렬
lst.sort(key=lambda x: x[2])
cnt = 0
ans = 0
for a, b, price in lst:
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        ans += price

    if cnt == node -1:
        print(ans)
        break
