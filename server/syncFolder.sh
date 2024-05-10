#!/bin/bash

# Change your server ip and password
SERVER="127.0.0.1"
PASSOWRD="your_root_password"
SOURCE_FOLDER="/root/OutputFolder"
DESTINATION_FOLDER="/home/cyrusop/bugBounty/serber"

echo $PASSOWRD | rsync -avz --progress root@$SERVER:$SOURCE_FOLDER $DESTINATION_FOLDER





