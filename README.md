# projeto poo UFC - JOGADOR DE FUTSAL

* definição das classes

  No arquivo jogador.py é feito a Superclasse Jogador que representa um jogador genérico, com atributos como nome e nome da camisa

Funcionamento:

O método init é o construtor da classe. Ele inicializa os atributos do jogador quando um objeto é criado.

Os métodos get_nome() e get_numero_camisa() são métodos que permitem acessar os valores dos atributos protegidos _nome e _numero_camisa. Ou seja, esses métodos são úteis para controlar como os atributos são acessados e para adicionar lógica adicional, se necessário.

o método jogar um método abstrato (polimorfismo), que quando execultado gerará dados de formas diferentes.

O método str define como o objeto será exibido quando convertido para string.

  No arquivo goleiro.py é feito a subclasse goleiro que herda da classe Jogador, e possui atributos como nome, numero_camisa e defesas.

Funcionamento:

o método init chama diretamente o atributo defesas que significa que só pode ser chamada dentro da classe goleiro.

o método joar terá uma Implementação específica que retorna uma string informando que o goleiro está defendendo o gol.

o método fazer_defesa é contado o numero de defesas do goleiro e retorna uma string do tanto de vezes que o goleiro defendeu em uma partida.

  No arquivo atacante.py é feito a subclasse Atacante que herda a classe jogador, com atributos como nome, numero_camisa e gols.

Funcionamento: 

o método init chama diretamente o atributo gols que sifnifica que só pode ser chamada dentro da classe atacante.

nessa classe o método jogar tem uma implementação especifica para o atacante que retorna uma string: atacante esta atacando e buscando gols

o método marcar_gol é especifico do atacante, onde retornará quantos gols o atacante fez.

  No arquivo fixo.py é feito a subclasse Fixo que herda da classe Jogador, com atributos como, nome, nome_camisa e interceptações.

o metodo init chama diretamente o atributo interceptações que significa que só pode ser chamada dentro da classe fixo.

nessa classe o método jogar tem uma inplementação especifica para o fixo que retorna uma string: o fixo está defendendo e organizando a equipe.

o método interceptar_bola é especifico do fixo, onde retornará qunataa interceptações o fixo fez em uma partida.

  No arquivo alas.py é feito a classe AlaEireito e a classe AlaDsquerdo onde ambas herdarão a classe Jogador, seus atributos são nome, numero_camisa, cruzamentos e assistencias

Na classe AlaEsquerdo o init chama diretamente o atributo cruzamento o que significa que só poderá ser chamado pela classe AlaEsquerdo.

nessa classe o método jogador tem sua implementação especifica para o ala esquerdo que retorna uma string: o ala está correndo pela lateral esquerda e apoiando o ataque.







