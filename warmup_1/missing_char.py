def missing_char(str, n):
    return str[:n] + str[1+n:]


print(missing_char('kitten', 4))
