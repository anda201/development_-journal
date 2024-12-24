for tc in range(1, int(input())+1):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # A의 x1 > B의 x2 or A의 x2 < B의 x1 or A의 y1 > B의 y2 or A의 y2 < B의 y1
    # 사각형이 떨어져 있는 경우
    if a[0] > b[2] or a[2] < b[0] or a[1] > b[3] or a[3] < b[1]:
        print(f"#{tc} 4")

    # A의 y2 == B의 y1 or A의 y1 == B의 y2
    elif a[3] == b[1] or a[1] == b[3]:
        # A의 x2 == B의 x1 or A의 x1 == B의 x2
        if a[2] == b[0] or a[0] == b[2]:
            # 꼭짓점이 만나는 경우
            print(f"#{tc} 3")
        else:
            # 한 변이 만나는 경우
            print(f"#{tc} 2")

    # A의 x2 == B의 x1 or A의 x1 == B의 x2
    elif a[2] == b[0] or a[0] == b[2]:
        print(f"#{tc} 2")

    else:
        print(f"#{tc} 1")


