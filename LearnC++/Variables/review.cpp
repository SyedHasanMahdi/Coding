//
// Created by user on 29-Jun-26.
//
#include <iostream>

int main() {
    // Add your code below
    double weightE;
    double weightM;
    std::cout << "Enter the weight on Earth: ";
    std::cin >> weightE;

    weightM = weightE * 1.6/9.8;
    std::cout << "The item weighs " << weightM << " KG on Mars\n";

    double miles;
    double kilom;
    std::cout << "Enter the Miles: ";
    std::cin >> miles;

    kilom = miles * 1.609;
    std::cout << "The distance is " << kilom << " Kilometers\n";

}