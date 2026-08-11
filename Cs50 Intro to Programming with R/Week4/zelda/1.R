library(tidyverse)
zelda <- read_csv("zelda.csv")

zelda <- zelda |>
  pivot_wider(
  id_cols = c(title, release),     # specifies which column should be unique, there are duplicate values in student column before
  names_from = role, # specifies which column contains values that should instead be columns / variables
  values_from = names # specifies the column from which to populate the values of the new columns
  ) |>
  separate_wider_delim(release, delim = " - ",names = c("year", "system"))
  colnames(zelda) <-tolower(colnames(zelda))
  
  
save(zelda, file = "zelda.RData")
