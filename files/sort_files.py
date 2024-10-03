from pathlib import Path

DIC = {".mp3": "Musique", ".wav": "Musique", ".flac": "Musique", 
	   ".avi": "Videos", ".mp4": "Videos", ".gif": "Videos", 
	   ".bmp": "Images", ".png": "Images", ".jpg": "Images", 
	   ".txt": "Documents", ".pptx": "Documents", ".csv": "Documents", ".xls": "Documents", ".odp": "Documents", ".pdf": "Documents", ".pages": "Documents"}

def sort_files():
	
	#Obtenir le chemin absolu du répertoire "data"
	#BASE_DIR = Path('/home/bland/Bureau/tosaPython/files/data')
	BASE_DIR = Path(__file__).parent.resolve()
	source_dir = BASE_DIR / "data"
	
	#check if 'data' directory exist
	if not source_dir.is_dir():
		print(f"Error: 'data' directory not found in {BASE_DIR}")

	files = [f for f in BASE_DIR.iterdir() if f.is_file()]
	for file in files:
		data = DIC.get(file.suffix, 'Divers')
		data_path = BASE_DIR / data
		data_path.mkdir(exist_ok=True)
		file_path = data_path / file.name
		file.rename(file_path)

		

#from os import makedirs, rename, getcwd, chdir

#MUSIQUE = [".mp3", ".wav", ".flac"]
#VIDEO = [".avi", ".mp4", ".gif"]
#IMAGES = [".bmp", ".png", ".jpg"]
#DOCUMENTS = [".txt", ".pptx", ".csv", ".xls", ".odp", ".pdf", ".pages"]

#def sort_files():
#	try:
#		p = Path('./data')
#		data = [x for x in p.iterdir() if not x.is_dir()]
#		chdir("data")
#		makedirs('Musique', exist_ok=True) 
#		makedirs('Videos', exist_ok=True)
#		makedirs('Images', exist_ok=True)
#		makedirs('Documents', exist_ok=True)
#		makedirs('Divers', exist_ok=True)
		
#		for val in data:
#			cur_path = Path.cwd().joinpath(val.name)
#			if val.suffix in MUSIQUE:
#				new_path = Path.cwd().joinpath('Musique', val.name)
#			elif val.suffix in VIDEO:
#				new_path = Path.cwd().joinpath('Videos', val.name)
#			elif val.suffix in IMAGES:
#				new_path = Path.cwd().joinpath('Images', val.name)
#			elif val.suffix in DOCUMENTS:
#				new_path = Path.cwd().joinpath('Documents', val.name)
#			else:
#				new_path = Path.cwd().joinpath('Divers', val.name)
#			cur_path.rename(new_path)
#	except:
#		print("Error: 'data' directory not found")
		

sort_files()

