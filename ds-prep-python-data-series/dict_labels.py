# Data Set: Do Not Modify
columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = {
    2002: 6,
    2020: 4,
    2007: 5,
    2015: 6,
    2010: 11,
    2014: 7,
    2001: 5,
    2006: 5,
    2004: 6,
    2009: 8,
    2013: 8,
    2008: 5,
    2021: 7,
    2018: 4,
    2011: 10,
    2005: 6,
    2016: 5,
    2019: 4,
    2012: 9,
    2017: 5,
    2003: 6
}

# Write your code below this line:
def last(di):
    c = list(di.items())
    d = dict(zip(columns, c[-1]))
    return(d)
print(last(unemployment_rates))
def five(dict):
    c = list(dict.items())
    return(c[:5])
print(five(unemployment_rates))
def included(year, dict):
    if year in dict:
        return(True)
    else:
            return(False)
print(included(2000, unemployment_rates))
print(included(2010, unemployment_rates))
def recent(dict):
    c = list(dict.items())
    c.sort()
    l = c[-1]
    return(l[1])
print(recent(unemployment_rates))
def years(dict):
    s= set()
    for x in dict:
        s.add(x)
    return(s)
print(years(unemployment_rates))
def rates(dict):
    c = list(dict.items())
    c.sort()
    l = []
    for x in c:
        l.append(x[1])
    return(l)
print(rates(unemployment_rates))
def largest(dict):
    c = list(dict.items())
    c.sort(key=lambda x: x[1])
    l = c[-1]
    return(l[1])
print(largest(unemployment_rates))
def greater(d):
    d1 = {}
    for x, y in d.items():
        if y >= 7:
            d1[x] = y
    return(d1)
print(greater(unemployment_rates))
def number(d):
    c = dict()
    for x, y in d.items():
        if (y in c):
            c[y] += 1
        else:
            c[y] = 1
    return(c)
print(number(unemployment_rates))
def employment_rate(dict):
    copied = dict.copy()
    for x, y in copied.items():
        copied.update({x: 100-y})
    return(copied)
print(employment_rate(unemployment_rates))
