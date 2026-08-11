

# test-driven development believes that it is best to create a test before even wriotng the source code to be tested

test_that("`greet` says hello to a user", {
  expect_equal(greet("Carter"), "hello, Carter")
})



# the test is written before the code below
greet <- function(to= "world") {
  return(paste("hello,", to))
}
# the programmer knows what functionality they should implement.
# the benefit is that the functionality is immediately testable and further modifications must always pass the tests one has already written





# Behaviour-driven development is similar but has a greater focus on the behaviour of the function in context
# one might describe what we want the function to do by explicity naming what it should do
# test that has two functions for this:   describe and it

describe("greet()", {
  it("can say hello to a user", {
    name <- "Carter"
    expect_equal(greet(name), "hello, Carter")
  })
  it("can say hello to the world", {
    expect_equal(greet(), "hello, world")
  })
})



