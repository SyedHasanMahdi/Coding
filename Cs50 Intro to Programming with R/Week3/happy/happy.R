file1 <- read.csv("2020.csv")
file1$year <- "2020"
file2 <- read.csv("2021.csv")
file2$year <- "2021"
file3 <- read.csv("2022.csv")
file3$year <- "2022"
file4 <- read.csv("2023.csv")
file4$year <- "2023"
file5 <- read.csv("2024.csv")
file5$year <- "2024"

full <- rbind(file1,file2,file3,file4,file5)

choice <- readline("Country: ")

flag <- FALSE
if (choice %in% unique(full$country)) {
  full <- full[full$country == choice, ]
  score <- c()
  for (year in 1:5) {
    row_year <- full[year, 2:8]
    score[year] <- apply(row_year, MARGIN = 1, FUN = sum)
    score[year] <- round(score[year], 2)
  }
} else {
  flag <- TRUE
}

if (flag == TRUE) {
  for (i in 1:5) {
    year <- 2019 + i
    print(paste0("choice (year): data unavailable "))
  }
} else {
  for (i in 1:5) {
    print(paste0(choice," (",i+2019,"): ", score[i]))
  }
}
