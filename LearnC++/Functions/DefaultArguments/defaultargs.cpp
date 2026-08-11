#include <iostream>
// Declaration
void intro(std::string name, std::string lang = "C++");

int add_nums(int num1, int num2 = 0);

int main() {
  intro("Mariel");
  // "Hi, my name is Mariel and I'm learning C++."

  intro("Mariel", "Python");
  // "Hi, my name is Mariel and I'm learning Python."
}

// Definition
void intro(std::string name, std::string lang) {
  std::cout << "Hi, my name is " << name << " and I'm learning " << lang
            << ".\n";
}