//
// Created by user on 15-Jul-26.
//
#include <iostream>

void print_cat_ears(char let) {
  std::cout << " " << let << "   " << let << " " << "\n";
  std::cout << let << let << let << " " << let << let << let << "\n";
}

void print_cat_ears(int num) {
  std::cout << " " << num << "   " << num << " " << "\n";
  std::cout << num << num << num << " " << num << num << num << "\n";
}


// can take int or char as a parameter


int main() {
  print_cat_ears('A');
  print_cat_ears(4);
}