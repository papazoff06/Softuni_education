def perfect_number(number):
    sum_numbers = 0
    for i in range(1, number):
        if number % i == 0:
            sum_numbers += i
    result = sum_numbers
    return result
commen_number = int(input())
final_result = perfect_number(commen_number)
if commen_number == final_result:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
