import math
paint_boxes_count = int(input())
tapets_count = int(input())
gloves_price = float(input())
brash_price = float(input())

paint_price = 21.50
tapets_price = 5.20

gloves_count = math.ceil(tapets_count * 0.35)
brashes_count = math.floor(paint_boxes_count * 0.48)

delivery =(paint_boxes_count * paint_price) \
          + (tapets_count * tapets_price) \
          + (gloves_price * gloves_count) \
          + (brashes_count * brash_price)
final_delivery = delivery / 15
print(f"This delivery will cost {final_delivery:.2f} lv.")