//
// Created by user on 13-Jul-26.
//

#include <cmath>
#include <iostream>
#include <vector>

// structure of a functions declaration
// return_type function_name( any, parameters, you, have ) {
//
//   // Code block here
//
//   return output_if_there_is_any;
//
// }

void make_sandwich() {

  std::cout << "bread\n";
  std::cout << "egg\n";
  std::cout << "cheese\n";
  std::cout << "avocado\n";
  std::cout << "bread\n";
}

std::string always_blue() {

  std::cout << "Returned blue!";

  return "blue!\n";
}

double get_tip(double price) { return price * 0.2; }

double get_tip(double price, double tip, bool total_included) {

  if (total_included) {

    return price * tip + price;

  } else {

    return price * tip;
  }
}

void name_x_times(std::string name, int x) {
  while (x > 0) {
    std::cout << name;
    x -= 1;
  }
}

int tenth_power(int num) { return pow(num, 10); }

std::vector<int> first_three_multiples(int num) {

  std::vector<int> multiples{num, num * 2, num * 3};

  return multiples;
}

std::string needs_water(int days, bool is_succulent) {
  if (is_succulent == false & days > 3) {
    return "Time to water the plant";
  } else if (is_succulent & days <= 12) {
    return "Don't water the plant!";
  } else if (is_succulent & days >= 13) {
    return "Go ahead and give the plant a little water.";
  } else {
    return "Don't water the plant!";
  }
}

bool is_palindrome(std::string text) {

  std::string reversed_text = "";

  for (int i = text.size() - 1; i >= 0; i--) {
    reversed_text += text[i];
  }

  if (reversed_text == text) {
    return true;
  }

  return false;
}

int main() {
  // function sqrt which returns the square root. its built in to the Cmath
  // import
  std::cout << sqrt(9) << "\n";

  // this seeds the random number generator
  srand(time(NULL));
  int the_amazing_random_number = rand() % 29;
  std::cout << the_amazing_random_number << "\n";

  make_sandwich();

  // output from the std::cout in the function declaration
  always_blue();

  // output the return value
  std::cout << always_blue() << "\n";

  // passing parameters
  double tip = get_tip(15.75);
  std::cout << tip << "\n";
  // tip would be 3.15

  tip = get_tip(45.50, 0.25, true);
  std::cout << tip << "\n";
  // this code results in 56.875, which you could round up to 56.88

  std::string my_name = "Add your name here!\n";
  int some_number = 5; // Change this if you like!
  // Call name_x_times() below with my_name and some_number

  name_x_times(my_name, some_number);

  std::cout << tenth_power(0) << "\n";
  std::cout << tenth_power(1) << "\n";
  std::cout << tenth_power(2) << "\n";

  for (int element : first_three_multiples(8)) {
    std::cout << element << "\n";
  }

  std::cout << needs_water(10, false) << "\n";

  std::cout << is_palindrome("madam") << "\n";
  std::cout << is_palindrome("ada") << "\n";
  std::cout << is_palindrome("lovelace") << "\n";
}