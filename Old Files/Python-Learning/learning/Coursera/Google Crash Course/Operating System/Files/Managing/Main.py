import os

# os.remove("novel.txt")
# os.remove("novel.txt")

# if file doesn't exist, error will be returned

# os.rename("first_draft.txt", "finished_masterpiece.txt")

os.path.exists("finished_masterpiece.txt")
# shows if file exists. True or false
os.path.exists("userprofile.txt")

print(os.path.getsize("spider.txt"))  # returns file size
print(os.path.getmtime("spider.txt"))  # timestamp

import datetime

timestamp = os.path.getmtime("spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))  # makes data easier to understand

print(os.path.abspath("spider.txt"))  # directory of file

print(os.getcwd())  # current directory
print(os.mkdir("new_dir"))  # makes new directory
# print(os.chdir("new_dir")) #change directory
print(os.rmdir("new_dir"))  # only empty directory removed
print(os.listdir())  # List files in directory

dir = "Managing"
for name in os.listdir():
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):  # find out what they are
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
#    https://docs.python.org/3/library/os.html

#    https://docs.python.org/3/library/os.path.html

#    https://en.wikipedia.org/wiki/Unix_time
