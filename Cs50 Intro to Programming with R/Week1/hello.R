print("hello, world")




# Demonstrates a bug
# prin("hello, world")






readline("What's your name? ") # taking input
print("Hello, Carter") # the name is hardcoded, never changes





name <- readline("What's your name? ")  # storing the input
print("Hello, name") # it still is hard coded and doesnt work





name <- readline("What's your name? ")  # storing the input
greeting <- paste("Hello, ", name)  # combining the two strings
print(greeting) # now it works





?paste # access the documentation


name <- readline("What's your name? ")
greeting <- paste("Hello, ", name, sep = "")  
greeting <- paste0("Hello, ", name) # same as this, paste0 is shortcut.
print(greeting)





#ask user for name
name <- readline("What's your name? ")

#say hello to user
print(paste("Hello,", name))





