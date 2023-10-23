
class pessoa:
    def __init__(self,nome,idade,cidade):
        self.__nome= nome
        self.__idade= idade
        #self.__peso= peso
        self.__cidade= cidade
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade

    @property
    def cidade(self):
        return self.__cidade 
        
    @idade.setter
    def idade(self,idade):
        self.__idade= idade
    
    
contador= int(input("quantas pessoas iram responder ao formulario?"))
x=0
while(x<contador):
    nome=(input("digite seu nome:"))
    idade=int(input("digite sua idade:")) 
    cidade=input("digite sua cidade:")
    x+=1
cidadao=pessoa(nome,idade,cidade)
print(cidadao.idade)
print(cidadao.nome)
print(cidadao.cidade)

cidadao.idade= 17
print(cidadao.idade)
