import copy
def first(rule):
    global rules, nonterm_userdef, \
        term_userdef, diction, firsts

    if len(rule) != 0 and (rule is not None):
        if rule[0] in term_userdef:
            return rule[0]
        elif rule[0] == '#':
            return '#'

    if len(rule) != 0:
        if rule[0] in list(diction.keys()):

            fres = []
            rhs_rules = diction[rule[0]]


            for itr in rhs_rules:
                indivRes = first(itr)
                if type(indivRes) is list:
                    for i in indivRes:
                        fres.append(i)
                else:
                    fres.append(indivRes)


            if '#' not in fres:
                return fres
            else:


                newList = []
                fres.remove('#')
                if len(rule) > 1:
                    ansNew = first(rule[1:])
                    if ansNew != None:
                        if type(ansNew) is list:
                            newList = fres + ansNew
                        else:
                            newList = fres + [ansNew]
                    else:
                        newList = fres
                    return newList


                fres.append('#')
                return fres


def follow(nt):
    global start_symbol, rules, nonterm_userdef, \
        term_userdef, diction, firsts, follows

    solset = set()
    if nt == start_symbol:
        # return '$'
        solset.add('$')


    for curNT in diction:
        rhs = diction[curNT]

        for subrule in rhs:
            if nt in subrule:


                while nt in subrule:
                    index_nt = subrule.index(nt)
                    subrule = subrule[index_nt + 1:]

                    if len(subrule) != 0:


                        res = first(subrule)


                        if '#' in res:
                            newList = []
                            res.remove('#')
                            ansNew = follow(curNT)
                            if ansNew != None:
                                if type(ansNew) is list:
                                    newList = res + ansNew
                                else:
                                    newList = res + [ansNew]
                            else:
                                newList = res
                            res = newList
                    else:
                        if nt != curNT:
                            res = follow(curNT)

                    # add follow result in set form
                    if res is not None:
                        if type(res) is list:
                            for g in res:
                                solset.add(g)
                        else:
                            solset.add(res)
    return list(solset)


def createTable(state_dict, state_map, T, NT):
    global seperated_rule_list, diction

    rows = list(state_dict.keys())
    cols = T + ['$'] + NT

    table = []
    tempRow = []
    for y in range(len(cols)):
        tempRow.append('')
    for x in range(len(rows)):
        table.append(copy.deepcopy(tempRow))

    for entry in state_map:
        state = entry[0]
        symbol = entry[1]
        a = rows.index(state)
        b = cols.index(symbol)
        if symbol in NT:
            table[a][b] = table[a][b] \
                          + f"{state_map[entry]} "
        elif symbol in T:
            table[a][b] = table[a][b] \
                          + f"S{state_map[entry]} "


    numbered = {}
    key_count = 0
    for rule in seperated_rule_list:
        temp_rule = copy.deepcopy(rule)
        temp_rule[1].remove('.')
        numbered[key_count] = temp_rule
        key_count += 1

    addedR = f"{seperated_rule_list[0][0]} -> " \
             f"{seperated_rule_list[0][1][1]}"
    rules.insert(0, addedR)
    for rule in rules:
        k = rule.split("->")
        k[0] = k[0].strip()
        k[1] = k[1].strip()
        rhs = k[1]
        multiple_rhs = rhs.split('|')

        for i in range(len(multiple_rhs)):
            multiple_rhs[i] = multiple_rhs[i].strip()
            multiple_rhs[i] = multiple_rhs[i].split()
        diction[k[0]] = multiple_rhs

    for atate_number in state_dict:
        for rule in state_dict[atate_number]:
            if rule[1][-1] == '.':

                temp2 = copy.deepcopy(rule)
                temp2[1].remove('.')
                for key in numbered:
                    if numbered[key] == temp2:

                        follow_result = follow(rule[0])
                        for col in follow_result:
                            index = cols.index(col)
                            if key == 0:
                                table[atate_number][index] = "Accepted"
                            else:
                                table[atate_number][index] = \
                                    table[atate_number][index] + f"R{key} "

    print("SLR(1) parsing table final:\n")
    frmt = "{:>8}" * len(cols)
    print("  ", frmt.format(*cols), "\n")
    ptr = 0
    j = 0
    for y in table:
        frmt1 = "{:>8}" * len(y)
        print(f"{{:>3}} {frmt1.format(*y)}"
              .format('I' + str(j)))
        j += 1



a= {0: [["E'", ['.', 'E']], ['E', ['.', 'E', '+', 'T']], ['E', ['.', 'T']], ['T', ['.', 'T', '*', 'F']], ['T', ['.', 'F']], ['F', ['.', '(', 'E', ')']], ['F', ['.', 'id']]], 1: [["E'", ['E', '.']], ['E', ['E', '.', '+', 'T']]], 2: [['E', ['T', '.']], ['T', ['T', '.', '*', 'F']]], 3: [['T', ['F', '.']]], 4: [['F', ['(', '.', 'E', ')']], ['E', ['.', 'E', '+', 'T']], ['E', ['.', 'T']], ['T', ['.', 'T', '*', 'F']], ['T', ['.', 'F']], ['F', ['.', '(', 'E', ')']], ['F', ['.', 'id']]], 5: [['F', ['id', '.']]], 6: [['E', ['E', '+', '.', 'T']], ['T', ['.', 'T', '*', 'F']], ['T', ['.', 'F']], ['F', ['.', '(', 'E', ')']], ['F', ['.', 'id']]], 7: [['T', ['T', '*', '.', 'F']], ['F', ['.', '(', 'E', ')']], ['F', ['.', 'id']]], 8: [['F', ['(', 'E', '.', ')']], ['E', ['E', '.', '+', 'T']]], 9: [['E', ['E', '+', 'T', '.']], ['T', ['T', '.', '*', 'F']]], 10: [['T', ['T', '*', 'F', '.']]], 11: [['F', ['(', 'E', ')', '.']]]}

b= {(0, 'E'): 1, (0, 'T'): 2, (0, 'F'): 3, (0, '('): 4, (0, 'id'): 5, (1, '+'): 6, (2, '*'): 7, (4, 'E'): 8, (4, 'T'): 2, (4, 'F'): 3, (4, '('): 4, (4, 'id'): 5, (6, 'T'): 9, (6, 'F'): 3, (6, '('): 4, (6, 'id'): 5, (7, 'F'): 10, (7, '('): 4, (7, 'id'): 5, (8, ')'): 11, (8, '+'): 6, (9, '*'): 7}

c= ['id', '+', '*', '(', ')']

d= ['E', 'T', 'F']

createTable(a,b,c,d)