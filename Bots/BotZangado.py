from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {"1":"Olá, tudo bem ? ", "2":"Como você está ?", "3":"Quero um conselho", "4": "Adeus"}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    def apresentacao(self):
        return f'GRRRRRR Meu nome é {self.__nome} e não me incomode!'

    def executa_comando(self,cmd):

        if cmd == 1:
            print('E o que tem de bom?!')
        elif cmd == 2:
            print('Não interesa!')
        elif cmd == 3:
            print('Não tenho filho deste tamanho')
        elif cmd == 4:
            print('Até nunca mais!')

    def boas_vindas(self):
        return f' {self.nome} diz: Não acredito que você me escolheu!'

    def despedida(self):
        return f' {self.nome} diz: Finalmente, até nunca mais! '
