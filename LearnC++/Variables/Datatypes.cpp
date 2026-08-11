//
// Created by user on 30-Jun-26.
//
#include <iostream>
int main() {
    int age = 28;          // integer
    std::cout << age ;

    double price = 8.99;    // double/float/decimal
    std::cout << price;

    char grade = 'A'; // character
    std::cout << grade;

    std::string message = "Game Over";  // string
    std::cout << message;

    bool late_to_work = true;       // boolean
    std::cout << late_to_work;


    // There are some data type modifiers which modify the length of data that a particular data type can hold
    // These include:
    //                  signed
    //                  unsigned
    //                  short
    //                  long

    // constant can be declared by const
    const double quarter = 0.25;
    std::cout << quarter;
    // the value can not be changed


    // Type conversion
    // (type) value                means convert value to type.
    double weight1;
    int weight2;

    weight1 = 154.49;
    std::cout << weight1;
    weight2 = (int) weight1;
    std::cout << weight2;
    // it converts the value of weight 1 to an integer which only takes the whole number part so just 154

}
