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

changeDir(){
    echo "Current Arg: $TARGET"
    echo "Current Dir: $currentDir"
}

changeDir