def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result += str[:i+1]
        print(str[:i+1])
        print(i)
    return result

print(string_splosion("Code"))
