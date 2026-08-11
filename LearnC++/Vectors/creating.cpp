//
// Created by user on 06-Jul-26.
//
#include <iostream>
#include <vector>

int main() {

  // creating
  std::vector<int> name;

  // creating and initialising
  std::vector<double> location = {42.651443, -73.749302};

  // Presizing or setting the size to limit number of elements
  std::vector<double> two(2);
  // empty vector of 2 elements

  // Accessing individual elements
  std::vector<char> vowels = {'a', 'e', 'i', 'o', 'u'};

  std::cout << vowels[0] << "\n";
  std::cout << vowels[1] << "\n";
  std::cout << vowels[2] << "\n";
  std::cout << vowels[3] << "\n";
  std::cout << vowels[4] << "\n";

  // Adding and removing elements

  std::vector<std::string> dna = {"ATG", "ACG"};
  // adding
  dna.push_back("GTG");
  dna.push_back("CTG");
  // removing last thing
  dna.pop_back();

  std::vector<std::string> grocery = {"Hot Pepper Jam", "Dragon Fruit",
                                      "Brussel Sprouts"};
  // Output the number of elements (3)
  std::cout << grocery.size() << "\n";

  // looping through the vector
  std::vector<double> delivery_order;
  delivery_order.push_back(8.99);
  delivery_order.push_back(2.55);
  delivery_order.push_back(3.32);
  delivery_order.push_back(4.45);

  double total = 0;
  for (int i = 0; i < delivery_order.size(); i++) {
    total += delivery_order[i];
  }
  std::cout << total << "\n";
}