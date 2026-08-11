load(file = "zelda.RData")
zelda <- zelda |>
  group_by(title) |>
  slice_min(order_by = year) |>
  filter(str_detect(producers, "Shigeru Miyamoto")) |>
  arrange(year, title, system) |>
  ungroup()
save(zelda, file = "4.RData")
