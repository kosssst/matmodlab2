import simplex


def var11():
    c = [1, -2, 3, -1]
    A = [[2, -1, 2, -3], [1, 2, -1, 1]]
    b = [5, 3]
    sign = [-1, -1]
    try:
        t, s, v = simplex.simplex(c, A, b, sign)
        print("Solution:")
        print(s)
        print("F = " + str(v))
    except:
        print("Has no solutions")


def var13():
    c = [2, -1, 3, -2, 1]
    A = [[-1, 1, 1, 0, 0], [1, -1, 0, 1, 0], [1, 1, 0, 0, 1]]
    b = [1, 1, 2]
    sign = [0, 0, 0]
    try:
        t, s, v = simplex.simplex(c, A, b, sign)
        print("Solution:")
        print(s)
        print("F = " + str(v))
    except:
        print("Has no solutions")


if __name__ == "__main__":
    print("\nVariant 11:")
    var11()
    print("\nVariant 13:")
    var13()
