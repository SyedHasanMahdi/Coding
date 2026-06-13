phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
print(phonebook)
for name, number in phonebook.items():
    print("%s's number is %d" % (name, number))

del phonebook["John"]  # or del phonebook["John"]
print(phonebook)
phonebook["John"] = 938477566

phonebook = {"John": 938477566, "Jack": 938273443, "Jill": 947662781}
# your code goes here
del phonebook["Jill"]
phonebook["Jake"]=938273443
# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")