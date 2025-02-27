from goleiro import Goleiro
from atacante import Atacante
from fixo import Fixo
from alas import AlaEsquerdo, AlaDireito

# Classe para representar um Time de Futsal
class TimeFutsal:
    def __init__(self, nome):
        self._nome = nome  # Nome do time
        self._jogadores = []  # Lista de jogadores

    # Metodo para adicionar um jogador ao time
    def adicionar_jogador(self, jogador):
        self._jogadores.append(jogador)
        print(f"{jogador.get_nome()} foi adicionado ao time {self._nome}.")

    # Metodo para listar todos os jogadores do time
    def listar_jogadores(self):
        print(f"Jogadores do time {self._nome}:")
        for jogador in self._jogadores:
            print(jogador)

    # Metodo para simular uma partida (todos os jogadores jogam)
    def jogar_partida(self):
        print(f"O time {self._nome} está em campo!")
        for jogador in self._jogadores:
            print(jogador.jogar())  # Polimorfismo: cada jogador executa sua própria implementação de jogar()

    # Metodo para mostrar o desempenho geral do time
    def desempenho_geral(self):
        print(f"Desempenho do time {self._nome} no ultimo jogo:")
        for jogador in self._jogadores:
            if isinstance(jogador, Goleiro):
                print(f"{jogador.get_nome()}: {jogador.fazer_defesa()}")
            elif isinstance(jogador, Atacante):
                print(f"{jogador.get_nome()}: {jogador.marcar_gol()}")
            elif isinstance(jogador, Fixo):
                print(f"{jogador.get_nome()}: {jogador.interceptar_bola()}")
            elif isinstance(jogador, AlaEsquerdo):
                print(f"{jogador.get_nome()}: {jogador.fazer_cruzamento()}")
            elif isinstance(jogador, AlaDireito):
                print(f"{jogador.get_nome()}: {jogador.dar_assistencia()}")
