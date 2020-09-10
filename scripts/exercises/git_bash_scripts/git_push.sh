#!/bin/bash

# Change directory to father folder
cd ~/Documents/Samples

# Commit changes currently staged
git add .
git commit -m "${1}"

# Push changes
git push origin master
