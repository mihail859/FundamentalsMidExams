peoples = int(input())
lift_state = [int(x) for x in input().split(" ")]

for i in range(len(lift_state)):
    can_load = min(4 - lift_state[i], peoples)
    lift_state[i] += can_load
    peoples -= can_load

if peoples > 0:
    print(f"There isn't enough space! {peoples} people in a queue!")

elif len([state for state in lift_state if state<4])>0:
    print("The lift has empty spots!")

final_lift = [str(state1) for state1 in lift_state]
print(" ".join(final_lift))
