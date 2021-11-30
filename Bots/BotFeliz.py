from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        comandos = {"1": "Olá, tudo bem ? ",
                           "2": "Como você está ?", "3": "Quero um conselho", "4": "Adeus"}
        super().__init__(nome, comandos)

    def apresentacao(self):
        return f"Oii, meu nome é {self.nome}, vamos conversar?"

    def executa_comando(self, cmd):
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
        return f' {self.nome} diz: Ebaa, que legal que me escolhesse'

    def despedida(self):
        return f' {self.nome} diz: Ahh, que pena, foi legal nossa conversa, até a próxima!'
