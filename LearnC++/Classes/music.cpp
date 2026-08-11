#include "song.h"
#include <iostream>

int main() {
  Song electric_relaxation("Back to Black", "Amy Winehouse");
  electric_relaxation.add_title("Electric Relaxation");
  std::cout << electric_relaxation.get_title() << "\n";

  electric_relaxation.add_artist("A Tribe Called Quest");
  std::cout << electric_relaxation.get_artist() << "\n";

  Song back_to_black("Back to Black", "Amy Winehouse");

  std::cout << back_to_black.get_title() << "\n";
  std::cout << back_to_black.get_artist();

}