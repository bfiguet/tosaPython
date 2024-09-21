def calculator():
	x = input ("Veuillez entrer le premier nombre : ")
	if x.isdigit() == True:
		y = input ("Veuillez entrer le deuxième nombre : ")
	if y.isdigit() == True:
		op = input ("Veuillez entrer l'opération à effectuer : ")
		x = int(x)
		y = int(y)
	
		if op == '+':
			print(x + y)
		elif op == '-':
			print(x - y)
		elif op == '*':
			print(x * y)
		elif op == '/':
			print(x / y)
		elif op == '**':
			print(x ** y)
		elif op == '//':
			print(x // y)
		else:
			print("l'Opérateur n'est pas encore gérer.")
	else:
		print("Il y a eu une erreur de saisie.\n")
	print("Merci pour votre participation!\n")
	res = input("Avez-vous un autre calcul a effectuer?\n Entrez 'oui' sinon laissez vide: ")
	if res == "oui":
		calculator()
	else:
		print("A Bientot!")	

print("Bienvenu à toi dans notre calculatrice")
calculator()