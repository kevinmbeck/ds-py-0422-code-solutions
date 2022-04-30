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
    {"unemployment_rate": 8, "year": 2013},
    {"unemployment_rate": 5, "year": 2006},
    {"unemployment_rate": 5, "year": 2017},
    {"unemployment_rate": 6, "year": 2015},
    {"unemployment_rate": 6, "year": 2002},
    {"unemployment_rate": 4, "year": 2019},
    {"unemployment_rate": 9, "year": 2012},
    {"unemployment_rate": 4, "year": 2018},
    {"unemployment_rate": 6, "year": 2003},
    {"unemployment_rate": 5, "year": 2007},
    {"unemployment_rate": 11, "year": 2010},
    {"unemployment_rate": 7, "year": 2014},
    {"unemployment_rate": 6, "year": 2004},
    {"unemployment_rate": 5, "year": 2016},
    {"unemployment_rate": 6, "year": 2005},
    {"unemployment_rate": 7, "year": 2021},
    {"unemployment_rate": 5, "year": 2001},
    {"unemployment_rate": 4, "year": 2020},
    {"unemployment_rate": 10, "year": 2011},
    {"unemployment_rate": 8, "year": 2009},
    {"unemployment_rate": 5, "year": 2008}
]

# Write your code below this line:
def last(list):
    return(list[-1])
print(last(unemployment_rates))
def five(list):
    c = [tuple(x.values()) for x in list]
    return(c[:5])
print(five(unemployment_rates))
def included(year, list):
    for x in list:
        if any(x["year"] == year for x in list):
            return(True)
        else:
            return(False)
print(included(2000, unemployment_rates))
print(included(2010, unemployment_rates))
def recent(list):
    list.sort(key = lambda item: item.get("year"))
    l = list[-1]
    return(l.get("unemployment_rate"))
print(recent(unemployment_rates))
def years(list):
    s= set()
    for x in list:
        s.add(x["year"])
    return(s)
print(years(unemployment_rates))
def rates(list):
    list.sort(key = lambda item: item.get("year"))
    l = []
    for x in list:
        l.append(x["unemployment_rate"])
    return(l)
print(rates(unemployment_rates))
def largest(list):
    list.sort(key=lambda x: x.get("unemployment_rate"))
    l = list[-1]
    return(l.get("unemployment_rate"))
print(largest(unemployment_rates))
def greater(list):
    l = []
    for x in list:
        if x["unemployment_rate"]>= 7:
            l.append(x)
    return(l)
print(greater(unemployment_rates))
def number(list):
    c = dict()
    for x in list:
        if (x["unemployment_rate"] in c):
            c[x["unemployment_rate"]] += 1
        else:
            c[x["unemployment_rate"]] = 1
    return(c)
print(number(unemployment_rates))
def employment_rates(list):
    for x in list:
        x.update({"employment_rate": 100-x.get("unemployment_rate")})
        del x["unemployment_rate"]
    return(list)
print(employment_rates(unemployment_rates))
