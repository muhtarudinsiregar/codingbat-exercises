def first_two(str):
    if len(str) <= 2 or str == "":
        return str or ""
    return str[:2]

print(first_two("ge"))
print(first_two(""))
print(first_two("hello"))
