class Moto:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_infos(self):
        print(f'carro: {self.marca} {self.modelo} {self.ano} {self.cor} ')

moto1 = moto("Honda", "CG 160 Super", 2020, "Preta")

moto1.exibir_infos()