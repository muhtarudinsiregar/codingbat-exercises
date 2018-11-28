def not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        return str[0:]

    return "not "+str

print(not_string("not is"))
