import copy
from datetime import datetime


def jacobi(matA, result, epsilion = 0.000001):
    R1 = []
    iteration = 0
    for i in range(len(matA)):
        R1.append([0])
    print("Jacobi Method:\n")
    while True:
        print("Iteration number: ", iteration, " results -> " , R1)
        iteration += 1
        R2 = copy.deepcopy(R1)
        for i in range(len(matA)):
            rowSum = 0
            for j in range(len(matA[i])):
                if j != i:
                    rowSum += matA[i][j] * R1[j][0]
            R2[i][0] = ((-rowSum + result[i][0]) / matA[i][i])
        if(checkDifference(R1, R2, epsilion)):
            break
        if(not checkDifference(R1, R2, iteration * 10)):
            print("The matirx has no dominant diagonal.")
            print("Jacobi will not give a proper answer!")
            break
        R1 = copy.deepcopy(R2)
    return R1


def checkDifference(R1, R2, epsilion):
    for i in range(len(R1)):
        if abs(abs(R2[i][0]) - abs(R1[i][0])) > epsilion:
            return False
    return True


q21 = [[10, 8, 1],
     [4, 10, -5],
     [5, 1, 10]]

q21_result = [[-7], [2], [1.5]]

final_result = []

now = datetime.now()
time = str(now.day) + str(now.hour) + str(now.minute)

result = jacobi(q21, q21_result)
for res in result:
    final_result.append(float(str(("%.6f" % res[0]).rstrip('0')) + "00000" + time))
print("The result of Jacobi methos is: ", final_result)


