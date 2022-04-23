ages = [29, 19, 17, 26, 32, 16, 21]
print(ages)
print(ages[4])
print(ages[-2])
print(ages[2:6])
print(ages[:4])
is_17 = 17 in ages
print(is_17)
is_42 = 42 in ages
print(is_42)
ages[2]=18
print(ages)
temp = 32
ages[4] = 26
ages[3] = temp
print(ages)
ages.append(45)
ages.insert(0, 32)
ages.insert(5, 37)
print(ages)
ages.pop()
ages.pop(2)
print(ages)
