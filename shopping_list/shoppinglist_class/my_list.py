import logging
import os
import json

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CUR_DIR, "data")

LOGGER = logging.getLogger()


class MyList(list):
    def __init__(self, name):
        self.name = name
        print(f'Your list "{self.name}" has been created successfully!')

    def your_choices(self):
        while True:
            print(f"\nChoose from the following 5 options:\n1: Add an item to the list\n2: Remove an item from the list\n3: Show the list\n4: Empty the list\n5: Exit")
            choice = input("👉 Votre choix : ")
            if choice == '1':
                new_item = input("What do you want add? 👉 ")
                self.add_item(new_item)
            elif choice == '2':
                del_item = input("What do you want remove? 👉 ")
                self.del_item(del_item)
            elif choice == '3':
                self.print_list()
            elif choice == '4':
                self.clear()
                self.save_list()
                print("\nYour list has been emptied of its contents.\n")
            elif choice == '5':
                print("\nThank you for using our list generator!\n")
                break
            print("~" * 400)

    def add_item(self, item):
        if not isinstance(item, str):
            LOGGER.error(f'\nYou can add only text not "{item}".\n')
            return False

        if item in self:
            LOGGER.error(f'\n"{item}" is already in list\n')
            return False

        self.append(item)
        print(f'\n"{item}" has been added to the list {self.name}\n')
        self.save_list()
        return True

    def del_item(self, item):
        if item in self:
            self.remove(item)
            self.save_list()
            return True
        LOGGER.error(f'\n"{item}" isn\'t in {self.name}.\n')
        return False

    def print_list(self):
        if self:
            print(f"\nMy shopping list of {self.name}:")
            for item in self:
                print(f" - {item}")
        else:
                print("\nYour list is empty.\n")
    def save_list(self):
        path = os.path.join(DATA_DIR, f"{self.name}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        with open(path, "w") as f:
            json.dump(self, f, indent=4)


if __name__ == "__main__":
    name = input("Hello! What's the name of the list do you want to create? 👉 ")
    new_list = MyList(name)
    new_list.your_choices()
