person = {
	"first_name": "Kevin",
    "last_name": "Beck",
    "hobby": "reading"
}

print(person)

first_name = person["first_name"]
last_name = person.get("last_name")
middle_name = person.get("middle_name")

print(first_name, middle_name, last_name)

person["job"] = "barista"

print(person["job"])

person["hobby"] = "hiking"

print(person["hobby"])

person.pop("last_name")

print(person)
