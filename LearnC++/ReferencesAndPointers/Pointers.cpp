//
// Created by user on 15-Jul-26.
//
#include <iostream>
int main() {
  int gum = 8;

  // Create Pointer
  int *number;
  double *decimal;
  char *character;
  int *ptr = &gum;

  // int* makes it a pointer rather than a normal variable.
  // ptr is the pointer name.
  // &gum is the memory address of the other variable gum.
  // now ptr holds the memory address of the other variable gum

  int *number1;
  int *number2;
  int *number3;
  // the star can be placed anywhere between type and name

  // Dereferencing
  int blah = *ptr;
  // When * is used in a declaration, it creates a pointer
  // When * is not used in a declaration, it is a dereference operator

  // Null Pointer
  ptr = nullptr;

  int power = 9000;
  int *ptr1 = &power;
  std::cout << ptr1 << std::endl;
  std::cout << *ptr1 << "\n";
}