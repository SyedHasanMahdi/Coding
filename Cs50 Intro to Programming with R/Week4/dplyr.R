# Dplyr is a package that includes functions tom anipulate data
# it has a data set called storms which includes observations of storm data

# loading a library
library(dplyr)




# selecting specific rows and excluding the given set of rows
# endswith is used to remove all rows which have a name ending with diameter so they dont have to be listed individually
select(storms,
       !c(lat, long, pressure, ends_with("diameter")))






# filter rows from data frame
# only get the hurricanes from data base
filter(
  select(
    storms,
    !c(lat,long, pressure, ends_with("diamter"))
  ),
  status == "hurricane"
)




# pipe operator |> allows one to pipe data into specific functions
storms |>
  select(!c(lat,long,pressure,ends_with("diameter"))) |>
  filter(status == "hurricane")



# arrange to sort the rows
storms |>
  select(!c(lat,long,pressure,ends_with("diamter"))) |>
  filter(status == "hurricane") |>
  arrange(desc(wind))




# finding distinct storms from the tibble rows
# by default it only considers duplicate if all values in the row match, but you can change what values to consider
storms|>
  select(!c(lat,long,pressure,ends_with("diamter")))|>
  filter(status == "hurricane") |>
  arrange(desc(wind), name) |>
  distinct(name, year, .keep_all =TRUE)
# keep_all tells distinct to still return all the columns for each row








# we can also save our data for later in a csv file
hurricanes <- storms|>
  select(!c(lat,long,pressure,ends_with("diamter")))|>
  filter(status == "hurricane")|>
  arrange(desc(wind), name) |>
  distinct(name,year,.keep_all=TRUE)

hurricanes|>
  select(c(year,name,wind))|>
  write.csv("hurricanes.csv", row.names = FALSE)
  




# finding the most powerful hurricane in each year by groupuing
hurricanes <- read.csv("hurricanes.csv")
hurricanes |>
  group_by(year)|>
  arrange(desc(wind)) |>
  slice_head()             # returns the top row from each group thus the strongest storm from each year presented

hurricanes|>
  group_by(year)|>
  slice_max(order_by = wind)     # selects the largest values within a variable so it eliminates the need for arrange()



# what if we wanted to know the number of hurricanes each yaer
hurricanes |>
  group_by(year)|>
  summarise(hurricanes = n())     # n counts the number of rows per group



# ungrouping 
hurricanes|>
  group_by(year)|>
  slice_max(order_by= wind)|>
  ungroup()
