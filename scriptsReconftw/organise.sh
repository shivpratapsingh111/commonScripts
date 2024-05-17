#!/bin/bash

# `dirname $0` gives the path of the organise.sh file, which helps to identify the main folder having all necessary files to execute the script.

# But if you execute `dirname $0` form folder conataing this script, it will return `.` as the directory name.
# to get the pure path instead of `.` we used `readlink`
currentDir="$(dirname "$(readlink -f "$0")")"


TARGET=$1

if [ "$#" -eq 0 ]
then 
	echo "Provide the target direcotry path"
	echo "Usage: "
	echo "./script.sh OutputFolder/google.com"
	exit 1
fi

echo "[-] Organising $TARGET"



#-------------CMS-------------
# Cats all cms.json file in every subdomain's dir and combines in into a single file.

# Going to base dir (OutputFolder)
cms(){

cd $currentDir
folder=$1

output_file="cms.txt"


if [ -d "$TARGET/$folder/cms/" ]; then

	cd "$TARGET/$folder/cms/"

	if [ -d "all" ]; then
		echo "[x] 'cms' is already organised"
		return

	else
		mkdir all

		for dir in */; do
			dir_name=$(basename "$dir")
			if [ -d "$dir" ]; then
				if [ "$dir_name" != "all" ]; then

		    		echo "====================$dir_name====================" >> "$output_file"
		    		echo "" >> "$output_file"

		    		cat "${dir}cms.json" >> "$output_file"

		    		echo "" >> "$output_file"
		    		echo "" >> "$output_file"

					mv "$dir_name" all

				fi
			fi

		done

		echo "[x] 'cms' done"

	fi

else
	echo "[+] No 'cms' folder found, Skipping.."
	return

fi
}
#-----------------------------------------------


# -------------Fuzzing------------- 
# Cats all fuzzing output, combines and categorises according to the status code.

# Going to base dir (OutputFolder)
fuzzing (){
cd $currentDir
folder=$1

if [ -d "$TARGET/$folder/fuzzing/" ]; then

	cd "$TARGET/$folder/fuzzing/"

	if [ -d "all" ]; then
		echo "[x] 'fuzzing' is already organised"
		return

	else

		for file in *; do
			if [ -f "$file" ]; then
			cat $file | grep -P '^2\d{2}' >> 200
			cat $file | grep -P '^3\d{2}' >> 302
			cat $file | grep -P '^4\d{2}' >> 403
			cat $file | grep -P '^5\d{2}' >> 500
			fi
		done
		mkdir all
		mv *.txt all/

		echo "[x] 'fuzzing' done"
	fi

else
	echo "[+] No 'fuzzing' folder found, Skipping.."
	# ls "$TARGET/$folder/fuzzing/"
fi
}
#-----------------------------------------------



# -------------Classify Screenshots------------- 

classifySS(){
cd $currentDir
folder=$1
if [ -d "$TARGET/$folder/screenshots/" ]; then

	# cd "$currentDir"/ssClassify/
	
	python3 "ssClassify/testScript.py" "$TARGET/$folder"

else 
	echo "[+] No 'screenshots' folder found, Skipping.."

fi
}
#-----------------------------------------------


# Calling functions

for dir in "$TARGET"/*; do

	dir=$(basename "$dir")

	cms $dir 
	fuzzing $dir 
	classifySS $dir
	echo $dir
done
