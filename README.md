# projeto poo UFC - JOGADOR DE FUTSAL

* definição das classes e seus métodos(definição) 

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

o método marcar_gol é especifico do atacante, que retornará quantos gols o atacante fez.

  No arquivo fixo.py é feito a subclasse Fixo que herda da classe Jogador, com atributos como, nome, nome_camisa e interceptações.

o metodo init chama diretamente o atributo interceptações que significa que só pode ser chamada dentro da classe fixo.

nessa classe o método jogar tem uma inplementação especifica para o fixo que retorna uma string: o fixo está defendendo e organizando a equipe.

o método interceptar_bola é especifico do fixo, que retornará qunatas interceptações o fixo fez em uma partida.

  No arquivo alas.py é feito a classe AlaEireito e a classe AlaDsquerdo onde ambas herdarão a classe Jogador, seus atributos são nome, numero_camisa, cruzamentos e assistencias

Na classe AlaEsquerdo o método init chama diretamente o atributo cruzamento o que significa que só poderá ser chamado pela classe AlaEsquerdo.

nessa classe o método jogador tem sua implementação especifica para o ala esquerdo que retorna uma string: o ala está correndo pela lateral esquerda e apoiando o ataque.

o método fazer_cruzamentos é específico do ala esquerdo, que retornará quantos cruzamentos o ala fez.

Ja na classe AlaDireito o método init chama diretamente o atributo assistencias, que significa que esse atributo só poderá ser chamada da classe AlaDireito.

nesssa classe o método jogar tem sua implementação especifica para ala direito que retorna a string: ala direito está correndo pela lateral direita e criando jogadas.

o método dar_assistencia é especifico do ala direito, que retornará quantas assistencias o ala fez na partda.

  No arquivo time_futebol.py é feito a classe TimeFutebol que será importado as classes Goleiro, Atacante, Fixo, AlaDireito e AlaEsquerdo.

nessa classe o método init terá o atributo nome do time e tambem uma lista de jogadores.

o método adicionar_jogador tem como sua função adicionar jogadores ao time.

o método listar jogadores tem como sua função listar os jogadores do time.

o método jogar_partida tem como sua função simular uma partida onde o polimorfismo entrará em ação por que cada jogador executa sua própria implementação de jogar().

o método desempenho_geral tem como sua função mostrar o desenpenho geral do time em sua ultima partida, esse método é composto por um laço for jogador in self._jogadores e dentro desse laço, haverá um if insistance que imprimirá os daods do joagador em um jogo.

* construção dos objetos






