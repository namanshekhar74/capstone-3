matrix = [["x", "o", ""],
          ["o", "x", "o"],
          ["x", "x", "x"]]


def strength(matrix):
    dom_x = []
    dom_o = []
    for i in matrix:
        temp = dominance_x(i)
        dom_x.append(temp)
    for i in matrix:
        temp = dominance_o(i)
        dom_o.append(temp)

    matrix_transpose = [["", "", ""],
                        ["", "", ""],
                        ["", "", ""]]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_transpose[j][i] = matrix[i][j]

    for i in matrix_transpose:
        temp = dominance_x(i)
        dom_x.append(temp)
    for i in matrix_transpose:
        temp = dominance_o(i)
        dom_o.append(temp)

    diag_1 = []
    diag_2 = []

    for i in range(3):
        for j in range(3):
            if i == j:
                diag_1.append(matrix[i][j])

    for i in range(3):
        for j in range(3):
            if i + j == 2:
                diag_2.append(matrix[i][j])

    temp = dominance_x(diag_1)
    dom_x.append(temp)
    temp = dominance_o(diag_1)
    dom_o.append(temp)

    temp = dominance_x(diag_2)
    dom_x.append(temp)
    temp = dominance_o(diag_2)
    dom_o.append(temp)

    dom_x_final = sum(dom_x)
    dom_o_final = sum(dom_o)

    final_strength = dom_x_final - dom_o_final

    if 100 in dom_x:
        print("The strength of x is 100")
        exit()
    if 100 in dom_o:
        print("The strength of o is 100")
        exit()

    print("dominance of x: ", dom_x)
    print("dominance of o: ", dom_o)

    print("final strength of x: ", final_strength)


def dominance_x(arr):
    if arr.count("x") == 3:
        return 100
    if "o" in arr:
        return 0
    else:
        return arr.count("x")


def dominance_o(arr):
    if arr.count("o") == 3:
        return 100
    if "x" in arr:
        return 0
    else:
        return arr.count("o")


strength(matrix)