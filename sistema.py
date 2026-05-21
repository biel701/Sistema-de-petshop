class Cachorro:
    def __init__(self, nome, comida, sono):
        self.nome= nome
        self.comida= comida
        self.sono= sono
    def __str__(self):
        return f"Nome: {self.nome}, Comida: {self.comida}, Sono: {self.sono}"
    def comer(self):
        if self.comida > 0:
            self.comida=self.comida - 1
            return self.comida
    def dormir(self):
        if self.sono == True:
            return "dormindo"
def inicializar():
    lista_espera = [
        Cachorro("robin", 3, False),
        Cachorro("cleber", 2, True),
        Cachorro("bart", 0, True),
        Cachorro("milena", 5, False),
        Cachorro("belinha", 0, True)
    ]
    tem_sono=[]
    tem_comida=[]
    def organizar():
        for cao in lista_espera:
            if cao.sono:
                tem_sono.append(cao)
            elif cao.comida > 0:
                tem_comida.append(cao)
    organizar()
    for cao in lista_espera:
        print(cao)
    for cao in tem_sono:
        print(f"Esse tem que dormir: {cao.nome}")
    for cao in tem_comida:
        print(f"Esse tem comida: {cao.comida}")
print("Bem-vindo, deseja inicializar o sistema?")
print("Digite 1 se sim e 0 se não")
resposta=int(input())
if resposta == 1:
    inicializar()
else:
    print("beleza, falou")
