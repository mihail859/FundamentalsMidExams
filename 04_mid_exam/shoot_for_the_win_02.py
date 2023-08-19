def shoot_the_target(array, idx, shoot_array):
    if idx in range(len(array)):
        target = array[idx]
        shoot_array.append(array[idx])
        array[idx] = - 1
        for i in range(len(array)):
            if array[i] == -1:
                continue
            elif array[i] > target:
                array[i] -= target
            else:
                array[i] += target

    return array


integers_list = [int(x) for x in input().split(' ')]
shoot_count_list = []
while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    integers_list = shoot_the_target(integers_list, index, shoot_count_list)

count = len(shoot_count_list)
integers_list = [str(i) for i in integers_list]
print(f"Shot targets: {count} -> {' '.join(integers_list)}")