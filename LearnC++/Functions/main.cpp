#include <iostream>

// Add declarations here:
double average(double num1, double num2);
int tenth_power(int num);
bool is_palindrome(std::string text);

int main() {

  std::cout << is_palindrome("racecar") << "\n";
  std::cout << tenth_power(3) << "\n";
  std::cout << average(8.0, 19.0) << "\n";
}

// You can define the functions in another file.
// you just need to declare them at the top in this main file
// When compiling you will use multiplpe files so use the following command:
// g++ main.cpp my_functions.cpp