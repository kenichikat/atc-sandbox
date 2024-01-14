n, a, b = map(int, input().split())

total = 0
for i in range(1, n+1):
    s = sum(map(int, str(i)))

    if a <= s <= b:
        total += i

print(total)
