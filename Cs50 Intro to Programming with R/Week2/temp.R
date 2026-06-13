load("temps.RData") # loading data
temps
mean(temps) #accessing average of loaded data





temps[2] #second val
temps[4] #fourth val
temps[7] #seventh val

#simplified
temps[c(2,4,7)]



no_outliers <- temps[-c(2,4,7)]  #removing certain indexs



mean(no_outliers) # without the outliers
mean(temps)



# logical manner to identify outlier instead
temps[1] < 0
temps[2] < 0
temps[3] < 0


temps < 0   # vector of boolean values for each element in temps
temps > 60

which(temps < 0)    # returns index of values that are <0

#  for vectors             &    means  AND                 |        means         OR          

#  for single values      &&     means    AND              ||      means        OR




temps < 0 | temps > 60

which(temps < 0 | temps > 60)


any(temps<0 | temps> 60)         #       asking if any of the values are outliiers


all(temps < 0 | temps > 60)       #      asking if all of the values are outliers



temps[which(temps<0 | temps > 60)]       #    gives the outliers

temps[-which(temps < 0 | temps > 60)]      #  removing the outliers

temps[temps < 0 | temps > 60]   # simplified



filter <- temps<0 | temps > 60        # simplify
temps[filter] # same as above






filter <- !(temps<0 | temps > 60)        # inverting the expression so it gives not outliers
temps[filter] # not outliers

no_outliers <- temps[!(temps<0 | temps > 60)]
outliers <- temps[temps < 0 | temps > 60 ]




save(no_outliers, file = "no_outliers.Rdata")          # saving data file
