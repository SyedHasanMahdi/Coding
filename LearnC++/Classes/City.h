//
// Created by user on 15-Jul-26.
//

#ifndef LEARNC___CITY_H
#define LEARNC___CITY_H
#include <iostream>
class City {

  // attribute
  std::string name;
  int population = 0;

  // we'll explain 'public' later
public:
  // method
  void add_resident() { population++; }
  int get_population();
  City(std::string new_name, int new_pop);
  ~City();
};

#endif // LEARNC___CITY_H