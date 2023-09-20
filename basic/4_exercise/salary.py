charge_facebook = 150
charge_instagram = 100
charge_reddit = 50



n_open_tabs = int(input())
whole_salary = float(input())

for _ in range(n_open_tabs):
    site = input()
    if site == 'Facebook':
        whole_salary -= charge_facebook
    elif site == 'Instagram':
        whole_salary -= charge_instagram
    elif site == 'Reddit':
        whole_salary -= charge_reddit
    if whole_salary <= 0:
        break



if whole_salary > 0:
    print(f'{int(whole_salary)}')
else:
    print('You have lost your salary.')




