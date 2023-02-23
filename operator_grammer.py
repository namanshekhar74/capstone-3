import pandas
from tabulate import tabulate

str = 'E=E+T/T*E/z'

lines = str.splitlines()

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


def check_operator_gramer(str):
    bool = True
    for i in range(len(str) - 1):
        if str[i].isupper() and str[i + 1].isupper():
            bool = False
    return bool


temp_bool = True
for i in rhs:
    temp_bool = check_operator_gramer(i)
    if temp_bool == False:
        print("the given grammer is not an operator precedence grammer! ")
        exit()
if temp_bool:
    print("the given gramer is an operator precedence grammer ")

precedence = ['$']


def associativity(str, start):
    operator = ''
    for i in str:
        if not i.isupper():
            operator += i
    operator_index = str.index(operator)
    precedence.append(operator)

    if operator == str:
        return
    else:
        if str[operator_index - 1] == start:
            return "left"
        elif str[operator_index + 1] == start:
            return "right"
        else:
            print("enter an unambiguous grammer")
            return "error"

asso = ["None"]
for i in (rhs_with_slash):
    index_var = rhs_with_slash.index(i)
    t = i.split('/')
    for j in t:
        asso.append(associativity(j, variables[index_var]))
asso.append("None")
length = len(precedence)
precedence_table = [['' for _ in range(length)] for _ in range(length)]
for i in range (length):
    for j in range (length):
        if i == 0 and j == 0:
            precedence_table[i][j] = "-"
        if i == length - 1 and j== length -1:
            precedence_table[i][j] = "-"
        elif i == j:
            if asso[i] == "left":
                precedence_table[i][j] = ">"
            elif asso[i] == "right":
                precedence_table[i][j] = "<"
        else:
            if precedence.index(precedence[i]) > precedence.index(precedence[j]):
                precedence_table[i][j] = ">"
            else:
                precedence_table[i][j] = "<"

print("The operator precedence table is: ")
df = pandas.DataFrame(precedence_table, precedence, precedence)
print(tabulate(df, headers='keys', tablefmt='psql'))