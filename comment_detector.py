f = open("sample_text.txt")
single_comment_counter = 0
multi_comment_counter = 0
line_counter = -1

lines = f.readlines()



for line in lines:
    line_counter += 1
    if "/*" in line:
        multi_comment_counter += 1
        temp = line_counter + 1
        index = line.index("/*")

        print("there is a multi line comment on line: ", line_counter + 1)
        print("the comment is: ", line[index + 2:].replace("\n", ""))

        while '*/' not in lines[temp]:
            print(lines[temp].replace("\n", ""))
            temp += 1
        index = lines[temp].index("*/")
        print(lines[temp][:index],"\n")

    elif "//" in line:
        single_comment_counter += 1
        print("there is a single line comment on line: ", line_counter + 1)
        index = line.index("//")
        print("the comment is: ", line[index + 2:])

