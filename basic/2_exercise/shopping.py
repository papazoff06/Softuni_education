
VIDEO_CARD_PRICE = 250
# •	Видеокарта – 250 лв./бр.
# •	Процесор – 35% от цената на закупените видеокарти/бр.
# •	Рам памет – 10% от цената на закупените видеокарти/бр.
#
#

piters_budget = float(input())
count_video_card = int(input())
count_processors = int(input())
count_ram = int(input())

whole_price = (count_video_card * VIDEO_CARD_PRICE) + \
              (count_processors * (count_video_card * VIDEO_CARD_PRICE) * 0.35) + \
              (count_ram * (count_video_card * VIDEO_CARD_PRICE) * 0.10)
if count_video_card > count_processors:
    whole_price *= 0.85
if piters_budget >= whole_price:
    print(f'You have {piters_budget - whole_price:.2f} leva left!')
else:
    print(f'Not enough money! You need {whole_price - piters_budget:.2f} leva more!')