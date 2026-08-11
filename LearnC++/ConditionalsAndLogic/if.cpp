#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    // Create a number that's 0 or 1

    srand (time(nullptr));
    int	coin = rand() % 2;

    // If number is 0: Heads
    // If it is not 0: Tails

    if (coin == 0) {

        std::cout << "Heads\n";

    }
    else {

        std::cout << "Tails\n";

    }

    // an if statement is used to test an expression
    int grade = 90;

    if (grade > 60) {
        std::cout << "Pass";
    }

    // there are some relational operators to compare values
    // These include:
    // ++ equal to
    // != not equal to
    // > greater than
    // < less than
    // >= greater than or equal to
    // <= less than or equal to

    int marks = 59;

    if (marks > 60) {
        std::cout << "Pass\n";
    } else {
        std::cout << "Fail\n";
    }


    double ph = 4.6;

    // Write the if, else if, else here:
    if (ph > 7) {
        std::cout << "Basic";
    }
    else if (ph < 7) {
        std::cout << "Acidic";
    }
    else {
        std::cout << "Neutral";
    }



    // Theres a function called swithc which provides an alternative syntax that is easier to read and write
    // this is used when there are multiple outcomes in our program
    grade = 11;
    switch (grade) {
        case 9:
            std::cout << "Freshman\n";
            break;
        case 10:
            std::cout << "Sophomore\n";
            break;
        case 11:
            std::cout << "Junior\n";
            break;
        case 12:
            std::cout << "Senior\n";
            break;
        default:
            std::cout << "Invalid\n";
    }
    // One restriction on this expression is that it must evaluate to an integral type (int, char, short, long, long long, or enum

}