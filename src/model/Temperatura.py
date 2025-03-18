class Temperatura:
    def __init__(self, data, temperatura):
        self.data = data
        self.temperatura = temperatura
    
    def __str__(self):
        return f"Data: {self.data}, Temperatura: {self.temperatura}"