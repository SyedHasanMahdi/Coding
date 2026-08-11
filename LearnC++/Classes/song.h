//
// Created by user on 15-Jul-26.
//

#ifndef LEARNC___SONG_H
#define LEARNC___SONG_H
#include <string>

// add the Song class here:
class Song {

  // Private Attribute
  std::string title;

public:
  void add_title(std::string new_title);
  std::string get_title();

  // Public Attribute
  std::string artist;

  void add_artist(std::string new_artist);
  std::string get_artist();

// Constructor:
  Song(std::string newtitle, std::string new_artist);

  // Destructor
  ~Song();
};
#endif // LEARNC___SONG_H