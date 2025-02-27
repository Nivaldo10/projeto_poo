from jogador import Jogador

class Goleiro(Jogador):
    def __init__(self, nome, numero_camisa, defesas):
        super().__init__(nome, numero_camisa)
        self.__defesas = defesas  # Encapsulamento: atributo privado

    # Implementação específica do metodo jogar para o Goleiro
    def jogar(self):
        return f"{self.get_nome()} está defendendo o gol!"

    def fazer_defesa(self):
        self.__defesas += 0
        return f"{self.get_nome()} defendeu o gol {self.__defesas} vezes em uma partida"

