from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome


    @property 
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    def apresentacao(self):
        return 'Meu nome é',self.__nome,'e e estou com muita RAIVA!!'
    def mostra_comandos(self):
        print('1: Ola, tudo bem?')
        print('2: Come você está?')
        print('3: Me de um conselho')
        print('4: Adeus')
    
    def executa_comando(self,cmd):
        
        if cmd == 1:
            print('E o que tem de bom?!')
        elif cmd == 2:
            print('Com muita raiva!')
        elif cmd == 3:
            print('Não tenho filho deste tamanho')
        elif cmd == 4:
            print('Até nunca mais!')

    def boas_vindas(self):
        return 'Não acredito que você me escolheu!'

    def despedida(self):
        return 'Finalmente, até nunca mais '


