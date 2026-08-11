//
// Created by user on 29-Jun-26.
//

#include <iostream>

int main () {

    // Declare a Variables
    int score;

    // Initialize a Variable
    score = 15;

    // Combine Declaration and Initialization
    int year = 2019;


    // Adding
    score = 4 + 2;

    // Subtracting
    score = 4 - 2;

    // Multiplying
    score  = 4 * 2;

    // Dividing
    score = 4 / 2;

    // Remainder
    score = 5 % 2;

    // Chaining the Output
    std::cout << "Player score: " << score << "\n";


    // Inputting Data
    int tip = 0;
    std::cout << "Enter tip amount: ";
    std::cin >> tip;
    std::cout << "You paid " << tip << " dollars.";
}