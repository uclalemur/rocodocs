import os
import shutil

for a in os.listdir("_static"):
	shutil.move(os.path.join(os.getcwd(), os.path.join("_static", a)), os.path.join(os.getcwd(), "_static" + a))