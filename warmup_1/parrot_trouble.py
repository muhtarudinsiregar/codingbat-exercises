def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True

    return False

print(parrot_trouble(False, 24))
