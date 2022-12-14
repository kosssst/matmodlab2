import heapq

def ToKanonView(c: list, A: list, b: list, sign: list) -> None:
    for i, s in enumerate(sign):
        if s == -1:
            c.append(0)
            for k in range(len(sign)):
                if k == i:
                    A[i].append(1)
                else:
                    A[i].append(0)

def column(A: list, j: int) -> list:
    return [row[j] for row in A]

def transpose(A: list) -> list:
    return [column(A, j) for j in range(len(A[0]))]

def isPivotCol(col: list) -> bool:
    return (len([c for c in col if c == 0]) == len(col) - 1) and sum(col) == 1

def variableValueForPivotColumn(tableau: list, column: int):
    pivotRow = [i for (i, x) in enumerate(column) if x == 1][0]
    return tableau[pivotRow][-1]

def initialTableau(c: list, A: list, b: list) -> list:
    tableau = [row[:] + [x] for row, x in zip(A, b)]
    tableau.append([ci for ci in c] + [0])
    return tableau

def primalSolution(tableau: list) -> list:
    columns = transpose(tableau)
    indices = [j for j, col in enumerate(columns[:-1]) if isPivotCol(col)]
    return [(colIndex, variableValueForPivotColumn(tableau, columns[colIndex]))
            for colIndex in indices]

def objectiveValue(tableau: list) -> int:
    return -(tableau[-1][-1])


def canImprove(tableau: list) -> bool:
    lastRow = tableau[-1]
    return any(x > 0 for x in lastRow[:-1])

def moreThanOneMin(L: list) -> bool:
    if len(L) <= 1:
        return False
    x, y = heapq.nsmallest(2, L, key=lambda x: x[1])
    return x == y

def findPivotIndex(tableau: list) -> tuple[int, int]:
    column_choices = [(i, x) for (i, x) in enumerate(tableau[-1][:-1]) if x > 0]
    column = min(column_choices, key=lambda a: a[1])[0]
    if all(row[column] <= 0 for row in tableau):
        raise Exception('Linear program is unbounded.')
    quotients = [(i, r[-1] / r[column])
                 for i, r in enumerate(tableau[:-1]) if r[column] > 0]
    if moreThanOneMin(quotients):
        raise Exception('Linear program is degenerate.')
    row = min(quotients, key=lambda x: x[1])[0]
    return row, column

def pivotAbout(tableau: list, pivot: int) -> None:
    i, j = pivot
    pivotDenom = tableau[i][j]
    tableau[i] = [x / pivotDenom for x in tableau[i]]
    for k, row in enumerate(tableau):
        if k != i:
            pivotRowMultiple = [y * tableau[k][j] for y in tableau[i]]
            tableau[k] = [x - y for x, y in zip(tableau[k], pivotRowMultiple)]

def simplex(c: list, A: list, b: list, sign: list) -> tuple[list, list, int]:
    ToKanonView(c, A, b, sign)
    tableau = initialTableau(c, A, b)
    print("Initial tableau:")
    for row in tableau:
        print(row)
    print()
    while canImprove(tableau):
        pivot = findPivotIndex(tableau)
        print("Next pivot index is=%d,%d \n" % pivot)
        pivotAbout(tableau, pivot)
        print("Tableau after pivot:")
        for row in tableau:
            print(row)
        print()
    return tableau, primalSolution(tableau), objectiveValue(tableau)