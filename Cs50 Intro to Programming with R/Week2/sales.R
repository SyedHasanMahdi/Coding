Q1 <- read.csv("Q1.csv")
Q2 <- read.csv("Q2.csv")
Q3 <- read.csv("Q3.csv")
Q4 <- read.csv("Q4.csv")

# combined all four data frames into 1
# rbind used because all four data frames are structured the same way
sales <- rbind(Q1, Q2, Q3, Q4)
View(sales)



# add a column to show the quarter for each row
Q1 <- read.csv("Q1.csv")
Q1$quarter <- "Q1"
Q2 <- read.csv("Q2.csv")
Q2$quarter <- "Q2"
Q3 <- read.csv("Q3.csv")
Q3$quarter <- "Q3"
Q4 <- read.csv("Q4.csv")
Q4$quarter <- "Q4"
sales<- rbind(Q1,Q2,Q3,Q4)
View(sales)


# we can also add a column to note when high or regular returns are noted

sales$value <- ifelse(sales$sale_amount > 100, "High Value", "Regular")
View(sales)
