import json

path = "/home/bland/Bureau/tosaPython/files/settings.json"
with open(path, "r") as f:
	settings = json.load(f)
	print(settings)
	print(settings.get("fondSize"))
	settings["fondSize"] = 10
	print(settings)

f = open(path, "r")
print(json.load(f))

with open(path, "w") as f:
	json.dump(settings, f, indent=4)