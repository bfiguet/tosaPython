path = "/home/bland/Bureau/tosaPython/files/text.txt"
#print(path)

#f = open(path, "r")
#print(f.read())
#f.seek(0) # revenir au debut du fichier
#content = f.read()
#print(content)
#f.close()

#ouvrir avec open ds le bloc et close automatiquement a la fin du bloc
with open(path, "r") as f:
	#content = f.read()
	#content = repr(f.read()) #affiche le \n mais ne l'interprete pas
	#content = f.readlines() #transforme chaq ligne en liste AVEC le \n
	content = f.read().splitlines() #transforme chaq lign en liste SANS le \n
	print(content)

#ici w ecrit et ecrase tout ce qu'il y avait
#with open(path, "w") as f:
#	f.write("Hello!")

#ecrit a la fin du fichier (append)
with open(path, "a") as f:
	f.write("\nHello je suis dans le fichier!")

