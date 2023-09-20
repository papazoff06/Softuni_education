bitcoin = 1168
dollar = 1.76
euro = 1.95
ioan = dollar * 0.15


bitcoin_count = int(input())
ioans_count = float(input())
comissiong = float(input())

whole_sum = (bitcoin_count * bitcoin) + (ioans_count * ioan)
whole_sum_with_comissiong = (whole_sum - (whole_sum * comissiong / 100)) / euro
print(f'{whole_sum_with_comissiong:.2f}')


