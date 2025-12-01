# - Adicionar contato
#   - O contato possui o nome como chave.
#   - Se tentar adicionar outro contato com o mesmo nome, adicione os telefones ao contato existente.
#   - Adicionar os novos números de telefone no contato já existente.
# - Mostrar
#   - Mostrar os contatos da agenda pela ordem alfabética.
# - Remoção
#   - Remover contato pela chave.
#   - Remover telefone do contato.
# - Busca
#   - Fazer uma busca por padrão em todos os atributos do contato, nome e telefones.
#   - Se o contato tiver qualquer campo que combine com a string pattern de busca, ele deve ser retornado. Se o pattern é maria, devem ser retornados os contatos como "maria julia", "mariana", "ana maria", etc. Também inclua na busca o id do telefone ou o número do telefone.
# - Favoritos
#   - Favoritar e Desfavoritar um contato.
#   - Mostrar os favoritos.
# ***

class Fone: 
    def __init__(self, id: str, number: str):
        self.id = id 
        self.number = number 
        self.fone = dict[str, Contato] = {}
    
    def getId(self):
        return self.id
    
    def getNumber(self):
        return self.number
    
    def validate(self, validos: str) -> bool:
        validos = "0123456789"
        for c in validos:
            if c not in validos:
                return False
            return True 
    
    def __str__(self):
        fones = ", ".join([str(x)for x in enumerate(self.contacts)])
        return f"{self.id}:{self.number}"
    

class Contato:
    def __init__(self):
        self.favoritos: bool = False 
        self.fones: dict[str, Fone] = {}
        self.nome: str 

    def addFone(self, id: str, number: str):
        if not Fone.validate(number):
            raise Exception("fail: numero invalido")
        index = len(self.fones)
        self.fones[index] = Fone(id, number)


    def rmFone(self, index: int):
        if index < 0 or index >= len(self.fones):
            raise Exception(f"fail: indice invalido")
        
        del self.fones[index]
        self.fones = {i: f for i, f in enumerate(self.fones.values())}


    def toogleFavorited(self, favoritos: bool):
        self.favoritos = not self.favoritos

    def isFavorited(self) -> bool: 
        return self.favoritos
    
    def getFones(self):
        return list(self.fones.values())
    
    def getName(self):
        return self.nome
    
    def setName(self, name: str):
        self.nome = name 


    def __str__(self):
        prefix = "@" if self.favoritos else "-"
        lista_fones = ", ".join(f"{fone.id}:{fone.number}" for fone in self.fones.values())
        return f"{prefix} {self.nome} [{lista_fones}]"

        

class Agenda:
    def __init__(self):
        self.contacts: list[Contato] = []

    def findPosByName(self, name: str) -> int:
        for i, contato in enumerate (self.contacts):
            if contato.getName() == name:
                return i
            return -1
        

    def addContact(self, name: str, fones: list):
        indice = self.findPosByName(name)
        if indice != -1:
            contato = self.contacts[indice]
            for f in fones:
                if Fone.validate(f.number):
                    contato.addFone(f.id, f.number)
                else:
                    print(f"fail: fone {f.number} invalido")
            return

        novo = Contato(name)

        for f in fones:
            if Fone.validate(f.number):
                novo.addFone(f.id, f.number)
            else:
                print(f"fail: fone {f.number} invalido")

        self.contacts.append(novo)
        self.contacts.sort(key=lambda c: c.getName())
                

    def getContact(self, name: str) -> Contato | None:
        indice = self.findPosByName(name)
        if indice == -1:
            return None 
        return self.contacts[indice]
    
    def rmContact(self, name: str):
        indice = self.findPosByName(name)
        if indice == -1:
            raise Exception("fail: contato nao existe")
        del self.contacts[indice]

    def search(self, contatos: list):
        
        


def main():
    agenda = Agenda
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        try:
            if args[0] == "end":
                break

            elif args[0] == "add":
                Fone.add = args([1][2])


            else: 
                print("fail: comando invalido")
        except Exception as e:
            print(e)


main()