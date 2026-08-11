//
// Created by user on 15-Jul-26.
//

#include "City.h"
#include <iostream>

int City::get_population() { return population; }
City::City(std::string new_name, int new_pop) {
  name = new_name;
  population = new_pop;
}
City::~City() {}
// or u can write it like this:
// City::City(std::string new_name, int new_pop) : name(new_name),
// population(new_pop) {}

int main() { City ankara("Ankara", 5445000); }