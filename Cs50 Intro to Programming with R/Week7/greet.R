# Demonstrates using custom package

library(ducksay)

name <- readline("What's your name? ")
msg <- greeting <- ducksay(paste("hello,", name))
cat(greeting)
