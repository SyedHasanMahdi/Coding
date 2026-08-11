air <- read_csv("air.csv")
  colnames(air)[1] <- "state" 
  colnames(air)[2] <- "county"
  colnames(air)[3] <- "pollutant"
  colnames(air)[4]  <- 'emissions'
  colnames(air)[9] <- "level_1"
  colnames(air)[10] <- "level_2"
  colnames(air)[11] <- "level_3"
  colnames(air)[12] <- "level_4"
save(air, file = "air.RData")
