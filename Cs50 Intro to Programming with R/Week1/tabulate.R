votes <- read.table("votes.csv", sep = ",", header = TRUE)   # reads the table from votes.csv into votes variable
# (sep) tells the read.table which character each column separates on
# (header) tells the read.table that there is a header


#simplified to
votes <- read.csv("votes.csv")


View(votes)        #  displays the table contents

# votes[row, column]
votes[,1] # all the values in first column (candidate)
votes[,2] # all the values in second column (poll)
votes[,3] # all the values in third column (mail)


# Vectors are a list of values all of the same storage mode
# Considering our table,, we can access specific values by creating a new vector
# we can simplify by calling the precise name of each column
colnames(votes)
votes$candidate # returns vector of all values in candidate column
votes$poll
votes$mail
#we can now access the values of poll with this new vector


sum(votes$poll[1], votes$poll[2], votes$poll[3])  # adding the values 1st, 2nd, 3rd row of poll
sum(votes$poll) # Simplified

# adding the values in each row across poll and mail
votes$poll[1] + votes$mail[1]
votes$poll[2] + votes$mail[2]
votes$poll[3] + votes$mail[3]

# simplified using vector arithmetic
votes$poll + votes$mail

votes$total <- votes$poll + votes$mail
write.csv(votes,"total.csv")
write.csv(votes,"total.csv", row.names=FALSE) # exclude row names



#We can also access external data
url <- "https://github.com/fivethirtyeight/data/raw/master/non-voters/nonvoters_data.csv"
voters <- read.csv(url)

nrow(voters) #  number of rows
ncol(voters) #  number of columns
View(voters)


unique(voters$voter_category) # determine the possible options participants may have selected


# we find that Q22 deals with why participants arent registered to vote, 
# there is NA in this column
voters$Q22
unique(voters$Q22)


# we find that Q21 deals with participants' plans to vote in future elections
# there is value of 1, 2 and 3. This may mean 1:Yes, 2:No, 3:Not Sure
voters$Q21
unique(voters$Q21)




factor( 
  voters$Q21 # shows the specific categories / levels of data for Q21
)




factor(
  voters$Q21,
  labels = c("?", "Yes", "No", "Unsure/Undecided") #change the number 1 to correspond to the text "Yes
)




# Simplified version
url <- "https://github.com/fivethirtyeight/data/raw/master/non-voters/nonvoters_data.csv"
voters <- read.csv(url)

voters$Q21 <- factor(
  voters$Q21,
  labels = c("Yes", "No", "Unsure/Undecided"),
  exclude = c(-1)
)
# excludes -1 as u dont know what it represents
voters$Q21
