#
# a = int(input())
# b = int(input())
#
# for i in range(a,b+1):
#     print(i)
#
#
# # 2
#
# a = int(input())
# b = int(input())
#
# if a < b:
#     for i in range(a, b+1):
#         print(i)
# else:
#     for i in range(a, b-1, -1):
#         print(i)
#
#
# # 3
#
#
# n = int(input('Введите количество чисел: '))
#
# sum = 0
#
# for i in range(n):
#     sum += int(input('Введите значение: '))
#     print(sum)
#
#
# # 4
#
# a = 1
# n = int(input())
# for i in range(1, n + 1):
#     a *= i
# print(a)
#
#
# # 5
#
# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, sep = '', end='')
#     print()
#
#
# # 6
#
# n = int(input())
# i = 0
#
# while i ** 2 < n:
#     print(i ** 2)
#     i += 1
#
#
# # 7
#
# n = int(input())
# st = 2
# p = 1
# while st <= n:
#     st *= 2
#     p += 1
# print(p - 1, st // 2)
#
#
# # 8
#
# x = int(input())
# y = int(input())
# l = x
# d = 0
#
# while l <= y:
#     l += 0.1*l
#     d += 1
#
# print(d)
#
#
# # 9
#
# len = 0
# while int(input()) != 0:
#     len += 1
# print(len)
#
#
# # 10
#
# pr = int(input())
# x = 0
# while pr != 0:
#     last = int(input('Введите число: '))
#     if last != 0 and pr < last:
#         x += 1
#     pr = last
# print(x)
#
#
# # 11
#
# a = int(input())
# b = int()
# c = int()
#
# while a != 0:
#     if b < a:
#         b = a
#     if c < b:
#         b, c = c, b
#     a = int(input())
# print(b)
#
#
# # 12
#
# n = int(input())
# if n == 0:
#     print(0)
# else:
#     a, b = 0, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     print(b)
#
#
# # 13
#
# a = int(input())
# x2 = x1 = 0
#
# while a != 0:
#     b = int(input())
#     if a == b:
#         x1 += 1
#         if x1 > x2:
#             x2 = x1
#     else:
#         x1 = 0
#     a = b
# print(x2 + 1)
#
#
# # 14
#
# a = input().split()
# for i in range(0, len(a), 2):
#     print(a[i])
#
#
# # 15
#
# a = [int(i) for i in input().split()]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i])


# # 16
#
# max = 0
# a = [int(i) for i in input().split()]
# for i in range(1, len(a)):
#     if a[i] > a[max]:
#         max = i
# print(a[max], max)
#
#
# # 17
#
# a = [int(i) for i in input().split()]
# x = int(input())
# pos = 0
# while pos < len(a) and a[pos] >= x:
#     pos += 1
# print(pos + 1)
#
#
# # 18
#
# a = [int(i) for i in input().split()]
#
# for i in range(1, len(a), 2):
#     a[i - 1], a[i] = a[i], a[i - 1]
#
# print(' '.join([str(i) for i in a]))
#
#
# # 19
#
# a = [int(i) for i in input().split()]
#
# min = a.index(min(a))
# max = a.index(max(a))
#
# [a[max], a[min]] = [a[min], a[max]]
#
# print(' '.join([str(i) for i in a]))
#
#
# # 20
#
# a = [int(s) for s in input().split()]
#
# k = int(input())
#
# for i in range(k + 1, len(a)):
#     a[i - 1] = a[i]
# a.pop()
#
# print(' '.join([str(i) for i in a]))
#
#
# # 21
#
# a = [int(s) for s in input().split()]
#
# k, c = [int(s) for s in input().split()]
#
# a.append(0)
#
# for i in range(len(a) - 1, k, -1):
#     a[i] = a[i - 1]
#
# a[k] = c
# print(' '.join([str(i) for i in a]))
#
#
#
# # 22
# n = 8
# x = []
# y = []
# for i in range(n):
#     new_x, new_y = [int(s) for s in input().split()]
#     x.append(new_x)
#     y.append(new_y)
#
# correct = True
# for i in range(n):
#     for j in range(i + 1, n):
#         if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
#             correct = False
#
# if correct:
#     print('NO')
# else:
#     print('YES')


