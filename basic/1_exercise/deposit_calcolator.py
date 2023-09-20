deposit_sum = float(input())
deposit_term = int(input())
interest = float(input()) / 100
sum = deposit_sum + deposit_term * ((deposit_sum * interest / 12))
print(sum)