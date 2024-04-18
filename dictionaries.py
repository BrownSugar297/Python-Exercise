
studentInfo = {
    "Ashik": {
        "Name": "Ashik",
        "Location": "Barishal",
        "Study": "University",
        "Subject": "CSE",
        "Roll": '2002026',
        "Number": '01782238232'
    },
       "Adib": {
        "Name": "Adib",
        "Location": "Barishal",
        "Study": "BZS",
        "Subject": "Science",
        "Roll": '20',
        "Number": '01731937507'
    },
    "Year": '1971'
}
math = {
    "sum1": 20,
    "sum2": 30,
    "sum3": 40
}

print(studentInfo["Adib"])
print(studentInfo["Ashik"]["Roll"])
print(studentInfo['Year'])
print(studentInfo.get("Adib"))
print(studentInfo.keys())
print(studentInfo.values())
print('\n')

#Update
studentInfo["Year"] = 2007
print(studentInfo["Year"])
studentInfo.update({"Adib":"Adib Mahmud"})
print(studentInfo["Adib"])
print('\n')

studentInfo.pop("Adib")
print(studentInfo)
studentInfo.popitem()
print(studentInfo)

for x in studentInfo:
    print(x)

for a in studentInfo.values():
    print(a)

for b in math.values():
    print(b)

for item in math.items():
    print(item)

#Copy

myDict = math.copy()
print(math)



