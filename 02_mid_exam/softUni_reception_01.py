employees_dict = {}
employees = ["first", "second","third"]
for i in range(3):
    employee_efficiency = int(input())
    employees_dict[employees[i]] = employee_efficiency


norm = 0
for value in employees_dict.values():
    norm += value

time_need = 0
students_count = int(input())

while students_count > 0:
    time_need += 1
    if time_need % 4 == 0:
        continue
    if students_count >= norm:
        students_count -= norm
    else:
        students_count = 0

print(f"Time needed: {time_need}h.")