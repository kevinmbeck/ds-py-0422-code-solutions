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
    'year': [
        2009, 2011, 2005, 2016, 2001,
        2012, 2019, 2007, 2021, 2018,
        2010, 2013, 2006, 2017, 2015,
        2014, 2008, 2004, 2003, 2020,
        2002
    ],
    'unemployment_rate': [
        8, 10, 6, 5, 5,
        9, 4, 5, 7, 4,
        11, 8, 5, 5, 6,
        7, 5, 6, 6, 4,
        6
    ]
}

# Write your code below this line:
def last(di):
    c = list(zip(di['year'], di['unemployment_rate']))
    d = dict(zip(columns, c[-1]))
    return(d)
print(last(unemployment_rates))
def five(dict):
    c = list(zip(dict['year'], dict['unemployment_rate']))
    return(c[:5])
print(five(unemployment_rates))
def included(year, dict):
    if year in dict['year']:
        return(True)
    else:
        return(False)
print(included(2000, unemployment_rates))
print(included(2010, unemployment_rates))
def recent(dict):
    c = list(zip(dict['year'], dict['unemployment_rate']))
    c.sort()
    l = c[-1]
    return(l[1])
print(recent(unemployment_rates))
def years(dict):
    s= set()
    for x in dict['year']:
        s.add(x)
    return(s)
print(years(unemployment_rates))
def rates(dict):
    c = list(zip(dict['year'], dict['unemployment_rate']))
    c.sort()
    l = []
    for x in c:
        l.append(x[1])
    return(l)
print(rates(unemployment_rates))
def largest(dict):
    c = list(zip(dict['year'], dict['unemployment_rate']))
    c.sort(key=lambda x: x[1])
    l = c[-1]
    return(l[1])
print(largest(unemployment_rates))
def greater(di):
    c = list(zip(di['year'], di['unemployment_rate']))
    l = []
    for x in c:
        if x[1] >= 7:
            l.append(x)
    l1 = []
    l2 = []
    for x in l:
        l1.append(x[0])
        l2.append(x[1])
    d = {}
    d['year'] = l1
    d['unemployment_rate'] = l2
    return(d)
print(greater(unemployment_rates))
def number(d):
    c = dict()
    for x in d['unemployment_rate']:
        if (x in c):
            c[x] += 1
        else:
            c[x] = 1
    return(c)
print(number(unemployment_rates))
def employment_rate(dict):
    dict['employment_rate'] = dict.pop('unemployment_rate')
    for x in dict['employment_rate']:
        dict['employment_rate'] = [100-x for x in dict['employment_rate']]
    return(dict)
print(employment_rate(unemployment_rates))
