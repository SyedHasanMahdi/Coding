chicks <- read.csv("chicks.csv")
View(chicks)


chicks
mean(chicks$weight, na.rm = TRUE) # mean without NA values

casein_chicks <- chicks[c(1,2,3), ]      # how food each chick eats impact their weight
mean(casein_chicks$weight)


#simplified
filter <- chicks$feed == "casein"         # boolean vector to find rows where the feed column has value "casein"
casein_chicks <- chicks[filter,]
mean(casein_chicks$weight)

#same
casein_chicks <- subset(chicks,feed=="casein")
mean(casein_chicks$weight, na.rm=TRUE)

is.na(chicks$weight) #chicking which is NA
chicks$chick[is.na(chicks$weight)]    # chick number that has NA weight

chicks <- subset(chicks, !is.na(weight))
rownames(chicks)


rownames(chicks) <- NULL      # reset them so its back to linear row names
rownames(chicks)



# determine the feed options to create a menu
feed_options <- unique(chicks$feed)

# prompt the user with options
cat("1.", feed_options[1])
cat("2.", feed_options[2])
cat("3.", feed_options[3])
cat("4.", feed_options[4])
cat("5.", feed_options[5])
cat("6.", feed_options[6])
feed_choice <- as.integer(readline("Feed type: "))









# Escape characters include:
#  \n          for a new line
#  \t          for a tab





# improving our menu
feed_options <- unique(chicks$feed)
cat("1.", feed_options[1], "\n")
cat("2.", feed_options[2], "\n")
cat("3.", feed_options[3], "\n")
cat("4.", feed_options[4], "\n")
cat("5.", feed_options[5], "\n")
cat("6.", feed_options[6], "\n")
feed_choice <- as.integer(readline("Feed type: "))





# we dont need to repeat the cat lines asw

formatted_options <- paste0(1:length(feed_options), ". ", feed_options)
cat(formatted_options, sep = "\n")
feed_choice <- as.integer(readline("Feed type: "))

# to find an invalid choice

if (feed_choice< 1 || feed_choice > length(feed_options)) {
  cat("Invalid Choice.")
} else {
  # print the slected option
  
  selected_feed <- feed_options[feed_choice]
  print(subset(chicks, feed == selected_feed))
}



