from random import randint

def war():
	my_life = enemy_life = 50
	my_potion = 3
	enemy_potion = 0
	skip_turn = False

	print(f"Bonjour👋, vous avez {my_life} point de vie et votre ennemi en a {enemy_life}.\nVous disposez de {my_potion} potion{'s' if my_potion > 0 else ''} 🍵 et l'ennemi de {enemy_potion} potion{'s' if enemy_potion > 0 else ''} 🍵.\nBonne chance!")

	while True:

		if skip_turn:
			print("Vous passez votre tour...")
			skip_turn = False
		else:
			action = ""
			while action not in ["1", "2"]:
				if my_potion <= 0:
					action = input("Souhaitez-vous attaquer (1) ? (Vous n'avez plus de potion) ")
				else:
					action = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
			if action == '1':
				domage = randint(5, 10)
				enemy_life -= domage
				print(f"Vous avez infligé {domage} points de dégats à l'ennemi.💥")
			elif action == '2' and my_potion > 0:
				potion = randint(15, 50)
				my_life += potion
				my_potion -= 1
				skip_turn = True
				print(f"Vous récupérez {potion} points de vie ({my_potion} potions restantes).")

		if enemy_life <= 0:
			print("Tu as gagné!!! 🥳\n")
			break
		
		domage = randint(5, 15)
		my_life -= domage
		print(f"L'ennemi vous a infligé {domage} points de dégats.💢 \n")
		
		if my_life <= 0:
			print("L'ennemi a gagné. Repose en Paix. 🙏")
			break

		print(f"Il vous reste {my_life} points de vie.")
		print(f"Il reste {enemy_life} points de vie à l'ennemi.")
		print("-" * 50)

	print("Fin du jeux. 🏆 \nMerci d'avoir participer!\n")

war()

