//
// Created by user on 15-Jul-26.
//
#include <iostream>

void swap_num(int &i, int &j) {

  int temp = i;
  i = j;
  j = temp;
}
int triple(int &i) {

  i = i * 3;

  return i;
}

int triple1(int const &i) {
  // the value of i doesnt change during the program so dont change the
  // reference as well
  return i * 3;
}

int main() {

  int songqiao = 10;
  int &sonny = songqiao;
  // sonny references songqiao
  // Anything we do to the reference also happens to the original.
  // Aliases cannot be changed to alias something else.

  int soda = 99;
  int &pop = soda;
  pop++;
  std::cout << soda << "\n"
            << pop
            << "\n"
               "";

  // same because added to both

  int a = 100;
  int b = 200;

  swap_num(a, b);

  std::cout << "A is " << a << "\n";
  std::cout << "B is " << b << "\n";
  // i and J will be modified but A and B will also be modified as the function
  // uses them as pass by reference parameters

  int num = 1;

  std::cout << triple(num) << "\n";
  std::cout << triple(num) << "\n";

  double const pi = 3.14;
  // if we try to pass this to the function it will throw error

  int porcupine_count = 3;
  std::cout << &porcupine_count << "\n"; // returns the memory address

// When & is used in a declaration, it is a reference operator.
// When & is not used in a declaration, it is an address operator.
}