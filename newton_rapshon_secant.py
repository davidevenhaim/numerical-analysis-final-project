from math import e
from sympy import *
from datetime import datetime

x = Symbol('x')


def newton_raphson(f, start_point, end_point, epsilon=0.000001):

    xr = (end_point - start_point) / 2 + start_point
    print("guess x0 = " + str(xr))
    print("i=1 | xr = " + str(xr) + " f(xr) = " + str(float(f.subs(x, xr))) + " f'(xr) = " + str(
        float(f.diff(x).subs(x, xr))))
    xr1 = xr - (float(f.subs(x, xr)) / float(diff(f).subs(x, xr)))
    print("i=2 | xr = " + str(xr1) + " f(xr) = " + str(float(f.subs(x, xr1))) + " f'(xr) = " + str(
        float(f.diff(x).subs(x, xr1))))
    count = 3
    while abs(float(f.subs(x, xr))) > epsilon and abs(xr1 - xr) > epsilon:
        xr = xr1
        try:
            xr1 = xr - (float(f.subs(x, xr)) / float(diff(f).subs(x, xr)))
            print("i=" + str(count) + " | xr = " + str(xr1) + " f(xr) = " + str(
                float(f.subs(x, xr1))) + " f'(xr) = " + str(
                float(f.diff(x).subs(x, xr1))))
        except:
            if float(diff(f).subs(x, xr)) == 0:
                return xr, count
        count += 1
    return xr1, count - 1


def secant_method(f, start_point, end_point, epsilon=0.000001):

    xr0 = (end_point - start_point) / 2 + start_point  # xr-1
    xr = (end_point - start_point) / 2 + epsilon + start_point  # xr
    print("guess: x0 = " + str(xr0) + " x1 = " + str(xr))
    try:
        xr1 = (xr0 * float(f.subs(x, xr)) - xr * float(f.subs(x, xr0))) / (
                float(f.subs(x, xr)) - float(f.subs(x, xr0)))  # xr+1
        print("x(r-1) = " + str(xr0) + " x(r) = " + str(xr) + " x(r+1) = " + str(xr1))
    except:
        if float(f.subs(x, xr)) == 0:
            return xr
        elif float(f.subs(x, xr0)) == 0:
            return xr0
    count = 1
    while abs(float(f.subs(x, xr))) > epsilon:
        xr0 = xr
        xr = xr1
        try:
            xr1 = (xr0 * float(f.subs(x, xr)) - xr * float(f.subs(x, xr0))) / (
                    float(f.subs(x, xr)) - float(f.subs(x, xr0)))  # xr+1
            print("x(r-1) = " + str(xr0) + " x(r) = " + str(xr) + " x(r+1) = " + str(xr1))
        except:
            if float(f.subs(x, xr)) == 0:
                return xr, count
            elif float(f.subs(x, xr0)) == 0:
                return xr0, count
        count += 1
    return xr1, count


def main_func_newton(f, start_point, end_point):

    x0 = start_point
    jump = 0.001
    roots_newton = list()
    while x0 < end_point:
        ay = float(f.subs(x, x0))
        by = float(f.subs(x, x0 + jump))
        if ay * by < 0:  # Suspicious root
            print("\nrange = [" + str(x0) + ", " + str(x0 + jump) + "]")
            roots_newton.append(newton_raphson(f, x0, x0 + jump))
        elif ay == 0 and (x0, 0) not in roots_newton:
            roots_newton.append((x0, 0))
        elif by == 0:
            roots_newton.append((x0 + jump, 0))
        x0 += jump
    # printing:
    if not roots_newton:
        print("no roots found")
    else:
        print("\nResults of Newton-Raphson: ")
        for t in roots_newton:
            now = datetime.now()
            time_str = str(now.day) + str(now.hour) + str(now.minute)
            final_answer = str("%.6f" % t[0]) + "00000" + time_str
            print("number of iterations: " + str(t[1]) + " root: " + final_answer)
    return roots_newton


def main_func_secant(f, start_point, end_point):

    x0 = start_point
    jump = 0.001
    roots_secant = list()
    while x0 < end_point:
        ay = float(f.subs(x, x0))
        by = float(f.subs(x, x0 + jump))
        if ay * by < 0:  # Suspicious root
            print("\nrange = [" + str(x0) + ", " + str(x0 + jump) + "]")
            roots_secant.append(secant_method(f, x0, x0 + jump))
        elif ay == 0 and (x0, 0) not in roots_secant:
            roots_secant.append((x0, 0))
        elif by == 0:
            roots_secant.append((x0 + jump, 0))
        x0 += jump
    # printing:
    if not roots_secant:
        print("no roots found")
    else:
        print("\nResults of Secant-Method: ")
        for t in roots_secant:
            now = datetime.now()
            time_str = str(now.day) + str(now.hour) + str(now.minute)
            final_answer = str("%.6f" % t[0]) + "00000" + time_str
            print("number of iterations: " + str(t[1]) + " root: " + final_answer)
    return roots_secant


# Questions:

# f9 = (sin(x ** 4 + 5 * x - 6)) / (2 * (e ** (-2 * x + 5)))
# print("func: " + str(f9)+"\nNewton Raphson:")
# main_func_newton(f9, -1.5, 1.5)
# print("\n\nSecant Method:")
# main_func_secant(f9, -1.5, 1.5)

# f17 = ((x**2)*(e**(-x**2-5*x-3)))*(3*x-1)
# print("func: " + str(f17)+"\nNewton Raphson:")
# main_func_newton(f17, 0, 1.5)
# print("\n\nSecant Method:")
# main_func_secant(f17, 0, 1.5)

# f15 = (x * e ** (-x ** 2 + 5 * x - 3)) * (x ** 2 + 3 * x - 5)
# print("func: " + str(f15)+"\nNewton Raphson:")
# main_func_newton(f15, 0, 1.5)
# print("\n\nSecant Method:")
# main_func_secant(f15, 0, 1.5)

