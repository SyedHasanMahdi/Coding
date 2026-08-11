# exception handling


#finding the average of a vector
average <- function(x) {
  if (!is.numeric(x)) {         # if the values arent numbers theres no need to perform the calculation  
    return(NA)
  } else {
    sum(x) / length(x)
  }
}


# using the message function so that our program alerts the user
average <- function(x) {
  if (!is.numeric(x)) {
    message("'x' must be a numericvector. Returning NA instead.")
    return(NA)
  } else {
    sum(x) / length(x)
  }
}
# message is usually for when something goes correctly
# use the warning instead
average <- function(x) {
  if (!is.numeric(x)) {
    warning("'x' must be a numericvector. Returning NA instead.")
    return(NA)
  } else {
    sum(x) / length(x)
  }
}


# we can also use the stop function when we ant to completely stop the functions.
average <- function(x) {
  if (!is.numeric(x)) {
    stop("`x` must be a numeric vector.")
  }
  sum(x) / length(x)
}




# we can also combine the stop and warning such as when code looks at both situations where there are no values or there are non numeric values
average <- function(x) {
  if (!is.numeric(x)) {
    stop("`x` must be a numeric vector.")
  }
  if (any(is.na(x))) {
    warning("'x' contains one or more NA Values")
    return(NA)
  }
  sum(x) / length(x)
}




