bool_to_int = lambda value: int(value)
print(bool_to_int(True))
get_smaller = lambda a, b: a if (a<b) else b
print(get_smaller(32,45))
def cube(base):
  print(base**3)
cube(9)
def absolute_value(a,b):
  if (a<b):
    return(b-a)
  else:
    return(a-b)
print(absolute_value(12,9))
def squared_value(a,b):
  if (a<b):
    return((b-a)**2)
  else:
    return((a-b)**2)
print(squared_value(12,9))
def hours_to_minutes(hours):
  return(hours*60)
print(hours_to_minutes(hours = 2))
def get_circumference(radius):
  return(radius*2*3.14)
print(get_circumference(radius=1))
def linear_transform(x, slope, intercept):
  return((slope*x)+intercept)
print(linear_transform(x=5, slope=2, intercept=3))
print(linear_transform(intercept=2, x=6, slope=3))
def standardize(x, x_center, scale_size):
  if (x>x_center):
    return((x-x_center)/scale_size)
  else:
    return((x_center-x)/scale_size)
print(standardize(x=6, x_center=4, scale_size=2))
print(standardize(scale_size=3, x=12, x_center=6))
