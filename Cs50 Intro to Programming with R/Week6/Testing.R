source("Exceptions.R")
# writing a test functions

test_average <- function() {
  if (average(c(1, 2, 3)) == 2) {
    cat("'average' passeed test :)\n")
  } else {
    cat("'average' failed test :(\n")
  }
}

test_average()




#testing negative values
test_average2 <- function() {
  if (average(c(1, 2, 3)) == 2) {
    cat("`average` passed test :)\n")
  } else {
    cat("`average` failed test :(\n")
  }
  
  if (average(c(-1, -2, -3)) == -2) {
    cat("`average` passed test :)\n")
  } else {
    cat("`average` failed test :(\n")
  }
  
  if (average(c(-1, 0, 1)) == 0) {
    cat("`average` passed test :)\n")
  } else {
    cat("`average` failed test :(\n")
  }
}

test_average2()



# we have written too many lines of code for this already so theres a fix for this
# the testthat package is used to test R code
library(testthat)
test_that("`average` calculates mean", {
  expect_equal(average(c(1, 2, 3)), 2)
  expect_equal(average(c(-1, -2, -3)), -2)
  expect_equal(average(c(-1, 0, 1)), 0)
  expect_equal(average(c(-2, -1, 1, 2)), 0)
})

test_that("`average` warns about NAs in input", {
  expect_warning(average(c(1, NA, 3)))
  expect_warning(average(c(NA, NA, NA)))
})



# our order of if statements in average function are out of order so lets change it
average <- function(x) {
  if (any(is.na(x))) {
    warning("'x' contains one or more NA Values")
    return(NA)
  }
  if (!is.numeric(x)) {
    stop("`x` must be a numeric vector.")
  }
  sum(x) / length(x)
}


test_that("`average` returns NA with NAs in input", {
  expect_equal(suppressWarnings(average(c(1, NA, 3))), NA)
  expect_equal(suppressWarnings(average(c(NA, NA, NA))), NA)
})

test_that("`average` warns about NAs in input", {
  expect_warning(average(c(1, NA, 3)))
  expect_warning(average(c(NA, NA, NA)))
})





# we can also use expect_error and expect_no_error
test_that("`average` stops if `x` is non-numeric", {
  expect_error(average(c("quack!")))
  expect_error(average(c("1", "2", "3")))
})



# testing floating point input
test_that("`average` calculates mean", {
  expect_equal(average(c(0.1, 0.5)), 0.3)
})


# floating point values are subject to imprecision  since they arent represented exactly
print(0.3, digits = 17)
# the expect equal function has acceptable tolerance provided in order to avoid confusing 0.3 = 0.299999999
# u can change the tolerance by passing tolerance argument
