hp, a = map(int, input().split())

if hp % a == 0:
    print(hp // a)
else:
    print(hp // a) + 1
