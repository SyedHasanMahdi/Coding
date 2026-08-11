cat("quack!\n")
cat("quack!\n")
cat("quack!\n")


repeat {
  cat("quack!\n")
}



i <- 3
repeat {
  cat("quack!\n")
  i <- i - 1
  if (i==0) {
    break
  }
}


i <- 3
while (i != 0) {
  cat("quack!\n")
  i <- i - 1
}


for (i in c(1, 2, 3)) {
  cat("quack!\n")
}


for (i in 1:3) {
  cat("quack!\n")
}





get_votes <- function(prompt = "Enter votes: ") {
  repeat {
    votes <- suppressWarnings(as.integer(readline(prompt)))
    if (!is.na(votes)) {
      break
    }
  }
  return(votes)
}

get_votes <- function(prompt = "Enter votes: ") {
  repeat {
    votes <- suppressWarnings(as.integer(readline(prompt)))
    if (!is.na(votes)) {
      return(votes)
    }
  }
  
}
mario <- get_votes(prompt = "Mario: ")
peach <- get_votes(prompt = "Peach: ")
bowser <- get_votes(prompt = "Bowser: ")



total <- 0
for (name in c("Mario", "Peach", "Bowser")) {
  votes <- get_votes(paste0(name, ": "))
  total <- total + votes
}
cat("Total votes:", total)




votes <- read.csv("votes.csv")
total_votes <- c()
for (candidate in rownames(votes)) {
  total_votes[candidate] <- sum(votes[candidate, ])
}
total_votes





# Demonstrates summing votes for each candidate with apply

votes <- read.csv("votes.csv")
total_votes_rows <- apply(votes, MARGIN = 1, FUN = sum)
total_votes_rows
# Demonstrates summing votes for each column with apply
total_votes_column <- apply(votes, MARGIN = 2, FUN = sum)
total_votes_column

