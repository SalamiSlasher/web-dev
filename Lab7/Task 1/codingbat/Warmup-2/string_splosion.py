def string_splosion(str):
    c = []
    for i in xrange(1, len(str)+1):
        c.append(str[:i])
    return "".join(c)
