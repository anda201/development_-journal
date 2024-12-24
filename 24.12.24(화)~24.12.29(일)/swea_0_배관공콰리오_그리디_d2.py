a, l = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()
# 테이프가 부착된 최대 위치값(now), 테이프의 개수(cnt)
now = cnt = 0

for hole in holes:
    # 테이프가 부착된 위치보다 구멍의 위치가 더 클 경우
    if now < hole:
        # 테이프의 개수를 추가
        cnt += 1
        # 구멍의 위치값에서 테이프의 길이 - 1(구멍의 위치값에도 테이프가 붙어서 -1)만큼 할당
        now = hole + l - 1

print(cnt)
