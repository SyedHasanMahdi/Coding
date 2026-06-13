soft <- c("soft", "dense")
soft_choice <- paste0(1:2, ". ", soft)
cat(soft_choice, sep = "\n")
soft_choice <- readline("Would you like the bread to be soft or dense: ")


flavor <- c("hearty", "classic")
flavor_choice <- paste0(1:2, "", flavor)
cat(flavor_choice, sep = "\n")
flavor_choice <- readline("")




if (soft_choice == "soft" && flavor_choice == "classic") {
  print("You should try White Bread")
} else if (soft_choice == "soft" && flavor_choice == "hearty") {
  print("You should try Milk Bread")
} else if (soft_choice == "dense" && flavor_choice == "classic") {
  print("You should try Brown Bread")
} else if (soft_choice == "dense" && flavor_choice == "hearty") {
  print("You should try Protein Bread")
}


