# Demonstrates updated markup, including specifying arguments

\name{ducksay}
\alias{ducksay}
\title{Duck Say}
\description{A duck that says hello.}
\usage{
ducksay(phrase = "hello, world")
}
\arguments{
\item{phrase}{The phrase for the duck to say.}
}
\value{
A string representation of a duck saying the given phrase.
}
\examples{
cat(ducksay())
cat(ducksay("quack!"))
}