import json
path = "/home/bland/Bureau/tosaPython/files/data.json"
with open(path, "r") as f:
	data = json.load(f)
#print(data)
data.append(4)

with open(path, "w") as f:
	json.dump(data, f, indent=4)