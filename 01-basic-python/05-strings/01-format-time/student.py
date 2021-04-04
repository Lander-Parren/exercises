def format_time(h, m, s):

    def to_string(getal):
        return str(getal).rjust(2, '0')

    h = to_string(h)
    m = to_string(m)
    s = to_string(s)

    return f'{h}:{m}:{s}'