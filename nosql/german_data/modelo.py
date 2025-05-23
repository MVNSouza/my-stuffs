class Cliente:
    def __init__(self,
                 idade: int = 0,
                 sexo: str = "",
                 credito: int = 0,
                 moradia: str = "",
                 conta_poupanca: str = "",
                 conta_corrente: str = "",
                 valor_conjunto: int = 0,
                 duracao: int = 0,
                 proposito: str = "",
                 aprovacao: int = -1):
        
        self.id = None  # ID será gerado pelo ClienteDAO, não no construtor
        self.idade = idade
        self.sexo = sexo
        self.credito = credito
        self.moradia = moradia
        self.conta_poupanca = conta_poupanca
        self.conta_corrente = conta_corrente
        self.valor_conjunto = valor_conjunto
        self.duracao = duracao
        self.proposito = proposito
        self.aprovacao = aprovacao
