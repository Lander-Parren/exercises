def format_grades(grades):
    return '\n'.join(f'{name}: {average(grades)}' for name, grades in grades.items())

def average(lst):
    return round(sum(lst) / len(lst))