import os
import shutil

for a in os.listdir("."):
	if not os.path.isdir(a):
		f = open(a, "r")
		file = f.read()
		file = file.replace("_static", "_static", 50000000)
		f.close()
		f = open(a, "w")
		f.write(file)
		f.close()
		