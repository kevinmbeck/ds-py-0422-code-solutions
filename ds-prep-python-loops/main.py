record = ("1", "Grimdiana", "Bones", "boulders")
row = ""
for x in record:
  row = (row + x + ",")
  print(row)
values_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]
for x in values_list:
  print(x)
index_list = [ ]
for i in range(len(values_list)):
  index_list.insert(0, i)
  print(index_list)
for i in index_list:
  if i%2 > 0:
    del values_list[i]
  print(values_list)
vowels = {"A", "E", "I", "O", "U"}
parts_of_the_big_letter = {"L", "M", "N", "O", "P"}
for x in vowels:
  parts_of_the_big_letter.discard(x)
print(parts_of_the_big_letter)
player_positions = {
    "Who": "1B",
    "What": "2B",
    "I Don't Know": "3B",
    "Why": "LF",
    "Because": "CF",
    "Tomorrow": "P",
    "Today": "C",
    "I Don't Care": "SS"
}
players = [ ]
for x in player_positions:
  players.append(x)
print(players)
positions = set()
for x in player_positions.values():
  positions.add(x)
print(positions)
for x, y in player_positions.items():
  print (x + " is on " + y)
