// You don't need to always have the declarations at the top of the main
// Well, you can take those function declarations and move them all over to a
// header file, another file — usually with the same name as the file with all
// the function definitions — with the extension .hpp or .h. For example, if
// your function definitions are in my_functions.cpp, the corresponding header
// file would be my_functions.hpp or my_functions.h.
#include "my_functions.h"
int main() {
  std::cout << is_palindrome("noon") << "\n";
  std::cout << tenth_power(4) << "\n";
  std::cout << average(4.0, 7.0) << "\n";
}