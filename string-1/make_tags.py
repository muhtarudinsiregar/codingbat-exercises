def make_tags(tag, word):
    tag_open = "<"+tag+">"
    tag_close = "</"+tag+">"

    return tag_open+word+tag_close


print(make_tags("body", "Hearth"))
