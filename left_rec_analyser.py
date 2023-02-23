def remove_left_recursion(start, rec, non_rec):
    new = start + "'"
    epsilon = 'epsilon'
    final_1 = start + '='
    final_2 = new + '='
    for i in rec:
        final_1 += i[1:]
        final_1 += new
        final_1 += '/'
    for i in non_rec:
        final_2 += i
        final_2 += new
        final_2 += '/'
    final_2 += epsilon
    final_1 = final_1[:-1]
    return final_1, final_2

def left_rec(str):
    input_str = str
    start = input_str[0]
    str = start + '=/'
    str += input_str[input_str.index("=")+1:]
    str +='/'
    
    lst = []
    for pos,char in enumerate(str):
        if(char == '/'):
            lst.append(pos)
    
    
    
    rec = []
    non_rec = []
    
    for i in range(len(lst) - 1):
        if str[lst[i]+1] == start:
            temp = str[lst[i]+1:lst[i+1]]
            rec.append(temp)
        else:
            temp = str[lst[i]+1:lst[i+1]]
            non_rec.append(temp)
    
    
    if(len(rec) == 0):
        print("There is no left recursion in this line")
    else:
        l = remove_left_recursion(start, rec, non_rec)
        
        for i in l:
            print(i)


list = []

number = int(input('please enter the number of lines: '))

print('please enter the gramar: ')
for i in range(number):
    list.append(input())
for i in list:
    left_rec(i)