n, m = map(int, input().split())
box = one = 1001

# 보드카 묶음 최저가와 낱개 최저가 산출
for i in range(m):
    a, b = map(int, input().split())
    box = min(box, a)
    one = min(one, b)

# 보드카 낱개로 6병 사는 비용이 6병 묶음으로 사는 비용보다 작을 경우
if box > one * 6:
    print(one*n)
else:
    # 묶음으로 사고 남은 개수를 낱개 구입하는 것보다 묶음으로 사는게 저렴할 경우
    if box < one*(n%6):
        print(box*(n//6)+box)
    else:
        # 묶음으로 사고 남은 개수를 낱개로 구입하는 비용
        print(box*(n//6)+one*(n%6))