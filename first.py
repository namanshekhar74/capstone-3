str = 'E=TX\nX=+TX/ε\nT=FY\nY=*FY/ε\nF=(E)/z'
# str = 'S=W\nW=ZXY/XY\nY=c/ε\nZ=a/d\nX=Xb/ε'
# str = 'S=aBDh\nB=cC\nC=bC/ε\nD=EF\nE=g/ε\nF=F/ε'

lines = str.splitlines()
variables = []
rhs = []
rhs_with_slash = []
for i in lines:
    index = i.index('=')
    rhs_with_slash.append(i[index+1:])

for i in lines:
    index = i.index('=')
    t = i[index + 1:].split('/')
    for j in t:
        rhs.append(j)
for i in lines:
    variables.append(i[0])
start_symbol = variables[0]
print('rhs:', rhs)
print(rhs_with_slash)


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
        if index_var + 1 < len(i):
            temp_next = i[i.index(next) + 1]
            if temp_next.isupper():
                temp.remove('ε')
                epsilon_resolution(variable, i, temp_next)
            else:
                temp.append(temp_next)
    return temp


def follow(variable, rhs_fn, start_symbol, rhs_with_slash):
    follow_list = []
    if variable == start_symbol:
        follow_list.append('$')
    for i in rhs_fn:
        # print('var: ',variable)
        # print(i)
        if variable in i:
            index_var = i.index(variable)

            if index_var == len(i)-1:
                temp_string_eq = [string for string in rhs_with_slash if i in string]
                temp_index = rhs_with_slash.index(temp_string_eq[0])
                if len(follow_all)>temp_index:
                    follow_list += follow_all[temp_index]
            if index_var + 1 < len(i):
                next = i[index_var + 1]
                if next.isupper():
                    received = epsilon_resolution(variable, i, next,rhs_with_slash)
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
    # print('variables: ', variables[i])
    follow_temp = follow(variables[i], rhs, start_symbol, rhs_with_slash)
    print('follow of ', variables[i], '=', follow_temp)
    follow_all.append(follow_temp)
print('follall: ', follow_all)
