n = int(input())
a = list(map(int, input().split()))

counter = 0

# while True:
#     can_do = True
#     for i in range(n):
#         if a[i] % 2 != 0:
#             can_do = False

#     if not can_do:
#         break

#     for i in range(n):
#         a[i] //= 2

#     counter += 1

while all([i % 2 == 0 for i in a]):
    a = [i // 2 for i in a]
    counter += 1

print(counter)
