OP = ["+", "-", "*", "/", "//", "**", "%"]

def calculator():
	x = input ("Veuillez entrer le premier nombre : ")
	y = input ("Veuillez entrer le deuxième nombre : ")
	op = input ("Veuillez entrer l'opération à effectuer : ")
	if op not in OP:
		print(f"L'opérateur {op} n'est pas encore gérer.")
		calculator()
	
	if x.isdigit() and y.isdigit():
		print(eval(x + op + y))
	else:
		print("Veuillez saisir des nombres valides.\n")
		calculator()

	print("Merci pour votre participation!\n")
	again = input("Avez-vous un autre calcul a effectuer?\n o/n: ")
	if again == "n":
		print("A Bientot!")	
	else:
		calculator()
	

print("Bienvenu à toi dans notre calculatrice")
calculator()