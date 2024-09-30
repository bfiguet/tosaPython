from random import randint
from sys import exit


WELCOME = """*** Bienvenu dans le jeu du nombre mystère ***
Tu as 5 essais pour deviner le nombre mystère compris entre 0 et 100 inclus"""

def mystery_num():
	print(WELCOME)
	test = 5
	num = randint(0, 100)
	while test > 0:
		print(f"Il te reste {test} essai{'s' if test > 1 else ''}.")
		your_choice = input("Devine le nombre: ")

		if your_choice.isdigit():
			your_choice = int(your_choice)
			test -= 1
			if your_choice < num:
				print(f"Le nombre mystère est plus grand que {your_choice}")
			elif your_choice > num:
				print(f"Le nombre mystère est plus petit que {your_choice}")
			else:
				print("Vous avez Gagnez!!!!\n")
				break
		else:
			print("Veuillez saisir un nombre valide.\n")
	if test == 0:
		print(f"Dommage! Le nombre mystère était {num}\nGame Over!")


mystery_num()