# Demonstrates taking an argument to print

ducksay <- function(phrase = "hello, world") {
  paste(
    phrase,
    ">(. )__",
    " (____/",
    sep = "\n"
  )
}