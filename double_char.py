command = input()
double_string = ''
while command != 'End':
    if command =='SoftUni':
        command = input()
        continue
    for word in command:
        double_string += word * 2
    command = input()
    print(double_string)
    double_string = ''


