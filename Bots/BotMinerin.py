from Bots.Bot import Bot

class BotMinerin(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.__comandos = {"1":"Você queria ter praia?",
                           "2":"Pão de Queijo ou Queijo Canastra?",
                           "3":"O que significa a sigla GO?",
                           "4":"Onde você mora?",
                           "5":"Qual o verdadeiro truco?",
                           "6":"Você é atleticano ou cruzeirense?"}

    @property
    def comandos(self):
        return self.__comandos

    def apresentacao(self):
        return f"Aoba, bão ô não?! Prazer, sou o {self.nome}. E ocê, cê é fí de quem?"

    def executa_comando(self, cmd):
        if cmd == "1":
            return f'{self.nome} diz: Sô, não é Minas que não tem mar, é o mar que não têm Minas!'
        elif cmd == "2":
            return f'{self.nome} diz: Pão de Queijo com Queijo Canastra'
        elif cmd == "3":
            return f' {self.nome} diz: GOnorante! Mas nós aqui de Minas somo Mai Gonorante ainda!'
        elif cmd == "4":
            return f' {self.nome} diz: Eu moro logo ali, na rua de cima do açouque do Valtin, debaixo da rua da Vânia mãe do Zé'
        elif cmd == "5":
            return f'{self.nome} diz: O truco de verdade é o trucão com manilha fixa! Esses paulistas que inventam esse trem de manilha alta'
        elif cmd == "6":
            return f'{self.nome} diz: GALOOOOOO!'
        else:
            return 'Comando não encontrado'

    def boas_vindas(self):
        return f' {self.nome} diz: Prazer, {self.nome} Eu tenho um primo em Uberlândia com esse mesmo nome.'

    def despedida(self):
        return f' {self.nome} diz: Vai não sô, tá cedo!! Fica só mais um cadin, vou passar um cafezin nesse instante.'

