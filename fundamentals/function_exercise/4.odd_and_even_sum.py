# number = input()
# list_even = []
# list_odd = []
# for i in number:
#     if int(i) % 2 == 0:
#         list_even.append(int(i))
#     else:
#         list_odd.append(int(i))
# odd_sum = sum(list_odd)
# even_sum = sum(list_even)
#
# print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

# both decisions are working!

number = input()

def numbers_even_or_odd(a):
    sum_odd = 0
    sum_even = 0
    for i in a:
        if int(i) % 2 == 0:
            sum_even += int(i)
        else:
            sum_odd += int(i)
    return sum_odd, sum_even
final_odd_sum, final_even_sum  = numbers_even_or_odd(number)
print(f"Odd sum = {final_odd_sum}, Even sum = {final_even_sum}")