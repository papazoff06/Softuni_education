# •	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# •	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# •	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# •	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

training_fee = int(input())

basketball_shoes = training_fee * 0.60
basketball_suit = basketball_shoes * 0.80
basketball_ball = basketball_suit * 0.25
basketball_staff = basketball_ball * 0.20

basketball_expense = training_fee + basketball_shoes + basketball_suit + basketball_ball + basketball_staff
print(basketball_expense)

