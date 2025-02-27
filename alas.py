from jogador import Jogador

class AlaEsquerdo(Jogador):
    def __init__(self, nome, numero_camisa, cruzamentos):
        super().__init__(nome, numero_camisa)
        self.__cruzamentos = cruzamentos  # Encapsulamento: atributo privado

    # Implementação específica do metodo jogar para o Ala Esquerdo
    def jogar(self):
        return f"{self.get_nome()} está correndo pela lateral esquerda e apoiando o ataque!"

    def fazer_cruzamento(self):
        self.__cruzamentos += 0
        return f"{self.get_nome()} fez {self.__cruzamentos} cruzamentos em uma partida"

class AlaDireito(Jogador):
    def __init__(self, nome, numero_camisa, assistencias):
        super().__init__(nome, numero_camisa)
        self.__assistencias = assistencias  # Encapsulamento: atributo privado

    # Implementação específica do metodo jogar para o Ala Direito
    def jogar(self):
        return f"{self.get_nome()} está correndo pela lateral direita e criando jogadas!"

    def dar_assistencia(self):
        self.__assistencias += 0
        return f"{self.get_nome()} fez {self.__assistencias} assistências em uma partida"
