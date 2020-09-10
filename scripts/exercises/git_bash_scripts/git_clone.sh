#!/bin/bash

# Local variables
local_dir=$(pwd)
my_var="${2}"
my_var="${my_var##*/}"
my_var="${my_var%.*}"
repo_name="$(echo ${my_var})"
target_dir='/home/oro/Documents/Samples/malware/'

# Check if directory exists; if not, create it
if [ -d "${target_dir}""${1}" ] ; then
	echo " "
else
	mkdir "${target_dir}""${1}"
fi

# Execution
cd "${target_dir}""${1}"
git clone -q "${2}"

# Verification of exit status
if test $? -eq 0; then
	echo 'Clonado com sucesso!'
else
	echo 'Erro na execução do comando git clone!'
fi

# Removing .git folder from cloned repo
cd "${target_dir}""${1}"/"${repo_name}"
rm -rf ".git/"
