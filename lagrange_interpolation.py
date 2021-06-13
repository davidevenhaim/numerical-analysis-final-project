from sympy import *
from datetime import datetime

x = Symbol('x')


def L(i, f, x0):
    L1 = ""
    num = 1  # the actual numeric result
    for j in range(len(f)):
        if j != i:
            num *= ((x0 - f[j][0]) / (f[i][0] - f[j][0]))
            L1 += "((x - " + str(f[j][0]) + ") / (" + str(f[i][0]) + " - " + str(f[j][0]) + "))"
            if i == len(f) - 1:
                if j != len(f) - 2:
                    L1 += " + "
            elif j != len(f) - 1:
                L1 += " + "
    return num, L1


def lagrange_interpolation(f, x0):
    sum = 0
    P = ""
    l = list()
    for i in range(len(f)):
        if i != 0:
            P += " + "
        num, L1 = L(i, f, x0)
        P += "L" + str(i) + " * " + str(f[i][1])
        l.append(('L' + str(i), L1, num))
        sum += num * f[i][1]
    return sum, l, P


x0 = 1.47
f = [(1.2, 1.5095), (1.3, 1.6984), (1.4, 1.9043), (1.5, 2.1293), (1.6, 2.3756)]
ans, l, P = lagrange_interpolation(f, x0)
print("P: " + str(P) + "\n")
print("L array:")
for i in l:
    print(i)

now = datetime.now()
today_str = str(now.day) + str(now.hour) + "0" + str(now.minute)
final_answer = str(("%.6f" % ans).rstrip('0')) + "00000" + today_str

print("\nf(" + str(x0) + ") = " + final_answer)
