from datetime import datetime

def neville(f, x0):
    points = dict()
    str_list = list()

    count = 0
    for i in f:
        points[(count, count)] = i[1]  # get only y
        str_list.append("points[" + str(count) + ", " + str(count) + "] = " + str(i[1]))
        count += 1

    count = 1
    while True:
        for i in range(len(f) - count):
            n = i + count
            points[(i, n)] = ((x0 - f[i][0]) * points[(i + 1, n)] - (x0 - f[n][0]) * points[(i, n - 1)]) / (f[n][0] - f[i][0])
            str_list.append("P[" + str(i) + ", " + str(n) + "] = ((x - x" + str(i) + ") * P[" + str(i + 1) + ", " + str(
                n) + "] - (x - x" + str(n) + ") * P[" + str(i) + ", " + str(n - 1) + "]) / (x" + str(n) + " - x" + str(
                i) + ")")
        if len(f) - count == 1:
            return points[(0, len(f) - 1)], points, str_list
        count += 1


x0 = 1.47
f = [(1.2, 1.5095), (1.3, 1.6984), (1.4, 1.9043), (1.5, 2.1293), (1.6, 2.3756)]
answer, points, str_list = neville(f, x0)
print(points)
print("P array: ")
count = 0
for i in points:
    print(str_list[count])
    count += 1
    print(str(i) + "= " + str(points[i]) + "\n")

now = datetime.now()
today_str = str(now.day) + str(now.hour) + str(now.minute)
final_answer = str(("%.6f" % answer).rstrip('0')) + "00000" + today_str

print("\nResult of using Neville method:")
print("f(" + str(x0) + ") = " + final_answer)
