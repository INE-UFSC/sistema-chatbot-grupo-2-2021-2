from Bots.Bot import Bot

class BotMusical(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.__comandos = {'1': 'Bom dia', '2': 'Quem é você?',
                           '3': 'Como vai ser o futuro?', '4': 'Adeus'}

    @property
    def comandos(self):
        return self.__comandos

    def apresentacao(self):
        return f'Deixa eu me apresentar, que eu acabei de chegar! Meu nome é {self.nome}!'
 
    def executa_comando(self, cmd):
        if cmd == '1':
            return self.boas_vindas()
        elif cmd =='2':
            return self.quem_e()
        elif cmd == '3':
            return self.futuro()
        elif cmd == '4':
            return self.despedida()
        else:
            return f'Comando não encontrado'
           
    def boas_vindas(self):
        return 'Alguma coisa acontece no meu coração... Ah, oi! Bom dia!'

    def quem_e(self):
        return f'EU SOU O SAMBAAA! Brincadeira, eu sou {self.nome}!'

    def futuro(self):
        return 'Eu vejo a vida melhor no futuro, eu vejo isso por cima de um muro\nde hipocrisia que insiste em nos rodear...'

    def despedida(self):
        return 'Deixe-me ir, preciso andar, vou por aí a procurar... Rir pra não chorar! Tchaau!'

