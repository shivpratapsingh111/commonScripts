#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <filename>"
    echo "File will be uploaded to '/root/username/'"
    exit 1
fi

SERVER=$(grep "Host bugbounty" ~/.ssh/config | awk '{print $2}')

FILE_TO_UPLOAD=$1
DESTINATION_PATH="/root/username/$FILE_TO_UPLOAD"

scp "$FILE_TO_UPLOAD" "$SERVER:$DESTINATION_PATH"

echo "File '$FILE_TO_UPLOAD' has been uploaded to $SERVER:$DESTINATION_PATH"
