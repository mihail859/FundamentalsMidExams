quantity_food = float(input())
quantity_hay = float(input())
quantity_cover = float(input())
weight = float(input())
is_enough = True
quantity_food *= 1000
quantity_hay *= 1000
quantity_cover *= 1000
weight *= 1000

for day in range(1, 31):
    quantity_food -= 300
    if quantity_food <= 0:
        is_enough = False
        break
    if day % 2 == 0:
        quantity_hay -= (0.05 * quantity_food)
        if quantity_hay <= 0:
            is_enough = False
            break
    if day % 3 == 0:
        quantity_cover -= (1/3 * weight)
        if quantity_cover <= 0:
            is_enough = False
            break

if is_enough:
    print(f"Everything is fine! Puppy is happy! "
          f"Food: {(quantity_food / 1000):.2f}, "
          f"Hay: {(quantity_hay / 1000):.2f}, "
          f"Cover: {(quantity_cover / 1000):.2f}.")
else:
    print("Merry must go to the pet store!")
