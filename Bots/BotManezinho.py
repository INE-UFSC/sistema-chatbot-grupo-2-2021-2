from Bots.Bot import Bot


class BotManezinho(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = {'1': "Ô meu querido, quesh saber quantas praias existem na nossa linda ilha da magia?",
                           '2': "Essa é complicada, Avaí ou Figueira?",
                           '3': "Mofas com a pomba na balaia?",
                           '4': "O que é bucica?"}
        self.__respostas = {"Ô meu querido, quesh saber quantas praias existem na nossa linda ilha da magia?": "\nA nossa belíssima ilha conta com incríveis 42 praias!",
                            "Essa é complicada, Avaí ou Figueira?": "\nFuracão ou Leão? Essa é difícil hein!",
                            "Mofas com a pomba na balaia?": "\nÔ meu querido, isso significa que a pessoa não vai alcançar o seu objetivo, tendesse?",
                            "O que é bucica?": "\nBucica é como a gente chama as nossas cadelinhas aqui da ilha!"}

    @property
    def nome(self):
        return self.__nome

    @property
    def comandos(self):
        return self.__comandos

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return f"Ó-lhó-lhó, me chamo {self.__nome}. Quex conversar comigo?"

    def executa_comando(self, cmd):
        if cmd == '1':
            return self.__respostas["Ô meu querido, quesh saber quantas praias existem na nossa linda ilha da magia?"]
        elif cmd == '2':
            return self.__respostas["Essa é complicada, Avaí ou Figueira?"]
        elif cmd == '3':
            return self.__respostas["Mofas com a pomba na balaia?"]
        elif cmd == '4':
            return self.__respostas["O que é bucica?"]
        else:
            return "Uhhh seu tanso! Não é assim não, pô!"

    def boas_vindas(self):
        return f"Me excolhesse mesmo, és um baita, feio!"

    def despedida(self):
        print("Valeu pelo papo, nego, dazumbanho! Agora segue reto toda vida que eu vou me ajojar aqui")
