import math

num_paint_boxes = int(input())
num_rolls_tappet = int(input())
price_per_gloves = float(input())
price_per_brush = float(input())

price_paint_boxes = num_paint_boxes * 21.50
price_rolls = num_rolls_tappet * 5.20
needed_gloves = math.ceil(num_rolls_tappet * 0.35)
price_all_gloves = needed_gloves * price_per_gloves
needed_brush = math.floor(num_paint_boxes * 0.48)
price_all_brush = needed_brush * price_per_brush

total_price = price_paint_boxes + price_rolls + price_all_gloves + price_all_brush
delivery = total_price / 15
print(f"This delivery will cost {delivery:.2f} lv.")