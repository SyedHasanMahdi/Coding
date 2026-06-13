flavor <- c("Light", "Bold")
flavor_choice <- paste0(1:2, ". ", flavor)
cat(flavor_choice, sep = "\n")
flavor_choice <- readline("Would you like the drink to have a light or bold flavor: ")
caffeine <- c("Yes", "No")

caffeine_choice <- paste0(1:2, ". ", caffeine)
cat(caffeine_choice, sep = "\n")
caffeine_choice <- readline("Would you like the drink to contain caffeine: ")


if (caffeine_choice == "Yes" && flavor_choice == "Light") {
  print("You should try Green Tea")
} else if (caffeine_choice == "Yes" && flavor_choice == "Bold") {
  print("You should try Black Tea")
} else if (caffeine_choice == "No" && flavor_choice == "Light") {
  print("You should try Chamomile Tea")
} else if (caffeine_choice == "No" && flavor_choice == "Bold") {
  print("You should try Rooibos Tea")
}


