from _typeshed import Self


class Carro:
    cor = "azul"
    cpdtqn = 5
    qtdgas = 10
    medialtkm = 8
    def __init__(self,cor,cpdtqn,qtdgas,medialtkm):
        self.cor = cor
        self.cpdtqn = cpdtqn
        self.medialtkm = medialtkm
        self.qtdgas = qtdgas
    def mediakm(qtdgas,medialtkm):
        Self._mediakm = (qtdgas/medialtkm)
        print (medialtkm)
    mediakm(qtdgas,medialtkm)