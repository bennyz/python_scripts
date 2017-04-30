#!/usr/bin/env python3

nm = input().split(' ')
n = int(nm[0])
m = int(nm[1])

arr = [0] * (n + 1)

for i in range(m):
    inputs = input().split(' ')
    a = int(inputs[0])
    b = int(inputs[1])
    k = int(inputs[2])

    arr[a] += k

    if b + 1 <= n:
        arr[b + 1] -= k

print(arr)

suma = 0
maxa = suma
for i in range(len(arr)):
    suma += arr[i]
    print(suma)
    if suma > maxa:
        maxa = suma
print(maxa)

