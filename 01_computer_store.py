price_without_taxes = 0
taxes = 0


while True:
    command = input()
    if command == "special" or command == "regular":
        break
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
        continue
    taxes += 0.20 * current_price
    price_without_taxes += current_price

if price_without_taxes == 0:
    print("Invalid order!")
else:
    total_price = price_without_taxes + taxes
    if command == "special":
        total_price *= 0.90
    print(f"""Congratulations you've just bought a new computer!
Price without taxes: {price_without_taxes:.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {total_price:.2f}$""")
