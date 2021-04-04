def count_turns(ns):
    teller = 0
    for (x, y, z) in zip(ns, ns[1:], ns[2:]):
        if x < y > z or x > y < z:
            teller += 1
    
    return teller