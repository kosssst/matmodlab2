import simplex


def var11():
    c = [1, -2, 3, -1]
    A = [[2, -1, 2, -3], [1, 2, -1, 1]]
    b = [5, 3]
    try:
        t, s, v = simplex.simplex(c, A, b)
        print(s)
        print(v)
    except:
        print("Has no solutions")


def var13():
    c = [2, -1, 3, -2, 1]
    A = [[-1, 1, 1, 0, 0], [1, -1, 0, 1, 0], [1, 1, 0, 0, 1]]
    b = [1, 1, 2]
    try:
        t, s, v = simplex.simplex(c, A, b)
        print(s)
        print(v)
    except:
        print("Has no solutions")


if __name__ == "__main__":
    var11()
    var13()
