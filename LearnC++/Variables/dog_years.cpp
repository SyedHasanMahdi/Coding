#include <iostream>

int main() {

    // initialise and declare
    int dog_age = 5;

    int early_years;
    int later_years;
    int human_years;

    // The first two years of a dog’s life count as 21 human years.
    early_years = 21;

    // Each following year counts as 4 human years.
    later_years = (dog_age-2) *4;

    human_years = early_years + later_years;

    std::cout << "My name is Dog! Ruff ruff, I am " << human_years << " years old in human years.\n";

}