load(file = "air.RData")
air <- air |> 
  select(c(level_1, pollutant, emissions)) |>
  group_by(level_1, pollutant) |>
  summarise(emissions = sum(emissions)) |>
  arrange(level_1, pollutant) |>
  ungroup()
save(air, file = "7.RData")
