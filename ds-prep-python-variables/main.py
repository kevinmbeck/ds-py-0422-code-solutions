first_name = 'Kevin'
last_name = "Beck"
full_name = first_name + " " + last_name
print(full_name)
height_in_inches = 70
print(height_in_inches, type (height_in_inches))
height_in_inches_float = float(height_in_inches)
print(height_in_inches_float, type(height_in_inches_float))
height_in_meters = height_in_inches_float*0.0254
print(height_in_meters)
eats_plants = True
eats_animals = False
is_animal = eats_animals
if is_animal == eats_animals or is_animal == eats_plants:
  print(True)
else:
  print(False)
is_omnivore = eats_animals + eats_plants
if is_omnivore != eats_animals and is_omnivore == eats_plants:
  print(True)
else:
  print(False)
is_plant = eats_plants
if not(is_plant != is_animal):
  print(True)
else:
  print(False)
mean_height_in_meters = 1.7155
short_threshold_in_meters = 1.576
tall_threshold_in_meters = 1.860
is_mean_height = height_in_meters
if is_mean_height == mean_height_in_meters:
  print(True)
else:
  print(False)
is_short = height_in_meters
if is_short < short_threshold_in_meters:
  print(True)
else:
  print(False)
is_tall = height_in_meters
if is_tall >= tall_threshold_in_meters:
  print(True)
else:
  print(False)
is_normal_height = height_in_meters
if is_normal_height >= short_threshold_in_meters and is_normal_height < tall_threshold_in_meters:
  print(True)
else:
  print(False)
nothing = None
print(nothing)
