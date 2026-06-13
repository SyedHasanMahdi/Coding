
bus <- read.csv("bus.csv")
rail <- read.csv("rail.csv")
transport <- rbind(bus,rail)
chosen_route <- readline("What route do u want to take? ")
while (!(chosen_route %in% unique(transport$route))) {
  print("Invalid.")
  chosen_route <- readline("What route do u want to take? ")
}

route_match <- subset(transport, route == chosen_route)
offP = subset(route_match, peak == "OFF_PEAK")
onP = subset(route_match, peak == "PEAK")
mean_offP <- toString(round(mean(offP[,7] / offP[,8]) *100, 0))
mean_onP <- toString(round(mean(onP[,7] / onP[,8]) * 100, 0))

print(paste0("for Off peak hours, the reliability is: ", mean_offP, "%"))
print(paste0("for On peak hours, the reliability is: ", mean_onP, "%"))

