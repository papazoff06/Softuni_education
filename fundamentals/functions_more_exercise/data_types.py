def data_type(data: str, number: str):
    if data == 'int':
        current_number = int(number) * 2
        return current_number
    elif data == 'real':
        current_number = f'{float(number) * 1.5:.2f}'
        return current_number
    elif data == 'string':
        current_number = f"${number}$"
        return  current_number


data_string = input()
int_number = input()

result = data_type(data_string, int_number)
print(result)