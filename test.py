# import sys
#
# # str = 'E=TX\nX=+TX/ε\nT=FY\nY=*FY/ε\nF=(E)/z'
# # str = 'S=W\nW=ZXY/XY\nY=c/ε\nZ=a/d\nX=Xb/ε'
# str = 'S=aBDh\nB=cC\nC=bC/ε\nD=EF\nE=g/ε\nF=F/ε'
# sys.setrecursionlimit(1500)
# lines = str.splitlines()
# variables = []
# for i in lines:
#     variables.append(i[0])
#
#
# def first(str):
#     input_str = str
#     start = input_str[0]
#     str = start + '=/'
#     str += input_str[input_str.index("=") + 1:]
#     str += '/'
#     first_ls = []
#
#     lst = []
#     for pos, char in enumerate(str):
#         if (char == '/'):
#             lst.append(pos)
#     var = []
#     ter = []
#     for i in range(len(lst) - 1):
#         if str[lst[i] + 1].isupper():
#             var.append(str[lst[i] + 1:lst[i + 1]])
#         else:
#             ter.append(str[lst[i] + 1:lst[i + 1]])
#     for i in ter:
#         first_ls.append(i[0])
#     break_out_flag = False
#     for i in var:
#         while (i):
#             ls = first(lines[variables.index(i[0])])
#             if 'ε' in ls:
#                 ls.remove('ε')
#                 first_ls += ls
#                 i = i[1:]
#             else:
#                 first_ls += ls
#                 break_out_flag = True
#                 break
#         if break_out_flag:
#             break
#         first_ls += 'ε'
#
#     return first_ls
#
#
# for i in range(len(variables)):
#     print('first of ', variables[i], '=', first(lines[i]))

a = '01234'
b = a[0:]
print(b)