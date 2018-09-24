#Versionify
#Use case:
#1) Set file directory to read from
#2) Run script
#3) Script asks what you want to increment 
#3.5) Script asks what you want to increment to (string, int, float)
#4) Enter version number/text
#5) Spit out what is being changed from and to.
#6) BONUS: Create copy of file locally next to script

#read file, get version number, assign version_number

# input1, input2, input3 = str(input_version).split('.')
# major, minor, patch = str(version_number).split('.')
import os

current_dir = os.getcwd()
# Specify the directory to the file you want to overwrite
file_dir = "/Desktop/Versionify"
new_dir = current_dir+file_dir
#Specify the file name that you want to overwrite
file_name = "versions.json"
os.chdir(new_dir)

def test(old_version, new_version):
	
	with open(file_name) as f:
		content = f.readlines()
		content = [x.strip() for x in content]
		for n, i in enumerate(content):
			if i == old_version:
				print "Old version: " + content[n]
				content[n] = new_version
				print "New version: " + content[n]
				#Seems like replacing value works, but need to figure out how to write this into the
		# file_name.write(line.replace(old_version, new_version))

#Specify the old verion you want to replace
old_version = 'VERSION_NAME = "Alpha"'

#Specify the new version you want to use
new_version = 'VERSION_NAME = "Beta"'

test(old_version, new_version)