input_line = [x for x in input().split(' ') if x != ""]
number_of_moves = 0

while True:
    command = input()
    if command == "end":
        break

    split_command = command.split(' ')
    first_idx = int(split_command[0])
    second_idx = int(split_command[1])

    number_of_moves += 1
    if first_idx == second_idx or (first_idx not in range(0, len(input_line))) or \
            (second_idx not in range(0, len(input_line))):

        middle_idx = len(input_line) // 2
        input_line.insert(middle_idx, f"-{number_of_moves}a")
        input_line.insert(middle_idx + 1, f"-{number_of_moves}a")
        print("Invalid input! Adding additional elements to the board")
    else:
        first_element = input_line[first_idx]
        second_element = input_line[second_idx]
        if first_element == second_element:
            input_line.pop(first_idx)
            sec_idx_to_remove = input_line.index(second_element)
            input_line.pop(sec_idx_to_remove)
            print(f"Congrats! You have found matching elements - {first_element}!")
        else:
            print("Try again!")
    if not input_line:
        print(f"You have won in {number_of_moves} turns!")
        break

if input_line:
    print("Sorry you lose :(")
    result = " ".join(input_line)
    print(result)
