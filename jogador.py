class Jogador:
    def __init__(self, nome, numero_camisa):
        self._nome = nome  # Encapsulamento: atributo protegido
        self._numero_camisa = numero_camisa

    def get_nome(self):
        return self._nome

    def get_numero_camisa(self):
        return self._numero_camisa

# Metodo abstrato (simulado com uma exceção)
    def jogar(self):
        raise NotImplementedError("Subclasses devem implementar o método 'jogar'")

# Metodo para exibir informações do jogador
    def __str__(self):
        return f"{self._nome} (Camisa {self._numero_camisa})"

