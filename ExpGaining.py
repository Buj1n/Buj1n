needed_exp = float(input())
count_of_battles = int(input())
colected_exp = 0
counter = 0

for exp in range(1, count_of_battles + 1):
    exp_per_battle = float(input())
    counter += 1
    current_exp = exp_per_battle

    if counter % 3 == 0:
        one = exp_per_battle * 0.15
        current_exp = exp_per_battle + one
    elif counter % 5 == 0:
        two = exp_per_battle * 0.10
        current_exp = exp_per_battle - two
    elif counter % 15 == 0:
        three = exp_per_battle * 0.05
        current_exp = exp_per_battle + three

    colected_exp = colected_exp + current_exp

    if colected_exp >= needed_exp:
        print(f"Player successfully collected his needed experience for {counter} battles.")
        break
miss_exp = needed_exp - colected_exp
if colected_exp < needed_exp:
    print(f"Player was not able to collect the needed experience, {miss_exp:.2f} more needed. ")