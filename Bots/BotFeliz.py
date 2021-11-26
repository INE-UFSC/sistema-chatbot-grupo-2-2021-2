from Bots.Bot import Bot


class BotFeliz(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = {"1": "Bom dia",
                           "2": "Qual o sue nome?",
                           "3": "Quero um conselho",
                           "4": "Adeus"}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return f"Oii, meu nome é {self.__nome}, vamos conversar?"

    def executa_comando(self, cmd):
        if cmd == 1:
            print("Bomm diaaa flor do dia s2 s2 s2, o sol está lindo hoje")
        elif cmd == 2:
            print(f"Meu nome é {self.__nome}, e o seu? Vamos ser amigos!?!?!?")
        elif cmd == 3:
            print("Você está pensando demais, apenas aproveite a vida e seja feliz")
        elif cmd == 4:
            self.despedida
        else:
            print('Comando não encontrado')

    def boas_vindas(self):
        boas_vindas = f"{self.__nome} diz: Ebaa, que legal que me escolhesse"
        print(boas_vindas)

    def despedida(self):
        despedida = "Ahh, que pena, foi legal nossa conversa, até a próxima!"
        print(despedida)
