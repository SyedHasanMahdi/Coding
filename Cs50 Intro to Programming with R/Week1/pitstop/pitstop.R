filename <- readline("Enter a CSV filename to analyse: ")
race <- read.csv(filename)
print(nrow(race))
time = race$time
print(min(time)) # shortest pit stop
print(max(time)) # longest pit stop
print(sum(time)) # total time spent on pitstops across all racers



