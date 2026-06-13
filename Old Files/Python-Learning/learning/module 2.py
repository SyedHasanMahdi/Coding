# import the library
import urllib

# We can look for which functions are implemented in each
# module by using the dir function:

dir(urllib)

# When we find the function in the module we want to use, we
# can read about it more using the help function
help(urllib)

# If we create a directory called foo, which marks the package name, we
# then create a module inside that package called bar. We also must not
# forget to add the __init__.py file inside the foo directory.

import foo.bar

print(foo.bar)
# from foo import bar. we dont need to use foo prefix if we do this

import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))
numbers=1,2,5,7,1,0
print(sorted(numbers))