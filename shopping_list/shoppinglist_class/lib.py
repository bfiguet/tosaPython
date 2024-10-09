import logging
import os
import json

from constants import DATA_DIR

LOGGER = logging.getLogger()

class ShoppingList(list):
	def __init__(self, name):
		self.name = name

	def add_elem(self, elem):
		if not isinstance(elem, str):
			raise ValueError("You can add only ...")
		
		if elem in self:
			LOGGER.error(f"{elem} is already in list")
			return False
		
		self.append(elem)
		return True
	
	def del_elem(self, elem):
		if elem in self:
			self.remove(elem)
			return True
		return False
	
	def print_list(self):
		print(f"My shopping list of {self.name}:")
		for elem in self:
			print(f" - {elem}")
	
	def save_list(self):
		path = os.path.join(DATA_DIR, f"{self.name}.json")
		if not os.path.exists(DATA_DIR):
			os.makedirs(DATA_DIR)

		with open(path, "w") as f:
			json.dump(self, f, indent=4)

if __name__ == "__main__":
	shopping_list = ShoppingList("food")
	shopping_list.add_elem("Pommes")
	shopping_list.add_elem("Poires")
	shopping_list.add_elem("Abricots")
	shopping_list.save_list()
	shopping_list.print_list()
	shopping_list.del_elem("Pommes")
	shopping_list.del_elem("Bananes")
	shopping_list.save_list()
	shopping_list.print_list()

	toDoList = ShoppingList("toDo")
	toDoList.add_elem("finish the tutorial")
	toDoList.add_elem("Write an article")
	toDoList.add_elem("watch a movie")
	toDoList.save_list()
	toDoList.print_list()
	toDoList.del_elem("finish the tutorial")
	toDoList.del_elem("finish the tutorial")
	toDoList.save_list()
	toDoList.print_list()