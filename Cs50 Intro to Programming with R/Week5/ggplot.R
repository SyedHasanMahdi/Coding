library(tidyverse)
#plot in ggplot means that we are going to plot our data.
#gg in ggplot references a grammar of graphics where individual components of graphics can be gathered together to visualize data.
#geometries. These are the various types of graphical representation options for plots. These include columns, points, and lines.
#aesthetic mappings are the relationships between the data and visual features of our plot


votes <- read.csv('votes.csv')

ggplot(votes, aes(x = candidate, y = votes)) +       # the + adds a layer on top of the base layer of our plot
  geom_col()






# it has decided that values of votes have an axis range from 0 to 200 but we could go till 250 if we want
# scales are continuos so they range from one number ot another, or discrete which means they are categorical
# continuous scales have limits
ggplot(votes, aes(x = candidate, y = votes)) +
  geom_col() +
  scale_y_continuous(limits = c(0, 250)) # this is provided by anothe layer so uses the + again





#adding labels
ggplot(votes, aes(x = candidate, y = votes)) +
  geom_col() +
  scale_y_continuous(limits = c(0, 250)) +
  labs(
    x = "Candidate",
    y = "Votes", 
    title = "Election Results"
  )




# fill colour can also be changes for example based on the candidate name


ggplot(votes, aes(x = candidate, y = votes)) +
  geom_col(aes(fill = candidate)) +
  scale_y_continuous(limits = c(0, 250)) +
  labs(
    x = "Candidate",
    y = "Votes",
    title = "Election Results"
  )


# to cater for colour blindness
ggplot(votes, aes(x = candidate, y = votes)) +
  geom_col(aes(fill = candidate)) +
  scale_fill_viridis_d("Candidate") +
  scale_y_continuous(limits = c(0, 250)) +
  labs(
    x = "Candidate",
    y = "Votes",
    title = "Election Results"
  )





# you can also modify the themes used by the ggplot
ggplot(votes, aes(x = candidate, y = votes)) +
  geom_col(aes(fill = candidate)) +
  scale_fill_viridis_d("Candidate") +
  scale_y_continuous(limits = c(0, 250)) +
  labs(
    x = "Candidate",
    y = "Votes",
    title = "Election Results"
  ) +
  theme_classic()

#theme_gray() The signature ggplot2 theme with a grey background and white grid lines, designed to put the data forward yet make comparisons easy.
#theme_bw() The classic dark-on-light ggplot2 theme. May work better for presentations displayed with a projector.
#theme_linedraw() A theme with only black lines of various widths on white backgrounds, reminiscent of a line drawing. Serves a purpose similar to theme_bw(). Note that this theme has some very thin lines (<< 1 pt) which some journals may refuse.
#theme_light() A theme similar to theme_linedraw() but with light grey lines and axes, to direct more attention towards the data.
#theme_dark() The dark cousin of theme_light(), with similar line sizes but a dark background. Useful to make thin colored lines pop out.
#theme_minimal() A minimalistic theme with no background annotations.
#theme_classic() A classic-looking theme, with x and y axis lines and no grid lines.
#theme_void() A completely empty theme.
#theme_test() A theme for visual unit tests. It should ideally never change except for new features.







# saving your plot
p <- ggplot(votes, aes(x = candidate, y = votes)) +
  geom_col(aes(fill = candidate)) +
  scale_fill_viridis_d("Candidate") +
  scale_y_continuous(limits = c(0, 250)) +
  labs(
    x = "Candidate",
    y = "Votes",
    title = "Election Results"
  ) +
  theme_classic()

ggsave(
  "votes.png",
  plot = p,
  width = 1200,
  height = 900,
  units = "px"
)







# new type of geometry called point
# percentiles are shown
load("candy.RData")

ggplot(
  candy,
  aes(x = price_percentile, y = sugar_percentile)
) +
  geom_point() +
  labs(
    x = "Price",
    y = "Sugar",
    title = "Price and Sugar"
  ) +
  theme_classic()






# some of the points overlap on each other so there's a better visual representation of them
ggplot(
  candy,
  aes(x = price_percentile, y = sugar_percentile)
) +
  geom_jitter() +
  labs(
    x = "Price",
    y = "Sugar",
    title = "Price and Sugar"
  ) +
  theme_classic()











# we can also add color aesthetics

ggplot(
  candy,
  aes(x = price_percentile, y = sugar_percentile)
) +
  geom_jitter(
    color = "darkorchid",
    size = 2
  ) +
  labs(
    x = "Price",
    y = "Sugar",
    title = "Price and Sugar"
  ) +
  theme_classic()









# we can also change the size and shape of the points
# view more at https://ggplot2.tidyverse.org/articles/ggplot2-specs.html#sec:shape-spec


ggplot(
  candy,
  aes(x = price_percentile, y = sugar_percentile)
) +
  geom_jitter(
    color = "darkorchid",
    fill = "orchid",
    shape = 21,
    size = 2
  ) +
  labs(
    x = "Price",
    y = "Sugar",
    title = "Price and Sugar"
  ) +
  theme_classic()







# How to visualize over time 
load("anita.RData")
ggplot(anita, aes(x= timestamp, y = wind)) +
  geom_line() +
  geom_point( color = "deepskyblue4")         # combine two different plots on one



# we can also modify the aesthetics seperately
ggplot(anita, aes(x= timestamp, y = wind)) +
  geom_line(
    linetype = 1,
    linewidth = 0.5
  ) +
  geom_point( 
    color = "deepskyblue4", 
    size = 5
  ) +
  labs(
    x = "Date", 
    y = 'Wind Speed (Knots)',
    title = "Hurricane Anita"
  ) +
  theme_classic()







# we can also finally add a horizontal line to show when the hurricane got its hurricane status
# learn more about the line aesthetics at https://ggplot2.tidyverse.org/reference/aes_linetype_size_shape.html#linetype
ggplot(anita, aes(x= timestamp, y = wind)) +
  geom_line(
    linetype = 1,
    linewidth = 0.5
  ) +
  geom_point( 
    color = "deepskyblue4", 
    size = 5
  ) +
  geom_hline(
    linetype = 3,
    linewidth = 2,
    yintercept = 64 # by definition of a hurricane it requires 64 knots to be classified as an actual hurricane
  ) +
  labs(
    x = "Date", 
    y = 'Wind Speed (Knots)',
    title = "Hurricane Anita"
  ) +
  theme_classic()
