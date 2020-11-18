#!/usr/bin/python3
# clean.py


def py_template(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for l in range(len(lines)):
        if '=' in lines[l].split('#', 1)[0]:
            if lines[l].strip().endswith('*'):
                lines[l] = lines[l][:-2] + '\n' if lines[l].endswith('\n') else lines[l][:-1]
                continue

            v = eval(lines[l].split('=', 1)[1])
            if type(v) == int:
                lines[l] = lines[l].replace(str(v), '0', 1)
            elif type(v) == bool:
                lines[l] = lines[l].replace(str(v), 'False', 1)
            else:
                lines[l] = lines[l].replace(str(v), '', 1)

    with open(filename + '.sample', 'w') as file:
        file.writelines(lines)
