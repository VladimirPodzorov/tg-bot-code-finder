def check(string):
    res = ''
    for sym in string:
        if sym == ',':
            break
        res += sym
    return res
