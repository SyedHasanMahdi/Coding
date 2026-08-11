load(file= "air.RData")
air <- air |>
  group_by(county) |>
  slice_max(order_by = emissions)|>
  ungroup()
save(air, file= "5.Rdata")
