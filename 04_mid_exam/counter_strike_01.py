initial_energy = int(input())
won_counter = 0
battle = 1
is_finnish = False
while True:
    distance = input()
    if distance == "End of battle":
        break
    distance = int(distance)

    if initial_energy - distance >= 0:
        initial_energy -= distance
        won_counter += 1
        if won_counter % 3 == 0:
            initial_energy += won_counter
    else:
        is_finnish = True
        break




if is_finnish:
    print(f"Not enough energy! Game ends with {won_counter} won battles and {initial_energy} energy")
else:
    print(f"Won battles: {won_counter}. Energy left: {initial_energy}")