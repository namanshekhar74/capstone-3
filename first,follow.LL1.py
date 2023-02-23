from curses.ascii import isupper
from matplotlib.table import Table
from sympy import TableForm

import pandas
from tabulate import tabulate

str = 'E=TX\nX=+TX/ε\nT=FY\nY=*FY/ε\nF=(E)/z'
# str = 'S=aBDh\nB=cC\nC=bC/ε\nD=EF\nE=g/ε\nF=f/ε'

lines = str.splitlines()
variables = []
rhs = []
rhs_with_slash = []
for i in lines:
    index = i.index('=')
    rhs_with_slash.append(i[index + 1:])

for i in lines:
    index = i.index('=')
    t = i[index + 1:].split('/')
    for j in t:
        rhs.append(j)
for i in lines:
    variables.append(i[0])
start_symbol = variables[0]


def first(str):
    input_str = str
    start = input_str[0]
    str = start + '=/'
    str += input_str[input_str.index("=") + 1:]
    str += '/'
    first_ls = []

    lst = []
    for pos, char in enumerate(str):
        if (char == '/'):
            lst.append(pos)
    var = []
    ter = []
    for i in range(len(lst) - 1):
        if str[lst[i] + 1].isupper():
            var.append(str[lst[i] + 1:lst[i + 1]])
        else:
            ter.append(str[lst[i] + 1:lst[i + 1]])
    for i in ter:
        first_ls.append(i[0])
    break_out_flag = False
    for i in var:
        while (i):
            ls = first(lines[variables.index(i[0])])
            if 'ε' in ls:

                ls.remove('ε')
                first_ls += ls
                i = i[1:]
            else:
                first_ls += ls
                break_out_flag = True
                break
        if break_out_flag:
            break
        first_ls += 'ε'

    return first_ls


first_list = []
for i in range(len(variables)):
    a = first(lines[i])
    first_list.append(a)
    print('first of ', variables[i], '=', a)


def epsilon_resolution(variable, i, next, rhs_with_slash):
    temp = first_list[variables.index(next)]
    if 'ε' in temp:

        index_var = i.index(next) + 1
        if index_var < len(i):
            temp_next = i[i.index(next) + 1]
            if temp_next.isupper():
                temp.remove('ε')
                epsilon_resolution(variable, i, temp_next)
            else:
                temp.remove('ε')
                temp.append(temp_next)
    return temp


def follow(variable, rhs_fn, start_symbol, rhs_with_slash):
    follow_list = []
    if variable == start_symbol:
        follow_list.append('$')
    for i in rhs_fn:
        if variable in i:
            index_var = i.index(variable)

            if index_var == len(i) - 1:
                temp_string_eq = [string for string in rhs_with_slash if i in string]
                temp_index = rhs_with_slash.index(temp_string_eq[0])
                if len(follow_all) > temp_index:
                    follow_list += follow_all[temp_index]
            if index_var + 1 < len(i):
                next = i[index_var + 1]
                if next.isupper():
                    received = epsilon_resolution(variable, i, next, rhs_with_slash)
                    follow_list += received
                else:
                    follow_list += next
        if 'ε' in follow_list:
            follow_list.remove('ε')
            temp_string_eq = [string for string in rhs_with_slash if i in string]
            temp_index = rhs_with_slash.index(temp_string_eq[0])
            if len(follow_all) > temp_index:
                follow_list += follow_all[temp_index]

    return list(set(follow_list))


follow_all = []
for i in range(len(variables)):
    follow_temp = follow(variables[i], rhs, start_symbol, rhs_with_slash)
    print('follow of ', variables[i], '=', follow_temp)
    follow_all.append(follow_temp)

list_of_ter = []
forbidden = ['/', '=', '\n', 'ε']
for i in str:
    if i.isupper() or i in forbidden:
        pass
    else:
        list_of_ter.append(i)
list_of_ter.append('$')


def table_for_var(str):
    input_str = str
    start = input_str[0]
    str = start + '=/'
    str += input_str[input_str.index("=") + 1:]
    str += '/'
    variable_table_row = ["-"] * len(list_of_ter)
    lst = []
    for pos, char in enumerate(str):
        if (char == '/'):
            lst.append(pos)
    productions = []

    for i in range(len(lst) - 1):
        productions.append(str[lst[i] + 1:lst[i + 1]])

    for i in productions:
        if i[0].isupper():
            temp_index = variables.index(i[0])
            temp_first_list = first_list[temp_index]
            for j in temp_first_list:
                if j == 'ε':
                    temp_follow = follow_all[variables.index(start)]
                    for k in temp_follow:
                        index_table = list_of_ter.index(k)
                        variable_table_row[index_table] = start + '=' + i

                else:
                    index_table = list_of_ter.index(j)
                    variable_table_row[index_table] = start + '=' + i

        elif i[0] == 'ε':
            temp_follow = follow_all[variables.index(start)]
            for j in temp_follow:
                index_table = list_of_ter.index(j)
                variable_table_row[index_table] = start + '=' + i
        else:
            temp_index = list_of_ter.index(i[0])
            variable_table_row[temp_index] = start + '=' + i
    return variable_table_row


table = []
for i in lines:
    table.append(table_for_var(i))
print()
print("LL(1) table:")
df = pandas.DataFrame(table, variables, list_of_ter)
print(tabulate(df, headers='keys', tablefmt='psql'))
w = 'z+z+z$'
input_str = []
for i in w:
    input_str.append(i)
stack = []
stack.append('$')
stack.append(start_symbol)

def parsing(stack, input_string, pointer):
    x = stack[-1]
    a = input_string[pointer]
    if x.isupper():
        i = variables.index(x)
        j = list_of_ter.index(a)
        temp = table[i][j]
        if temp == '-':
            print("error")

        else:
            equals_index = temp.index('=')
            temp = temp[equals_index + 1:]
            temp = temp[::-1]
            if temp == 'ε':
                stack.pop()
                parsing(stack, input_string, pointer)
            else:
                stack.pop()
                for k in temp:
                    stack.append(k)
                print(stack)
                parsing(stack, input_string, pointer)

    else:
        if x == a == "$":
            print("parsing done successfully!")
        elif x == a != '$':
            stack.pop()

            pointer += 1
            print(stack)
            parsing(stack, input_string, pointer)

print("stack contents on parsing:")
parsing(stack, input_str, 0)
