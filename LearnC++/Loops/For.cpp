
//
// Created by user on 30-Jun-26.
//
#include <iostream>

int main() {

    for (int i = 0; i < 10; i++) {

        std::cout << "I will not throw paper airplanes in class.\n";

    }
    // There are three separate parts to this separated by ;:
    //
    //     The initialization of a counter: int i = 0
    //     The continue condition: i < 20
    //     The change in the counter (in this case an increment): i++




    // repeat 99 times
    for (int i = 99; i > 0; i--) {
        std::cout << i << " bottles of pop on the wall.\n";
        std::cout << "Take one down and pass it around.\n";
        std::cout << i -1 << " bottles of pop on the wall.\n";
    }
}