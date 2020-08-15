class Pizza:
    pedacos = 8
    
    def __init__(self, sabor):
        self.sabor = sabor

    def pegar_pedaco(self):
        self.pedacos -= 1
    
    @classmethod
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos