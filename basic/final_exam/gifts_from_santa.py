
n = int(input())
m = int(input())
s = int(input())
current_address = 0

for address in range(m, n - 1, - 1):
     if address % 3 == 0 and address % 2 ==0:
         current_address = address
         if current_address == s:
             break

         print(current_address, end=' ')

