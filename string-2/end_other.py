def end_other(a, b):
    a_lower = a.lower()
    b_lower = b.lower()
    boundary = len(a)

    if a_lower[-boundary::] == b_lower[-boundary::]:
        return True
    return False

    # another answer
    # return a_lower[-len(b)] == b or a == b[-len(a):]


print(end_other('yz', '12xz'))
print(end_other('Z', '12xz'))
# print(end_other('Hiabc', 'abc'))
# print(end_other('AbC', 'HiaBc'))
# print(end_other('abc', 'abXabc'))
