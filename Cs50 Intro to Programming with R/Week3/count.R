mario <- readline("Enter votes for Mario: ")
peach <- readline("Enter votes for Peach: ")
bowser <- readline("Enter votes for Bowser: ")


mario <- as.integer(mario)
peach <- as.integer(peach)
bowser <- as.integer(bowser)


total <- mario + peach + bowser
total <- sum(mario, peach, bowser)  # same


print(paste("Total votes:", total))






# Demonstrates defining a function
get_votes <- function() {
  votes <- as.integer(readline("Enter votes: "))
  return(votes)
}
mario <- get_votes()
peach <- get_votes()
bowser <- get_votes()

total <- sum(mario,peach, bowser)
cat("Total votes: ", total)









# Demonstrates defining a parameter
get_votes <- function(prompt) {
  votes <- as.integer(readline(prompt))
  return(votes)
}
mario <- get_votes("Mario: ")
peach <- get_votes("Peach: ")
bowser <- get_votes("Bowser: ")

total <- sum(mario,peach, bowser)
cat("Total votes: ", total)






# Demonstrates defining a parameter with a default value
get_votes <- function(prompt = "Enter votes; ") {
  votes <- as.integer(readline(prompt))
  return(votes)
}
mario <- get_votes("Mario: ")
peach <- get_votes("Peach: ")
bowser <- get_votes("Bowser: ")

total <- sum(mario,peach, bowser)
cat("Total votes: ", total)






# Demonstrates exact argument matching

get_votes <- function(prompt = "Enter votes: ") {
  votes <- as.integer(readline(prompt))
}

mario <- get_votes(prompt = "Mario: ")
peach <- get_votes(prompt = "Peach: ")
bowser <- get_votes(prompt = "Bowser: ")

total <- sum(mario, peach, bowser)
cat("Total votes:", total)












# Demonstrates exact argument matching

get_votes <- function(prompt = "Enter votes: ") {
  votes <- suppressWarnings(as.integer(readline(prompt)))
  if (is.na(votes)) {
    return(0)
  } else {
    return(votes)
  }
}

get_votes <- function(prompt = "Enter votes: ") {
  votes <- suppressWarnings(as.integer(readline(prompt)))
  return(ifelse(is.na(votes), 0, votes))
}

mario <- get_votes(prompt = "Mario: ")
peach <- get_votes(prompt = "Peach: ")
bowser <- get_votes(prompt = "Bowser: ")

total <- sum(mario, peach, bowser)
cat("Total votes:", total)

