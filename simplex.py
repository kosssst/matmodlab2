def ToMin(koefs: list) -> None:
    for i in range(len(koefs)):
        koefs[i] = 0 - koefs[i]

def lessThenZero(koefs: list) -> bool:
    b = True
    for i in koefs:
        if i >= 0:
            b = False
    return b

def addNewVar(koefs: list, limitations: list, data: int or str, data_for_limits: int, which_limit: int) -> None:
    pass

def simplex(koefs: list, limitations: list) -> list:
    # koefs = [x1, x2, x3, ..., 1 or -1 (max or min)]
    # limitations = [[x1, x2, x3, ..., limit, sign],
    #                [x1, x2, x3, ..., limit, sign],
    #                ....
    #                [x1, x2, x3, ..., limit, sign]]
    # if koefs[last] == 1 -> ToMin(koefs)
    # if lessThenZero(koefs) -> return "Fuck you"
    pass