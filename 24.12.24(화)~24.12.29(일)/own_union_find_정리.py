def find(n):
    if boss[n] == n:
        return n
    result = find(boss[n])
    return result

# 경로 압축 코드
# def find(n):
#     if boss[n] != n:
#         boss[n] = find(boss[n])
#     return boss[n]

def union(a ,b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    boss[b] = a

boss = [i for i in range(10)]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    union(a, b)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print("o")
    else:
        print("x")
