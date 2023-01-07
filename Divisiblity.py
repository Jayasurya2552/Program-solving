# Q - https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisible-or-not-81b86ad7/
# Divisiblity


N = int(input())

A = [int(i) for i in input().split()]

Y = []

for integer in A:
    X = [int(j) for j in str(integer)]
    Y.append(X[-1])

s = [str(x) for x in Y]
result = int("".join(s))

if result % 10 == 0:
    print("Yes")
else:
    print("No")
