import math
itens_number = int(input("Enter the number of items: "))
number_per_box = int(input("Enter the number of items per box: "))
boxes = math.ceil(itens_number / number_per_box)
print(f"For {itens_number} items, packing {number_per_box} items in each box, you will need {boxes} boxes.")