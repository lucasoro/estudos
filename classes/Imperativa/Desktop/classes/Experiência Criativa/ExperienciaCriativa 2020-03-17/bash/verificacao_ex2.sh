#!/bin/bash

# Verifica se o usuário existe no 'banco'
verifica() {
	clear
	read -p "Digite seu usuário: " local user
	
	# Chamada da função que verifica a senha, passando o usuário como parâmetro
	verificacao_user $user
}

# Adiciona credenciais ao 'banco'
adiciona_verificacao(){

		# Limpa a tela
        clear

		# Leitura de input
        read -p "Insira o novo usuário: " user_novo
        read -p "Insira a nova senha: " user_senha_novo
        
		# Codificação em sha1 da senha
		echo $user_senha_novo > dummy
        user_senha_hash=$(openssl sha1 dummy)
        rm dummy
        user_senha_hash=${user_senha_hash##*=}
        
		# Escreve no 'banco' as credenciais passadas pelo usuário
		echo "$user_novo :$user_senha_hash" >> credenciais.txt
        
		# Retorna ao usuário se a escrita foi bem-sucedida
		if [ $? -eq 0 ]; then
                echo "Usuário escrito no 'banco de dados!'"
        else
                echo "Ocorreu um erro!"
        fi
}

# Verifica a existência de um usuário no 'banco'
# Quando essa função é chamada, é passado como parâmetro o usuário,
# por isso, lê-se dentro do escopo desta função apenas a senha
verificacao_pass() {

	# Captura da senha
	read -p "Insira sua senha: " pass

	# Codificação da senha
	echo $pass > dummy
	local_hash=$(openssl sha1 dummy)
	rm dummy
	local_hash=${local_hash##*=}

	# Concatenação dos dados
	local_creds=$(echo "${2} :${local_hash}")

	# Verificação dos dados dentro do 'banco de dados'
	grep "${local_creds}" credenciais.txt > /dev/null
	if [ $? -eq 0 ]; then
		echo "Sucesso!"
	else
		echo "Senha incorreta, tente novamente."
		case $1 in
			5) verificacao_pass 4 $2;;
			4) verificacao_pass 3 $2;;
			3) verificacao_pass 2 $2;;
			2) verificacao_pass 1 $2;;
			1)echo "Tentativas demais, tente novamente mais tarde! "; exit;;
		esac
	fi
}

# Verifica a existência de um usuário no banco
verificacao_user() {
	grep "$1" credenciais.txt > /dev/null
	if [ $? -eq 0 ]; then
		verificacao_pass 5 $1
	else
		echo "Usuário não cadastrado!"
	fi
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
