class persona:
    def __init__(self):
        self.nome = None
        self.conome = None
        self.eta = None
        self.sesso = None

    def salva_nome(self, v):
        self.nome = v

    def salva_cognome(self, v):
        self.cognome = v

    def salva_eta(self, v):
        self.eta = v

    def salva_sesso(self, name, num):
        self.sesso = name
