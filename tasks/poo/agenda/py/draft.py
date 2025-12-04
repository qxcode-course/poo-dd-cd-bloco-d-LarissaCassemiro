class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    @staticmethod
    def isValid(number: str) -> bool:
        validos = "0123456789"
        return all(c in validos for c in number)

    def getId(self):
        return self.id

    def getNumber(self):
        return self.number

    def toString(self):
        return f"{self.id}:{self.number}"

    def __str__(self):
        return self.toString()


class Contact:
    def __init__(self, name: str):
        self.name = name
        self.favorited = False
        self.fones: list[Fone] = []

    def addFone(self, id: str, number: str):
        if Fone.isValid(number):
            self.fones.append(Fone(id, number))
        else:
            print(f"fail: fone {number} invalido")

    def rmFone(self, index: int):
        if 0 <= index < len(self.fones):
            self.fones.pop(index)
        else:
            print("fail: indice invalido")

    def toogleFavorited(self):
        self.favorited = not self.favorited

    def isFavorited(self):
        return self.favorited

    def getFones(self):
        return self.fones

    def getName(self):
        return self.name

    def setName(self, name: str):
        self.name = name

    def toString(self):
        prefix = "@" if self.favorited else "-"
        lista = ", ".join(str(f) for f in self.fones)
        return f"{prefix} {self.name} [{lista}]"

    def __str__(self):
        return self.toString()


class Agenda:
    def __init__(self):
        self.contacts: list[Contact] = []

    def findPosByName(self, name: str) -> int:
        for i, c in enumerate(self.contacts):
            if c.getName() == name:
                return i
        return -1

    def addContact(self, name: str, fones: list[Fone]):
        pos = self.findPosByName(name)

        if pos != -1:
            contato = self.contacts[pos]
            for f in fones:
                contato.addFone(f.id, f.number)
            return
        novo = Contact(name)
        for f in fones:
            novo.addFone(f.id, f.number)

        self.contacts.append(novo)
        self.contacts.sort(key=lambda c: c.getName())

    def getContact(self, name: str):
        pos = self.findPosByName(name)
        return self.contacts[pos] if pos != -1 else None

    def rmContact(self, name: str):
        pos = self.findPosByName(name)
        if pos == -1:
            print("fail: contato nao existe")
        else:
            self.contacts.pop(pos)

    def search(self, pattern: str):
        result = []
        for c in self.contacts:
            texto = c.toString()
            if pattern in texto:
                result.append(c)
        return result

    def getFavorited(self):
        return [c for c in self.contacts if c.isFavorited()]

    def getContacts(self):
        return self.contacts

    def toString(self):
        return "\n".join(c.toString() for c in self.contacts)


def main():
    agenda = Agenda()
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "add":
            name = args[1]
            fones = []
            for token in args[2:]:
                id_, num = token.split(":")
                fones.append(Fone(id_, num))
            agenda.addContact(name, fones)

        elif args[0] == "show":
            for c in agenda.getContacts():
                print(c.toString())

        elif args[0] == "rmFone":
            name = args[1]
            index = int(args[2])
            c = agenda.getContact(name)
            if c:
                c.rmFone(index)
            else:
                print("fail: contato nao existe")

        elif args[0] == "rm":
            agenda.rmContact(args[1])

        elif args[0] == "search":
            pattern = args[1]
            for c in agenda.search(pattern):
                print(c.toString())

        elif args[0] == "tfav":
            c = agenda.getContact(args[1])
            if c:
                c.toogleFavorited()
            else:
                print("fail: contato nao existe")

        elif args[0] == "favs":
            for c in agenda.getFavorited():
                print(c.toString())

        else:
            print("fail: comando invalido")


main()
