visitors <- read.csv("visitors.csv", header = TRUE)
calculate_growth_rate <- function() {
  diff_latest_first_visitors <- visitors$visitors[length(visitors$visitors)] - visitors$visitors[1]
  diff_latest_first_year <- visitors$year[length(visitors$year)] - visitors$year[1]
  growth_rate <- diff_latest_first_visitors / diff_latest_first_year
  return(growth_rate)
}
predict_visitors <- function(year) {
  diff_year <- year - visitors$year[length(visitors$year)]
  avg_growth <- calculate_growth_rate()
  expected <- (visitors$visitors[length(visitors$visitors)] + avg_growth * diff_year)
  return(paste0(expected, " million visitors"))
}

year <- as.integer(readline("Year: "))
predict_visitors(year)

