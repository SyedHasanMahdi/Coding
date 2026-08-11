//
// Created by user on 15-Jul-26.
//
#include <iostream>
template <typename T> void print_cat_ears(T item) {

  std::cout << " " << item << "   " << item << " " << "\n";
  std::cout << item << item << item << " " << item << item << item << "\n";
}

int main() {
  print_cat_ears(2);

  // the output:
  //  2   2
  // 222 222
}

// this way we4 can use any parameter type we want as long as it can be used
// with the methods expected

// Note: Using templates will slow down the program’s compile time, but speed up the execution time