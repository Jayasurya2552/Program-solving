# Question : https://www.hackerearth.com/problem/algorithm/bowl-em-over-4/?utm_source=new_practice
# Bowl 'Em over :

N = int(input())
x = [int(i) for i in input().split()]
X = []


def checker(d1, d2, d3, d4):
    if d1 == 10:
        a = d1 + d2 + d3
        X.append(a)
    if d2 == 10 and d1 != 10:
        a = d1 + d2 + d3 + d4
        X.append(a)
    if d1 + d2 == 10 and d1 != 0 and d2 != 0:
        a = d1 + d2 + d3
        X.append(a)
    if d1 != 10 and d2 != 10 and d1 + d2 != 10:
        a = d1 + d2
        X.append(a)


if __name__ == "__main__":
    while N != 0:
        if len(x) == 0:
            x = [int(i) for i in input().split()]
        if len(x) >= 4:
            checker(x[0], x[1], x[2], x[3])
            if x[0] == 10:
                x = x[1:len(x)]
            else:
                x = x[2:len(x)]
        if len(x) < 4:
            if len(x) == 3:
                if x[0] == 10 and x[1] != 10:
                    b = x[0] + x[1] + x[2]
                    X.append(b)
                    x = x[1:len(x)]
                else:
                    b = x[0] + x[1] + x[2]
                    X.append(b)
                    x = []
                    N = N - 1
                    print(sum(X))
                    X = []
            else:
                b = x[0] + x[1]
                X.append(b)
                x = []
                N = N - 1
                print(sum(X))
                X = []
