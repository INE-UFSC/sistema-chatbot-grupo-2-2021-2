from Bots.Bot import Bot

class BotManezinho(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.__comandos = {"1":"Ô meu querido, quesh saber quantas praias existem na nossa linda ilha da magia?",
                           "2":"Essa é complicada, Avaí ou Figueira?",
                           "3":"Mofas com a pomba na balaia?",
                           "4":"O que é bucica?"}

    @property
    def comandos(self):
        return self.__comandos

    def apresentacao(self):
        return f"Ó-lhó-lhó, me chamo {self.nome}. Quex conversar comigo?"

    def executa_comando(self, cmd):
        if cmd == "1":
            return f'{self.nome} diz: A nossa belíssima ilha conta com incríveis 42 praias!'
        elif cmd == "2":
            return f'{self.nome} diz: Furacão ou Leão? Essa é difícil hein!'
        elif cmd == "3":
            return f' {self.nome} diz: Ô meu querido, isso significa que a pessoa não vai alcançar o seu objetivo, tendesse?'
        elif cmd == "4":
            return f' {self.nome} diz: Bucica é como a gente chama as nossas cadelinhas aqui da ilha!'
        else:
            return 'Uhhh seu tanso! Não é assim não, pô!'

    def boas_vindas(self):
        return f' {self.nome} diz: Me excolhesse mesmo, és um baita, feio!'

    def despedida(self):
        return f' {self.nome} diz: Valeu pelo papo, nego, dazumbanho! Agora segue reto toda vida que eu vou me ajojar aqui'