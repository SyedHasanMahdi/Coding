import csv

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has {} users".format(row["name"], row["users"]))

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
         {"name": "Lio Nelson", "username": "lion", "department": "User experience Research"},
         {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]

keys = ["name", "username", "department"]  # define keys we want to write to file

with open("by_department.csv", 'w') as by_department:  # open the file
    writer = csv.DictWriter(by_department, fieldnames=keys)  # create Dict writer passing keys we identified
    writer.writeheader()  # will create first line based on keys passed
    writer.writerows(users)  # create next lines based on dictionaries

#    https://docs.python.org/3/library/csv.html

#    https://realpython.com/python-csv/