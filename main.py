from goleiro import Goleiro
from atacante import Atacante
from fixo import Fixo
from alas import AlaEsquerdo, AlaDireito
from time_futsal import TimeFutsal

meu_time = TimeFutsal("Corinthians")

# Criando os jogadores
goleiro = Goleiro("Hugo Solza", 1, 12)
atacante = Atacante("Menphis Depay", 10, 7)
fixo = Fixo("André Ramalho", 5, 6)
ala_esquerdo = AlaEsquerdo("André Carrilho", 19, 3)
ala_direito = AlaDireito("Rodrigo Garro", 8, 5)

meu_time.adicionar_jogador(goleiro)
meu_time.adicionar_jogador(atacante)
meu_time.adicionar_jogador(fixo)
meu_time.adicionar_jogador(ala_esquerdo)
meu_time.adicionar_jogador(ala_direito)
print("\n")

meu_time.listar_jogadores()
print("\n")

# Simulando uma partida (polimorfismo em ação)
meu_time.jogar_partida()
print("\n")

meu_time.desempenho_geral()