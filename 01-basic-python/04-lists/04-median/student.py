def median(ns):
    arr = sorted(ns)
    l = len(arr) // 2
    if len(arr) % 2 == 0:
        return (arr[l - 1] + arr[l]) / 2
    else:
        return arr[l]