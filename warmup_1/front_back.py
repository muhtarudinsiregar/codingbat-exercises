def front_back(str):
    if len(str) > 1:
        return str[-1:]+str[1:-1]+str[:1]
    return str



print(front_back('ab'))
print(front_back('a'))
print(front_back('code'))
