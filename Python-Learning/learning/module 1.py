import draw
from draw import draw_game


def play_game():
    ...


def main():
    result = play_game()
    draw.draw_game(result)


# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()


def main():
    result = play_game()
    draw_game(result)


from draw import *


# Importing all objects from a module


def main():
    result = play_game()
    draw_game(result)


# import the draw module
from draw import draw_game


def main():
    result = play_game()
    draw_game(result)


# if u want to import a module conditionally with same name
if visual_mode:
    import draw_visual as draw
else:
    import draw_textual as draw


def main():
    result = play_game()
    draw.draw_game(result)


sys.path.append("/foo")
# This will add the foo directory to the list of paths to
# look for modules in as well.


