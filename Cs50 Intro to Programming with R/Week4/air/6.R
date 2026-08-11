load(file= "air.RData")
air <-air |>
  select(c(pollutant, emissions)) |>
  group_by(pollutant) |>
  summarise(emissions = max(emissions)) |>
  arrange(desc(emissions)) |>
  ungroup()

save(air, file = "6.RData")
