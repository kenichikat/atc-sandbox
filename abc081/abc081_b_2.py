
def all_even(a):
    for i in a:
        if i % 2 == 1:
            return False
    return True


def replace_value(a):
    for i in range(len(a)):
        a[i] //= 2


n = int(input())
a = list(map(int, input().split()))

counter = 0
while all_even(a):
    replace_value(a)
    counter += 1

print(counter)
