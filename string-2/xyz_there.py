def xyz_there(str):
    for i in range(len(str)):
        if str[i] == '.' and str[i:i+4] == '.xyz':
            return False
        if str[0:3] != 'xyz':
            return False

    return True


# print(xyz_there('abcxy'))
print(xyz_there('abcxyz'))
# print(xyz_there('xyz.abc'))
# print(xyz_there('abc.xyz'))
# print(xyz_there('xyz.abc'))
