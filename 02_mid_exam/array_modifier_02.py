def swap_function(array, idx1, idx2):
    array[idx1], array[idx2] = array[idx2], array[idx1]
    return array


def multiply_function(array, idx1, idx2):
    result = array[idx1] * array[idx2]
    array[idx1] = result
    return array


def decrease_function(array):
    array = [x-1 for x in array]
    return array


array_integers = [int(x) for x in input().split()]
while True:
    command, *params = input().split()
    if command == "end":
        break

    # •	"swap {index1} {index2}"
    if command == "swap":
        index1 = int(params[0])
        index2 = int(params[1])
        array_integers = swap_function(array_integers, index1, index2)

    # "multiply {index1} {index2}"
    elif command == "multiply":
        index1 = int(params[0])
        index2 = int(params[1])
        array_integers = multiply_function(array_integers, index1, index2)

    elif command == "decrease":
        array_integers = decrease_function(array_integers)


array_integers = [str(x) for x in array_integers]
print(", ".join(array_integers))