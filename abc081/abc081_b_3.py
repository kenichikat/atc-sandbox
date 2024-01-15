
def how_many_times(num):
    counter = 0
    while num % 2 == 0:
        num //= 2
        counter += 1

    return counter


n = int(input())
a = list(map(int, input().split()))
ans = min(map(how_many_times, a))
print(ans)
