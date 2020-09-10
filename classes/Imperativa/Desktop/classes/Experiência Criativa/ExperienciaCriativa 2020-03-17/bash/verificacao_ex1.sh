#!/bin/bash

# Escreve no banco
adiciona_verificacao(){

	# Limpa a tela
	clear

	# Leitura de input
	read -p "Insira o novo usuário: " user_novo
	read -p "Insira a nova senha: " user_senha_novo
	
	# Codifica em hash sha1 a senha inserida
	echo $user_senha_novo > dummy
	user_senha_hash=$(openssl sha1 dummy)
	rm dummy
	user_senha_hash=${user_senha_hash##*=}

	# Escreve no arquivo as credenciais fornecidas
	echo "$user_novo :$user_senha_hash" >> credenciais.txt

	# Diz ao usuário se a escrita foi bem sucedida
	if [ $? -eq 0 ]; then
		echo "Usuário escrito no 'banco de dados!'"
	else
		echo "Ocorreu um erro!"
	fi
}

# Verifica se o usuário inserido existe no arquivo credenciais.txt
verifica() {

	# Leitura de input
	read -p "Insira o usuário: " user
	read -p "Insira a senha: " pass

	# Codificação do input fornecido
	echo $pass > dummy
	local_pass=$(openssl sha1 dummy)
	local_pass=${local_pass##*=}
	rm dummy
	local_creds="${user} :${local_pass}"
	
	# Identifica se o usuário fornecido foi encontrado no banco de dados
	grep "${local_creds}" credenciais.txt > /dev/null

	# Retorna ao usuário se o acesso foi concedido ou não
	case $? in
		0) echo "Acesso garantido!";;
		1) echo "Acesso negado!";;
		*) echo "Erro!";;
	esac
}

# Menu principal
clear
echo "Opção 1: inserir novo usuário"
echo "Opção 2: verificar existência de usuário"
read -p "Escolha a opção: " menu_input

case ${menu_input} in
	1 ) adiciona_verificacao;;
	2 ) verifica;;
	* ) echo "Opção inválida"; exit;;
esac
