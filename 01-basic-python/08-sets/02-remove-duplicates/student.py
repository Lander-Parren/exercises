def remove_duplicates(xs):
    seen = set()
    seen_add = seen.add
    return [x for x in xs if not (x in seen or seen_add(x))]