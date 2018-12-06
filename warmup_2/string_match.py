def string_match(a, b):
    final_list = []
    if len(a) == 0:
        return 0

    for i in range(0, len(a)-1):
        if a[i:i+2] in b and a[i:i+2] not in final_list:
            final_list.append(a[i:i+2])
    return len(final_list)

    # solution from codingbat
    # Figure which string is shorter.
    # shorter = min(len(a), len(b))
    # count = 0

    # Loop i over every substring starting spot.
    # Use length-1 here, so can use char str[i+1] in the loop
    # for i in range(shorter-1):
    #     a_sub = a[i:i+2]
    #     b_sub = b[i:i+2]
    #         if a_sub == b_sub:
    #             count = count + 1

    # return count

# print(string_match('xxcaazz', 'xxbaaz'))
# print(string_match('abc', 'abc'))
print(string_match('aabbccdd', 'abbbxxd'))
print(string_match('aaxxaaxx', 'iaxxai'))
