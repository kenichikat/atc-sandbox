

def calc_sum_digit(n):
    sum_digit = 0
    while n > 0:
        sum_digit += n % 10
        n //= 10
    return sum_digit


if __name__ == '__main__':
    n, a, b = map(int, input().split())

    total = 0
    for i in range(1, n+1):
        sum_digit = calc_sum_digit(i)

        if a <= sum_digit <= b:
            total += i

    print(total)
