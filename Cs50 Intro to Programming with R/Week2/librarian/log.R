authors <- read.csv("authors.csv")
books <- read.csv("books.csv")

# finding books where the author is Mia morgan
print(subset(books, author == "Mia Morgan"))

# subsetting to find the year and the topic
found2 <- subset(books, year == 1613)
found2 <- subset(found2, topic == "Music")

# filtering the author and year
filter <- (books$author == "Lysandra Silverleaf" | books$author == "Elena Petrova") & books$year == 1775
books[filter, ]


# filtering the pages, topic and year
filter <- books$pages >= 200 & books$pages <= 300 & books$topic == "Art"  & (books$year == 1990 | books$year ==1992)
books[filter, ]

# filtering for the word Quantum mechanics in the title
filter <- grepl("Quantum Mechanics", books$title)
books[filter, ]

# finding authors from Zenthia and then finding a book published in 1700 by any of those authors
auth_filter<- authors$hometown == "Zenthia"
valid_authors <- authors[auth_filter, 1]
filter<- books$author %in% valid_authors & books$year >=1700 & books$year <= 1800
books[filter, ]
