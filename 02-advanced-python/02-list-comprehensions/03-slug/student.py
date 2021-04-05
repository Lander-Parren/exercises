def slug(string):
    names = string.split(' ')
    first = names[0]
    last = names[1:]
    return '-'.join(x.lower() for x in last + [first])