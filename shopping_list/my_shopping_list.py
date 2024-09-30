
def my_shoppinglist():
	my_list = []

	while True:
		print(f"\nChoisissez parmi les 5 options suivantes :\n1: Ajouter un element à la liste\n2: Retirer un élément à la liste\n3: Afficher la liste\n4: Vider la liste\n5: Quitter")

		choice = input("👉 Votre choix : ")
		if choice == '1':
			new_element = input("\nEntrez le nom d'un élément à ajouter à la liste de course: ")
			my_list.append(new_element)			
		elif choice == '2':
			remove_element = input("\nEntrez le nom de l'élément à retirer de la liste de course: ")
			if remove_element in my_list:
				my_list.remove(remove_element)
				print(f"\nL'élément {remove_element} a bien été supprimé de la liste.\n")
			else:
				print(f"\nL'élément {remove_element} n'est pas dans la liste\n")
		elif choice == '3':
			if my_list:
				for i, element in enumerate(my_list, 1):
					print(f"{i}. {element}")
			else:
				print("\nLa liste ne contient aucun élément.\n")
		elif choice == '4':
			my_list.clear()
			print("\nLa liste a été vidée de son contenu.\n")
		elif choice == '5':
			print("\nMerci d'avoir utiliser notre shoppinglist!\n")
			break

my_shoppinglist()