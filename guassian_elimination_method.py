from datetime import datetime

def calcAnswer(matA, result):
    n = len(matA)
    vector = [0] * n
    vector[n - 1] = result[n - 1][0]
    for i in range(n - 2, -1, -1):
        vector[i] = result[i][0]
        for j in range(n - 1, i, -1):
            if matA[i][j] != 0:
                vector[i] -= matA[i][j] * vector[j]
        vector[i] /= matA[i][i]
    return vector


def detCalculator(matA):  # it works!!!
    matLen = len(matA)
    if matLen < 2:
        return None
    if matLen == 2:
        return (matA[0][0] * matA[1][1]) - (matA[0][1] * matA[1][0])
    else:
        sum = 0
        currentRow = 0
        # will calculate det of first row
        # We assume that its a square matrix
        for currentCol in range(matLen):
            newMat = [x[:] for x in matA]
            for row in range(matLen):
                del newMat[row][currentCol]
            del newMat[currentRow]
            pivot = matA[currentRow][currentCol]
            if currentCol % 2 != 0:
                pivot *= -1
            sum += pivot * detCalculator(newMat)
        return sum


def elementryInverse(matA, i, j=None):
    if j is None:
        j = i
    if matA[i][j] != 1:
        matA[i][j] = -matA[i][j]
    return matA


def gaussianElimination(matA, result):
    if detCalculator(matA) == 0:
        return "Matrix unsolvable (zero or infinite results)"
    matA, result = makeUpperTriangular(matA, result)
    return calcAnswer(matA, result)


def makeUpperTriangular(matA, result):
    dim = len(matA)
    for i in range(dim):
        matA, result = pivoting(matA, i, result)
        for j in range(i + 1):
            if i == j:
                matA, result = makePivotOne(i, matA, result)
            else:
                matA, result = makePivotZero(i, j, matA, result)
    return (matA, result)


def pivoting(matA, index, result=None):
    # find max pivot in each column
    n = len(matA)
    for j in range(index, n):
        if abs(matA[j][index]) > abs(matA[index][index]):
            matA[index], matA[j] = matA[j], matA[index]
            if result != None:
                result[index], result[j] = result[j], result[index]
    if result != None:
        return (matA, result)
    return matA


def makePivotZero(i, j, matA, result, LU=False):
    if matA[j][j] == 0:
        return matA
    I = makeIdentityMat(len(matA))
    I[i][j] = -matA[i][j] / matA[j][j]
    if LU is True:
        return (matMultiply(I, matA), elementryInverse(I, i, j))
    return (matMultiply(I, matA), matMultiply(I, result))


def makePivotOne(i, matA, result, LU=False):
    if matA[i][i] == 0:
        return matA
    I = makeIdentityMat(len(matA))
    I[i][i] = 1 / matA[i][i]
    if LU is True:
        return elementryInverse(I, i)
    return (matMultiply(I, matA), matMultiply(I, result))


def makeIdentityMat(dim):
    # Works for square mat only
    identityMat = []
    for i in range(dim):
        rowMat = []
        for j in range(dim):
            if i == j:
                rowMat.append(1)
            else:
                rowMat.append(0)
        identityMat.append(rowMat)
    return identityMat


def matMultiply(matA, matB):
    # multiply from the left: A * B.
    result = []
    for i in range(len(matA)):
        rowMat = []
        for j in range(len(matB[i])):
            index = 0
            for k in range(len(matB)):
                index += matA[i][k] * matB[k][j]
            rowMat.append(index)
        result.append(rowMat)
    return result


# q21 = [[10, 8, 1],
#      [4, 10, -5],
#      [5, 1, 10]]
#
# q21_result = [[-7], [2], [1.5]]
# now = datetime.now()
# time = str(now.day) + str(now.hour) + str(now.minute)
# result = gaussianElimination(q21, q21_result)
#
# final_result = []
# q29 = [[1, 0, -1],
#      [-0.5, 1, -0.25],
#      [1, -0.5, 1]]

# q29_result = [[0.2], [-1.425], [2]]
#
# now = datetime.now()
# time = str(now.day) + str(now.hour) + str(now.minute)
# result = gaussianElimination(q29, q29_result)
#
# final_result = []

# for res in result:
#     final_result.append(float(str(("%.6f" % res).rstrip('0')) + "00000" + time))
#
# print("The gaussian elimination method result is: ", final_result)


