#Напишете програма, която пресмята нужните разходи за закупуването на храна за кучета и котки.
# Храната се пазарува от зоомагазин, като една опаковка храна за кучета е на цена 2.50 лв,
# а опаковка храна за котки струва 4 лв.
#Вход
#От конзолата се четат 2 реда:
#1.	Броят на опаковките храна за кучета – цяло число в интервала [0… 100]
#2.	Броят на опаковките храна за котки –  цяло число в интервала [0… 100]
#Изход
#На конзолата се отпечатва:
#"{крайната сума} lv."

dog_count = int(input())
cat_count = int(input())
dog_pacage = dog_count * 2.5
cat_pacage = cat_count * 4
food_price = dog_pacage + cat_pacage
print(f'{food_price} lv.' )