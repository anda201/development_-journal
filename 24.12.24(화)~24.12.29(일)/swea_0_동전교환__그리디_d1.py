price = int(input())
coin = 0

for i in (500, 100, 50, 10):
    if price >= i:
        coin += price // i
        price %= i

print(coin)

