load(file = 'zelda.RData')
zelda <- zelda |>
  group_by(year) |>
  summarize(releases = n()) |>
  arrange(desc(releases)) |>
  ungroup()
save(zelda, file = "2.RData")
