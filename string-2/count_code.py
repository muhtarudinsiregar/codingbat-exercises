def count_code(str):
    count = 0
    for i in range(len(str)):
        string = str[i:i+4]
        if string == 'code' or incomplete_code(string):
            count += 1
    return count

    # or another answer
    # if str[i:i+2] == 'co' and string[3] == 'e':
    #   count += 1


def incomplete_code(string):
    if len(string) == 4:
        return string[0] == 'c' and string[1] == 'o' and string[3] == 'e'
    return False


# print(count_code('aaacodebbb'))
# print(count_code('codexxcode'))
print(count_code('cozexxcope'))
