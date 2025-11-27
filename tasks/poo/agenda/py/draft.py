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
    
    def validar_numero(self, validos: str) -> bool:
        validos = "0123456789"
        for c in validos:
            if c not in validos:
                return False
            return True 
    
    def __str__(self):
        fones = ", ".join([str(x)for x in enumerate(self.contatos)])
        return f"{self.id}:{self.number}"
    

class Contato:
    def __init__(self):
        self.favoritos: bool = False 
        self.fones: dict[str, Fone] = {}
        self.nome: str 

    def addFone(self, id: str, number: str):
        if not Fone.validar_numero(number):
            raise Exception("fail: numero invalido")
        
        self.fones.append(Fone(id, number))

    def remover_fone(self, index: int):
        if self.index in self.fones:
            raise Exception (f"fail: indice {index} ja existe")
        del 
        
        try:
            del self.pessoas[id]
        except KeyError as _:
            raise Exception(f"fail: Id {id} não existe")


        

class Agenda:
    def __init__(self, id: str):
        self.id = id 

    def get_id(self):
        return self.id 
    
    def add_contato(self, id: str):
        if self.id 