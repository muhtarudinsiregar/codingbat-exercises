def cigar_party(cigars, is_weekend):
    if is_weekend and (cigars >= 40):
        return True

    if not is_weekend and cigars >= 40 and cigars <= 60:
        return True

    return False

    # or another answer
    # if is_weekend:
    #     return cigars >= 40
    # return 40 <= cigars <= 60

print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))
print(cigar_party(39, True))
