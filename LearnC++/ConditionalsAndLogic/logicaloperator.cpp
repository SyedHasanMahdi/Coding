//
// Created by user on 30-Jun-26.
//
// There are three logical operators that we will cover:
//     &&: the and logical operator
//     ||: the or logical operator
//     !: the not logical operator

#include <iostream>
int main() {
    int hunger = true;
    int anger = true;

    if (hunger == true && anger == true) {
        std::cout << "Hangry";
    }

    int day = 6;

    if (day ==6 || day == 7) {
        std::cout << "Weekend";
    }


    bool logged_in = false;

    if (!logged_in) {
        std::cout << "Try again";
    }
}