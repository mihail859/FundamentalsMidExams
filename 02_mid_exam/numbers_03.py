def array_sum(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + array_sum(nums, idx + 1)


input_numbers = [int(x) for x in input().split()]
sum_numbers = array_sum(input_numbers, 0)
average_sum = sum_numbers / len(input_numbers)


final_array = []
new_array = [x for x in input_numbers if x > average_sum]
if new_array:
    new_array.sort(reverse=True)
    length = len(new_array)
    if length > 5:
        for i in range(5):
            final_array.append(new_array[i])
    else:
        for j in range(length):
            final_array.append(new_array[j])
    final_array = [str(x) for x in final_array]
    print(" ".join(final_array))
else:
    print("No")