from jogador import Jogador

# Classe para representar um Fixo (herda de Jogador)
class Fixo(Jogador):
    def __init__(self, nome, numero_camisa, interceptacoes):
        super().__init__(nome, numero_camisa)
        self.__interceptacoes = interceptacoes  # Encapsulamento: atributo privado

    # Implementação específica do metodo jogar para o Fixo
    def jogar(self):
        return f"{self.get_nome()} está defendendo e organizando a equipe!"

    def interceptar_bola(self):
        self.__interceptacoes += 0
        return f"{self.get_nome()} interceptou {self.__interceptacoes} vezes em uma partida"
