
# what if the values themselves arent tidy
shows <- read.csv("shows.csv")
shows |>
  group_by (show)|>
  summarize(votes = n()) |>
  ungroup() |>
  arrange(desc(votes))






# if u look at the titles of shows, there are repeats of Avatar: the last airbender due to spaces and capitalisation differences
shows$show <- shows$show |>
  str_trim() |>  # removes trailing whitespaces
  str_squish() |> # removes whitespaces between the words
  str_to_title() # forces title casing on each string so each word is capital

shows |>
  group_by (show)|>
  summarize(votes = n()) |>
  ungroup() |>
  arrange(desc(votes))

