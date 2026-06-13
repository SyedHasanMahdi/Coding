def my_function():
    print("Hello From My Function!")


def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s" % (username, greeting))


def sum_of_two_numbers(a, b):
    return a + b


# calling functions
my_function()

my_function_with_args("John Doe", "a great year!")
x = sum_of_two_numbers(1, 2)


def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"


def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()