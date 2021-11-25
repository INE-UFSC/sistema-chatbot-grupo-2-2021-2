from Bot import Bot

class BotFeliz(Bot):
    def __init__(self):
        self.__nome = "BotFeliz"

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    def apresentacao(self):
        apresentacao = "Oii, meu nome é BotFeliz, vamos conversar?"
        print(apresentacao)
 
    def mostra_comandos(self):
        comandos = """1 - Bom dia\n2 - Qual o seu nome?\n3 - Quero um conselho\n4 - Adeus"""
        print(comandos)

    def executa_comando(self,cmd):
        if cmd == 1:
            print("Bomm diaaa flor do dia s2 s2 s2, o sol está lindo hoje")
        elif cmd == 2:
            print("Meu nome é BotFeliz, e o seu? Vamos ser amigos!?!?!?")
        elif cmd == 3:
            print("Você está pensando demais, apenas aproveite a vida e seja feliz")
        elif cmd == 4:
            self.despedida
        
    def boas_vindas(self):
        boas_vindas = "BotFeliz diz: Ebaa, que legal que me escolhesse"
        print(boas_vindas)
        
    def despedida(self):
        despedida ="Ahh, que pena, foi legal nossa conversa, até a próxima!"
        print(despedida)
