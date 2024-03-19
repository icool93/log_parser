filename = 'LOG_2023-03-26.log'

with open(filename, 'r') as myfile:
    for line in myfile:

        if 'Signal' in line:
            splitted_line = line.split()
            print(splitted_line)