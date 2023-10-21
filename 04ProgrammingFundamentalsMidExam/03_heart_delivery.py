def jump(neighborhood_houses, idx):
    if neighborhood_houses[idx] == 0:
        print(f"Place {idx} already had Valentine's day.")
    else:
        neighborhood_houses[idx] -= 2
        if neighborhood_houses[idx] == 0:
            print(f"Place {idx} has Valentine's day.")
    return neighborhood_houses


neighborhood = [int(x) for x in input().split("@")]
position = 0
while True:
    command, *params = input().split()
    if command == 'Love!':
        break
    elif command == 'Jump':
        jump_score = int(params[0])
        position += jump_score
        if position not in range(len(neighborhood)):
            position = 0
        neighborhood = jump(neighborhood, position)

print(f"Cupid's last position was {position}.")
failed = [x for x in neighborhood if x != 0]
if failed:
    failed = [x for x in neighborhood if x != 0]
    print(f"Cupid has failed {len(failed)} places.")
else:
    print("Mission was successful.")