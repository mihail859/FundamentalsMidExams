def urgent_function(shopping_list, item):
    if item not in shopping_list:
        shopping_list.insert(0, item)
    return shopping_list


def unnecessary_function(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
    return shopping_list


def correct_function(shopping_list, old, new):
    if old in shopping_list:
        old_index = shopping_list.index(old)
        shopping_list.pop(old_index)
        shopping_list.insert(old_index, new)
    return shopping_list


def rearrange_shopping_list(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        shopping_list.append(item)
    return shopping_list


initial_list_of_products = input().split("!")
while True:
    command = input()
    if command == "Go Shopping!":
        break
    split_command = command.split()
    if split_command[0] == 'Urgent':
        item_to_add = split_command[1]
        initial_list_of_products = urgent_function(initial_list_of_products, item_to_add)
    elif split_command[0] == 'Unnecessary':
        item_to_remove = split_command[1]
        initial_list_of_products = unnecessary_function(initial_list_of_products, item_to_remove)
    elif split_command[0] == 'Correct':
        old_item = split_command[1]
        new_item = split_command[2]
        initial_list_of_products = correct_function(initial_list_of_products, old_item, new_item)
    elif split_command[0] == 'Rearrange':
        item_to_rearrange = split_command[1]
        initial_list_of_products = rearrange_shopping_list(initial_list_of_products, item_to_rearrange)

print(", ".join(initial_list_of_products))