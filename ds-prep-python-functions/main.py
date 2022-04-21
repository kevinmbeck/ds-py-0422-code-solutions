bool_to_int = lambda value: int(value)
print(bool_to_int(True))
get_smaller = lambda a, b: a if (a<b) else b
print(get_smaller(32,45))
def cube(base):
  print(base**3)
cube(9)
def absolute_value(a,b):
  if (a<b):
    print(b-a)
  else:
    print(a-b)
print(absolute_value(12,9))
def squared_value(a,b):
  if (a<b):
    print((b-a)**2)
  else:
    print((a-b)**2)
print(squared_value(12,9))
def hours_to_minutes(hours):
  print(hours*60)
hours_to_minutes(hours = 2)
def get_circumference(radius):
  print(radius*2*3.14)
print(get_circumference(radius=1))
def linear_transform(x, slope, intercept):
  print((slope*x)+intercept)
print(linear_transform(x=5, slope=2, intercept=3))
print(linear_transform(intercept=2, x=6, slope=3))
