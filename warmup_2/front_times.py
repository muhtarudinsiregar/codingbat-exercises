def front_times(str, n):
    result = ""
    for i in range(n):
        result += str[:3]
    return result

print(front_times('Chocolate', 3))
