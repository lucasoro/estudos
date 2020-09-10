 # Questão 22

## Atributos:

Decidiu-se criar uma única classe para representar todos os produtos, denominada Bebida, com os seguintes atributos: tipo (correspondente ao tipo de bebida, podendo ser vinho ou cerveja), marca (correspondente à marca do vinho ou da cerveja), preço(correspondente ao preço da garrafa do vinho ou da lata da cerveja), estoque (correspondente ao número de garrafas do vinho ou de latas da cerveja disponível na loja), ano (correspondente ao ano de fabricação,se for vinho), país (correspondente ao país de origem, se for vinho), cor (tinto ou branco, se for vinho)e uva (correspondente ao tipo de uva, se for vinho).

## Métodos:

### Getters e setters!
No caso do vinho, a loja tinha interesse em saber a marca, o ano de fabricação, o país de origem, a cor (tinto ou branco), o tipo de uva, o preço da garrafa e onúmero de garrafas disponível na loja.
No caso da cerveja, a loja tinha interesse em saber a sua marca, o preço da lata e o número de latas disponível na loja.

### Métodos específicos:
•construtor, com os parâmetros necessários para definir o valor inicial de todos os atributos do objeto.
•vender, com um parâmetro do tipo int que indica a quantidade de unidades vendidas (a execução desse método altera o atributo estoque).
•comprar, com um parâmetro do tipo int que indica a quantidade de unidades compradas(a execução desse método altera o atributo estoque).
•atualizarPreco, com um parâmetro do tipo double que indica o novo preço do item. Deve ser criada uma classe Teste contendo o método main que instancia um objeto de cada classe e chama todos os seus métodos uma vez, ao menos.