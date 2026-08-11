load(file = "air.RData")
air <- air |>
  filter(county == "OR - Marion") |>
  arrange(desc(emissions))
save(air, file = "4.RData")
