# tidyr is a library to use when data is not already well organised
library(tidyverse)
#1. Each observation is a row; each row is an observation.
#2. Each variable is a column; each column is a variable.
#3. Each value is a cell; each cell is a single value.


#normalizing is the process of converting data such that they fulfill these 3 rules
students <- read.csv('students.csv')
View(students)


# there are some row values that should instead be a column name such as "Major" or "GPA"
# this data set violates the second rule
# we can pivot the data to turn those variables into columns

#pivot_wider can transform a data set that is longer than it shuld be ( one with variables as row values) and 
#make it wider (turn the vars to columns)


students <- read.csv("students.csv")

students <- pivot_wider(
  students,        # data to operate on
  id_cols = student,     # specifies which column should be unique, there are duplicate values in student column before
  names_from = attribute, # specifies which column contains values that should instead be columns / variables
  values_from = value # specifies the column from which to populate the values of the new columns
)
View(students)



# finding the meanof the GPA after its converted into a numeric value
students$GPA <- as.numeric(students$GPA)
students |> 
  group_by(major) |>
  summarize(GPA =mean(GPA))