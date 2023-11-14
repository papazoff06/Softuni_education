
def loading_bar(number):
    percent = 0
    percent += number // 10
    return percent
num = int(input())
final_percent = loading_bar(num)
if num == 100:
    print('100% Complete!')
    print('[%%%%%%%%%%]')
else:
    print(f"{num}% [{final_percent * '%'}{(10 - final_percent) * '.'}]")
    print('Still loading...')