tic = [['X', '', ''],
       ['', 'X', ''],
       ['O', '', '']]

for i in tic:
    print(i)

def cal_strangth(arr):
    #Rows
    x_strength = []
    o_strength = []
    # for i in arr:
    #     x_strength.append(i.count('X') - i.count('O'))
    #     o_strength.append(i.count('O') - i.count('X'))

    # Colomns
    size = 3
    # col = []
    for i in range(size):
        temp = []
        x_strength.append(arr[i].count('X') - arr[i].count('O'))
        o_strength.append(arr[i].count('O') - arr[i].count('X'))
        for j in range(size):
            temp.append(arr[j][i])
            x_strength.append(temp.count('X') - temp.count('O'))
            o_strength.append(temp.count('O') - temp.count('X'))

        # Diagonals
        diag = []
        rev_diag  = []
        # for i in range(size):
        diag.append(arr[i][i])
        rev_diag.append(arr[i][size-1])

        x_strength.append(diag.count('X') - diag.count('O'))
        o_strength.append(diag.count('O') - diag.count('X'))
        x_strength.append(rev_diag.count('X') - rev_diag.count('O'))
        o_strength.append(rev_diag.count('O') - rev_diag.count('X'))

    return sum([0 if x < 0 else x for x in x_strength]) - sum([0 if x < 0 else x for x in o_strength])



print('Strength',cal_strangth(tic))
