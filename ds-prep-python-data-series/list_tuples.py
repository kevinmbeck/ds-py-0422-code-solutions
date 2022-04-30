# Data Set: Do Not Modify
columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = [
    (2005, 6),
    (2001, 5),
    (2013, 8),
    (2011, 10),
    (2017, 5),
    (2006, 5),
    (2009, 8),
    (2021, 7),
    (2002, 6),
    (2007, 5),
    (2012, 9),
    (2014, 7),
    (2003, 6),
    (2019, 4),
    (2016, 5),
    (2015, 6),
    (2018, 4),
    (2008, 5),
    (2010, 11),
    (2004, 6),
    (2020, 4)
]

# Write your code below this line:
def last(list):
    d = dict(zip(columns, list[-1]))
    return(d)
print(last(unemployment_rates))
def five(list):
    return(list[:5])
print(five(unemployment_rates))
def included(year, list):
    if [x for x in list if x[0] == year]:
        return(True)
    else:
        return(False)
print(included(2000, unemployment_rates))
print(included(2010, unemployment_rates))
def recent(list):
    l = sorted(list)
    l1 = l[-1]
    return(l1[1])
print(recent(unemployment_rates))
def years(list):
    s= set()
    for x in list:
        s.add(x[0])
    return(s)
print(years(unemployment_rates))
def rates(list):
    l1 = sorted(list)
    l = []
    for x in l1:
        l.append(x[1])
    return(l)
print(rates(unemployment_rates))
def largest(list):
    l1 = sorted(list, key=lambda x: x[1])
    l = l1[-1]
    return(l[1])
print(largest(unemployment_rates))
def employment_rates(l):
    l1 = []
    l2 = []
    for x in l:
        l1.append(x[0])
        l2.append(100-x[1])
    l3 = list(zip(l1, l2))
    return(l3)
print(employment_rates(unemployment_rates))
def greater(list):
    l = []
    for x in list:
        if x[1]>= 7:
            l.append(x)
    return(l)
print(greater(unemployment_rates))
def number(list):
    c = dict()
    for x in list:
        if (x[1] in c):
            c[x[1]] += 1
        else:
            c[x[1]] = 1
    return(c)
print(number(unemployment_rates))
