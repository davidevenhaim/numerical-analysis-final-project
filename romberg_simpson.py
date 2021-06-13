from math import e
from sympy import *
from datetime import datetime

x = Symbol('x')


def simpson_method(f, a, b, n):
    print("\nUsing the Simpson - Method")
    print("Function: " + str(f))

    if n % 2 != 0:
        n = n - 1
    print("n: " + str(float(n)))
    h = (b - a) / n
    print("h: " + str(float(h)))
    print("\nmiddle results:")
    sum = f.subs(x, a)
    func = "f(a)"
    j = 4
    x0 = a + h
    print("i: " + str(0) + "  x: " + str(float(x0)) + "   f(x): " + str(float(f.subs(x, x0))))
    for i in range(1, n):
        sum += j * f.subs(x, x0)
        func += " + " + str(j) + "*f(x" + str(i) + ")"
        x0 += h
        if j == 4:
            j = 2
        else:
            j = 4
        print("i: " + str(i) + "  x: " + str(float(x0)) + "  f(x): " + str(float(f.subs(x, x0))))
    sum += f.subs(x, b)
    func += " + f(b)"
    func = "(1/3)*h * (" + func + ")"
    return float((1 / 3) * h * sum), func


def trapeze_method(f, k, a, b):
    h = (b - a) / (2**k)
    X0 = a
    sum = h
    sum_new = 0
    nos = str(h)+"*"+"["+"0.5*f("+str(a)+")"+"+"

    for i in range(0, (2**k)-1):
        X0 = X0 + h
        sum_new += f.subs(x, X0)
        nos += "f("+str(X0)+")"+"+"
    nos += "f("+str(b)+")"+"]"
    sum = sum * (0.5*f.subs(x, a) + 0.5*f.subs(x, b) + sum_new)
    nos += "="+str(float(sum))
    return sum, nos


def romberg_method(f, a, b, epsilon=0.000001):
    print("Using the Romberg - Method")
    r = dict()
    r2 = dict()
    r[0, 0], r2[0, 0] = trapeze_method(f, 0, a, b)
    r[1, 0], r2[1, 0] = trapeze_method(f, 1, a, b)
    r[1, 1] = r[1, 0] + (1 / 3) * (r[1, 0] - r[0, 0])
    r2[1, 1] = "r[1, 0] + (1 / 3) * (r[1, 0] - r[0, 0])"+"="+str(float(r[1, 1]))
    i = 1

    def rom(i, j):
        if j == 0:
            r[i, j], r2[i, j] = trapeze_method(f, i, a, b)
            return
        if (i, j - 1) not in r:
            rom(i, j - 1)
        if (i - 1, j - 1) not in r:
            rom(i - 1, j)
        r[i, j] = r[i, j - 1] + ((1 / (4 ** (j) - 1)) * (r[i, j - 1] - r[i - 1, j - 1]))
        r2[i, j] = "r["+str(i)+","+str(j - 1)+"] + "+str((1 / (4 ** j - 1))) + "* (r["+str(i)+"," + \
                   str(j - 1)+"] - r[" + str(i - 1) + ", " + str(j - 1)+"]))=" + str(float(r[i, j]))

    while abs(r[i, i] - r[i - 1, i - 1]) > epsilon:
        rom(i + 1, i + 1)
        i += 1
    return r[i, i], r2


now = datetime.now()
time_str = str(now.day) + str(now.hour) + str(now.minute)


# f9 = (sin(x ** 4 + 5 * x - 6)) / (2 * (e ** (-2 * x + 5)))
# r, r2 = romberg_method(f9, -0.5, 0.5)
# for i in r2:
#     print("i=" + str(i[0]) + " j=" + str(i[1]) + " " + r2[i])
# final_answer_romberg = str("%.6f" % r) + "00000" + time_str
# print("\nThe result of the integral is: " + final_answer_romberg)
# Simpson
# a = -0.5
# b = 0.5
# sum, func = simpson_method(f9, a, b, 6)
# final_answer_simpson = str("%.6f" % sum) + "00000" + time_str
# print("The result of the integral is: " + final_answer_simpson)



# f17 = ((x**2)*(e**(-x**2-5*x-3)))*(3*x-1)
# r, r2 = romberg_method(f17, 0.5, 1)
# for i in r2:
#     print("i=" + str(i[0]) + " j=" + str(i[1]) + " " + r2[i])
# final_answer_romberg = str("%.6f" % r) + "00000" + time_str
# print("\nThe result of the integral is: " + final_answer_romberg)
# a = 0.5
# b = 1
# Simpson
# sum, func = simpson_method(f17, a, b, 6)
# final_answer_simpson = str("%.6f" % sum) + "00000" + time_str
# print("The result of the integral is: " + final_answer_simpson)



# f15 = (x * e ** (-x ** 2 + 5 * x - 3)) * (x ** 2 + 3 * x - 5)
# a = 0.5
# b = 1
# r, r2 = romberg_method(f15, a, b)
# for i in r2:
#     print("i=" + str(i[0]) + " j=" + str(i[1]) + " " + r2[i])
# final_answer_romberg = str("%.6f" % r) + "00000" + time_str
# print("\nThe result of the integral is: " + final_answer_romberg)
# #Simpson
# sum, func = simpson_method(f15, a, b, 6)
# final_answer_simpson = str("%.6f" % sum) + "00000" + time_str
# print("The result of the integral is: " + final_answer_simpson)