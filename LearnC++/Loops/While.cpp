//
// Created by user on 30-Jun-26.
//
#include <iostream>

int main() {

    int pin = 0;
    int tries = 0;

    std::cout << "BANK OF CODECADEMY\n";

    std::cout << "Enter your PIN: ";
    std::cin >> pin;

    tries++;

    while (pin != 1234 && tries < 3) {

        std::cout << "Enter your PIN: ";
        std::cin >> pin;
        tries++;

    }

    if (pin == 1234) {

        std::cout << "PIN accepted!\n";
        std::cout << "You now have access.\n";

    }


    int guess;

    int attempts = 0;

    std::cout << "I have a number 1-10.\n";
    std::cout << "Please guess it: ";
    std::cin >> guess;

    // Write a while loop here:

    while (guess != 8 && attempts < 50) {

        std::cout << "Wrong guess, try again: ";
        std::cin >> guess;

        attempts++;

    }

    if (guess == 8) {

        std::cout << "You got it!\n";

    }




    int i = 0;
    int square = 0;


    while (i <10) {
        square = i*i;
        std::cout << i << " " << square << "\n";
        i++;
    }
}