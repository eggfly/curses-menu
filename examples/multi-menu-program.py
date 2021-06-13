import os

import cursesmenu.utils
from cursesmenu import CursesMenu
from cursesmenu.curses_menu import MenuItem


def main():
    menu1 = CursesMenu("Menu 1")
    item1 = MenuItem("Item 1", menu1, should_exit=True)
    menu1.append_item(item1)
    menu1.show()
    i = input("Enter some input:")
    menu2 = CursesMenu("Menu 2")
    item2 = MenuItem("Item 2", menu2, should_exit=True)
    menu2.append_item(item2)

    menu2.show()


if __name__ == "__main__":
    main()
