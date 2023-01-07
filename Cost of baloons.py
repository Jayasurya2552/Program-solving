#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/mojtaba-prepares-contest-29b2a044/
# Cost of Baloons

T = int(input())

while T != 0:
    a2 = []
    b2 = []
    A = input().split()
    a1 = int(A[0])
    b1 = int(A[1])
    n = int(input())
    while n != 0:

        i = input().split()
        x = int(i[0])
        y = int(i[1])

        if x == 1:
            a2.append(x)
        if y == 1:
            b2.append(y)
        n = n - 1

    result_1 = len(a2) * a1
    result_2 = len(b2) * b1

    sum1 = result_1 + result_2

    result_3 = len(a2) * b1
    result_4 = len(b2) * a1

    sum2 = result_3 + result_4

    if sum1 > sum2:
        print(sum2)
    else:
        print(sum1)
    T = T - 1

