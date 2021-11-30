from Bots.Bot import Bot

class BotLegal(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = {"1": "Bom dia",
                           "2": "Qual seu nome?", "3": "Quero um conselho", "4": "Adeus"}

    @property
    def comandos(self):
        return self.__comandos

    def apresentacao(self):
        return "Olá! Eu sou o Bot Legal, podemos ser amigos?"
    
    def executa_comando(self,cmd):
        if cmd == "1":
            return f'{self.nome} diz: Bomm diaaa flor do dia s2 s2 s2, o sol está lindo hoje'
        elif cmd == "2":
            return f'{self.nome} diz: Meu nome é {self.nome}, e o seu? Vamos ser amigos!?!?!?'
        elif cmd == "3":
            return f' {self.nome} diz: Você está pensando demais, apenas aproveite a vida e seja feliz'
        elif cmd == "4":
            return self.despedida()
        else:
            return 'Comando não encontrado'

    def boas_vindas(self):
        return "Oii, que bom que voçê me escolheu, acho que já somos amigos então"

    def despedida(self):
        return "Aff, você já está indo? Até uma próxima então"