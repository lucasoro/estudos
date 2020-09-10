#!/bin/bash

# Organização de diretórios
mkdir -p alice
mkdir -p bob 

# Criação da chave privada - Alice
openssl genrsa -out alice/alice_key.pem 1024

# Criação da chave pública - Alice
openssl rsa -in alice/alice_key.pem -pubout -out alice/alice_pubkey.pem

# Texto a ser encriptado
echo "Mensagem a ser encriptada:" && echo "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
echo "Lorem ipsum dolor sit amet, consectetur adipiscing elit." > bob/teste.txt

# Comando que encripta o texto
echo "" && openssl rsautl -in bob/teste.txt -out bob/teste.rsa -encrypt -pubin -inkey alice/alice_pubkey.pem && echo "Texto encriptado: " && cat bob/teste.rsa && echo ""

# Alice desencripta a mensagem com sua chave privada
echo "" && openssl rsautl -in bob/teste.rsa -decrypt -inkey alice/alice_key.pem -out alice/texto_traduzido.txt && echo "Texto desencriptado:" && cat alice/texto_traduzido.txt && echo ""

# Tentativas de um terceiro de decriptar a mensagem interceptada:
mkdir -p bad && cp bob/teste.rsa bad/teste_roubado.rsa

# Tentativa com a chave pública
echo "Resultado da primeira tentantiva, usando a chave pública: "
openssl rsautl -in bad/teste_roubado.rsa -decrypt -pubin -inkey alice/alice_pubkey.pem && echo ""

# Tentativa com uma própria chave
echo "Resultado da segunda tentativa, utilizando uma chave gerada pelo badBoy: "

# Geração da chave do badBoy
openssl genrsa -out bad/badboy_key.pem 1024

# Aplicação de sua própria chave privada em cima da mensagem criptografada
openssl rsautl -in bad/teste_roubado.rsa -decrypt -inkey bad/badboy_key.pem 

echo "" && echo "O erro encontrado indica uma falha na tentativa de checagem de padding, detectado pelo algoritmo de desencriptação; comumente, isto indica a utilização de uma chave privada não utilizada para a encriptação do texto."

# -----------------------------------------------------------------
# Segunda parte:
# Bob criptografa uma chave secreta para enviar para Alice
echo "1234" > bob/chavesecreta
openssl des-ecb -in bob/teste.txt -out alice/teste.des -kfile bob/chavesecreta
openssl rsautl -in bob/chavesecreta -out alice/chavesecreta.rsa -encrypt -pubin -inkey alice/alice_pubkey.pem

# Alice descriptografa a chave secreta para utilizá-la, por sua vez, como chave na descriptografia da mensagem teste.des
echo "" && echo "Mensagem encriptada com a chave secreta: "
cat alice/teste.des
echo "" && echo ""
echo "Mensagem descriptografada com a chave recebida: "
openssl rsautl -in alice/chavesecreta.rsa -decrypt -inkey alice/alice_key.pem -out alice/chavesecreta_descriptografada
openssl des-ecb -d -in alice/teste.des -kfile alice/chavesecreta_descriptografada
