from jogador import Jogador

# Classe para representar um Atacante (herda de Jogador)
class Atacante(Jogador):
    def __init__(self, nome, numero_camisa, gols):
        super().__init__(nome, numero_camisa)
        self.__gols = gols  # Encapsulamento: atributo privado

    # Implementação específica do método jogar para o Atacante
    def jogar(self):
        return f"{self.get_nome()} está atacando e buscando gols!"

    def marcar_gol(self):
        self.__gols += 0
        return f"{self.get_nome()} fez {self.__gols} gols em uma partida"
