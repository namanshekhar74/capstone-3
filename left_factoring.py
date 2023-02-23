def common_start(sa, sb):
    def _iter():
        for a, b in zip(sa, sb):
            if a == b:
                yield a
            else:
                return

    return ''.join(_iter())


def lef_factoring_string(beta, diff, start, minimum):
    new = start + "'"
    final1 = start + '=' + minimum + new
    final2 = new + '='

    for i in diff:
        final1 += '/'
        final1 += i
    for i in beta:
        final2 += i
        final2 += '/'

    final2 = final2[:-1]

    return final1, final2


def left_factoring(str):
    input_str = str
    start = input_str[0]
    str = start + '=/'
    str += input_str[input_str.index("=") + 1:]
    str += '/'

    lst = []
    for pos, char in enumerate(str):
        if (char == '/'):
            lst.append(pos)
    list = []
    for i in range(len(lst) - 1):
        temp = str[lst[i] + 1:lst[i + 1]]
        list.append(temp)

    print(list)
    result = min(list, key=len)

    minimum = []

    for i in list:
        if len(i) == len(result):
            minimum.append(i)
    print(minimum)

    beta = [[] for i in range(len(minimum))]
    diff = [[] for i in range(len(minimum))]

    for i in range(len(minimum)):
        for j in list:
            if common_start(minimum[i], j):
                length = len(minimum[i])
                temp = j[length:]
                if len(temp):
                    beta[i].append(j[length:])
            else:
                diff[i].append(j)
    print(beta, diff)

    for i in range(len(minimum)):
        if beta[i]:
            answer = lef_factoring_string(beta[i], diff[i], start, minimum[i])
            for i in answer:
                print(i)


left_factoring(input('please enter the string: '))
