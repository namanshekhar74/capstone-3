def left_recursion_removal(rule):


    c = 1
    a = ''
    t = []

    for i in range(1):
        a = rule[i]
        t.append(a.split('->'))  # splitting lhs and rhs

    t1 = []
    for i in range(1):
        z = t[i][c]
        t1.append(z.split('|'))  # splitting rhs

    x = []
    for i in range(1):
        x.append(t[i][0])  # storing the lhs of production

    s = []
    s1 = []
    m = 0
    o = 0
    fl = 0
    v = ''
    ch = ""
    for i in range(len(t1)):
        v = x[i]
        for j in range(len(t1[i])):
            ch = t1[i][j]
            if (v != ch[0]):
                s.append(ch)
            else:
                s1.append(ch[1:])
                fl = fl + 1

    b = 0
    if len(rule) == 1:
        print(x[0] + "->", end="")
        for i in range(len(s)):
            print(s[i] + x[0] + "'", end="")
            if (i < len(s) - 1):
                print("|", end="")

        print(" ")

        print(x[0] + "'" + "->", end="")
        for i in range(len(s)):
            print(s1[i] + x[0] + "'", end="")
            if (i < len(s) - 1):
                print("|", end="")
            if (i == len(s) - 1):
                print("|ε")
    else:
        for ds in range(1):
            if (fl >= 1):
                print(x[ds] + "->", end="")

                for i in range(len(s)):
                    h = s[i]
                    k = rule[b]
                    if (k.__contains__(h)):
                        print(s[i] + x[0] + "'", end="")
                        if (i < len(s) - 1):
                            print("|", end="")

                print(" ")

                print(x[0] + "'" + "->", end="")
                for i in range(len(s1)):
                    h = s1[i]
                    k = rule[i]
                    if (k.__contains__(h)):
                        print(s1[i] + x[0] + "'", end="")
                        if (i < len(s1) - 1):
                            print("|", end="")
                        if (i == len(s1) - 1):
                            print("|ε")
                fl = fl - 1
            else:
                print(rule[ds])
# abc(["S->SAa|c"])
n = int(input("please enter no. of production rule: "))
rule = []
for i in range(n):
    rule.append(input("enter the production: "))

for i in rule:
    left_recursion_removal([i])