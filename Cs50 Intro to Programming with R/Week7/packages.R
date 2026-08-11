#dir.create("ducksay")
#setwd("ducksay")

# packages generally have the following structure
#DESCRIPTION
#NAMESPACE
#man/
#  R/
#  tests/


#The DESCRIPTION file will include a description of the package, including who wrote it. 
#The NAMESPACE file will include a list of functions we want to make available to the users of our package. 
#man is a folder that holds the manual (documentation) for the package. 
#R includes the R code for the package. 
#Finally, tests holds all the tests that we want to be able to run to ensure our package behaves as we expect.










#We can create a DESCRIPTION file by typing file.create("DESCRIPTION") into the R console. We can now open this file and code as follows:

# Demonstrates required components of a DESCRIPTION file

#  Package: ducksay
#Title: Duck Say
#Description: Say hello with a duck.
#Version: 1.0
#Authors@R: person("Carter", "Zenke", email = "carter@cs50.harvard.edu", role = c("aut", "cre", "cph"))
#License: MIT + file LICENSE


#Notice how the package is named and titled. Then, a description is provided. Authors are included.
#Finally, the license is provided under which this package is offered. 









#As you can see by the DESCRIPTION file above, we also need a LICENSE file. We can code that as follows:

# Demonstrates adding on to a license template

#  YEAR: ...
#COPYRIGHT HOLDER: ducksay authors

#Fill in the ... with the present year. Notice how the year of the license and the copyright holder is named.






#A package called devtools allows us to create packages faster.
#In particular, devtools comes with utilities for creating the necessary folder structure for our package’s tests and R code.
#We can load devtools by typing library(devtools) into the R console, assuming it’s already installed.





#Writing Tests

#Thanks to the devtools package, we can easily use testthat to develop tests for packages we author.

#Then, we can type use_testthat() to invoke the ability to use testthat. Our DESCRIPTION file will be automatically modified as follows:

# Demonstrates suggesting a dependency, for testing's sake

#  Package: ducksay
#Title: Duck Say
#Description: Say hello with a duck.
#Version: 1.0
#Authors@R: person("Carter", "Zenke", email = "carter@cs50.harvard.edu", role = c("aut", "cre", "cph"))
#License: MIT + file LICENSE
#Suggests:
#  testthat (>= 3.0.0)
#Config/testthat/edition: 3

#Notice that the package will suggest that one should have testthat version 3.0.0 or above installed. This may vary depending on the version of testthat that you’ve installed.

#Inside our tests/testthat folder, created by use_testthat, we can create our first test, test-ducksay.R, as follows:
  
  # Demonstrates describing behavior of `ducksay`
  
 # describe("ducksay()", {
#  it("can print to the console with `cat`", {
#      expect_output(cat(ducksay()))
#    })
#    it("can say hello to the world", {
#      expect_match(ducksay(), "hello, world")
#    })
#  })

#Notice that expect_match looks for the string hello, world in the output of ducksay.
