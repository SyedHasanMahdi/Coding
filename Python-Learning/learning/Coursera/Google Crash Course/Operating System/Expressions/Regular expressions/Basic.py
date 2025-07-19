import re  # regular expression

print(re.search(r"aza", "plaza"))
# use the pattern aza on the string plaza
# r means rawstring, no special characters interpreted
print(re.search(r"aza", "bazaar"))

# if we pass a string that doesn't include the expression we get None as result
print(re.search(r"aza", "maze"))
print(re.search(r"^x", "xenon"))

print(re.search("p.ing", "penguin"))  # matches peng
# . can match any letter

print(re.search(r"p.ng", "clapping"))  # matches ping

print(re.search(r"p.ng", "Pangea", re.IGNORECASE))  # case insensitive

# What if we wanted all usernames that start with a vowel
# What if we wanted to check if an answer contains a valid character
# We have to use character classes. They are written in []

print(re.search(r"[Pp]ython", "Python"))  # lower or uppercase P

print(re.search(r"[a-z]way", "The end of the highway"))  # any letter between a-z at the start
print(re.search(r"[a-z]way", "What a way to go"))  # no match because space is not between a-z

print(re.search("cloud[a-zA-Z0-9]", "cloudy"))  # combined expression
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

# match any character that aren't
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
# first space is matched
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
# . is matched because space is excluded in expression.

# cat or dog
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like dogs."))
print(re.search(r"cat|dog", "I like dogs and cats."))  # first one matched only

# to match all use findall
print(re.findall(r"cat|dog", "I like cats and dogs."))

print(re.search(r"Py.*n", "Pygmalion"))  # .* expands range to whole word
# Py and everything till n

print(re.search(r"Py.*n", "Python Programming"))
# .* takes as many values as possible

print(re.search(r"Py[a-z]*n", "Python Programming"))
# letter between Py and n should be a-z

print(re.search(r"o+l+", "goldfish"))
# shortest matching string
print(re.search(r"o+l+", "ooll"))
print(re.search(r"o+l+", "boil"))  # letter between o and l

print(re.search(r"p?each", "To each their own"))
# p is optional but rest has to match

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))  # theres no .com
print(re.search(r"\.com", "mydomain.com"))  # can use \ to escape any special characters

# \w matches any alphanumeric character (number,letter or underscore)
print(re.search(r"\w*", "And_this_is_another"))

print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))

print(re.search(r"^A.*a$", "Azerbaijan"))  # has to start and end with a
print(re.search(r"^A.*a$", "Australia"))

pattern = r"^[a-zA-z_][a-zA-z0-9_]*"  # start with a-zA-z_ and only has a-zA-z0-9_
# It can contain any number of letters numbers or underscores,but it can't start with a number
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isnt a valid variable name"))

#    https://docs.python.org/3/howto/regex.html

#    https://docs.python.org/3/library/re.html

#   https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy