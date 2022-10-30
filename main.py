import simplex

if __name__ == "__main__":
    c = [1, -2, 3, -1]
    A = [[2, -1, 2, -3], [1, 2, -1, 1]]
    b = [5, 3]
    try:
        t, s, v = simplex.simplex(c, A, b)
        print(s)
        print(v)
    except:
        print("Has no solutions")
    