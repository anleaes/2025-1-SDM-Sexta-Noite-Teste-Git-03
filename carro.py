class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_infos(self):
        print(f'carro: {self.marca} {self.modelo} {self.ano} {self.cor} ')

carro1 = Carro("Chevrolet", "Camaro", 99, "Azul")

carro1.exibir_infos()