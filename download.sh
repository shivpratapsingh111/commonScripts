#!/bin/bash

remote=$1
local=$2

helpFun() {
echo "Usage: "
echo "arg1: remote file path (Server)"
echo "arg2: local path to save file (Client)"
echo "Example:- "
echo "./script.sh /root/data/file.txt /home/john/Desktop/"
}

if [ "$#" -eq 0 ]
then
  helpFun
  exit 1
fi

scp root@157.245.111.17:$remote $local 