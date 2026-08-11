//
// Created by user on 13-Jul-26.
//

#include <iostream>
#include <vector>

int main() {
  // in arrays, you cant add or remove values but u can modify existing values

  // empty array of 4 elements that holds 0 as values
  int NumsEmpty[4];

  // Specified values with no need to specify the size
  int NumsSet[]{7, 8, 15, 16};

  char vowels[] = {'a', 'e', 'i', 'o', 'u'};
  std::cout << vowels[0] << "\n";

  // updates the value 'a' to 'r'
  vowels[0] = 'r';
  std::cout << vowels[0] << "\n";
}