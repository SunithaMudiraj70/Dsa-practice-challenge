'''
You start with a certain amount of experience. There are several monsters, and each monster has:
- power[i]: the minimum experience needed to defeat it.
- bonus[i]: the experience you gain after defeating it.
You can defeat a monster only if your current experience is at least its power. After defeating it, you gain its bonus.

Goal: Defeat the maximum possible number of monsters. You may choose the order in which you fight them.'''

experience = 50
power = [70, 40, 55, 90]
bonus = [100, 5, 20, 200]

monsters = sorted(zip(power, bonus))

count = 0

for power_required, bonus_gained in monsters:
    if experience < power_required:
        break
    else:
        experience+=power_required
        count+=1

print(count)