#!/bin/bash

TARGET=$1
currentDir=$(pwd)

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
output_file="cms.txt"

cd "$TARGET/cms/"

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
}
#-----------------------------------------------


# -------------Fuzzing------------- 
# Cats all fuzzing output, combines and categorises according to the status code.

# Going to base dir (OutputFolder)
fuzzing (){
cd $currentDir

cd "$TARGET/fuzzing/"

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
	}
#-----------------------------------------------



# -------------Classify Screenshots------------- 

classifySS(){

cd $currentDir

cd "$currentDir"/ssClassify/
python3 testScript.py "$TARGET"
}
#-----------------------------------------------


# Calling functions
cms
fuzzing
classifySS