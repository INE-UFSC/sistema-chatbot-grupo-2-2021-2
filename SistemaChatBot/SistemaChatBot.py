from Bots.Bot import Bot


class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        self.__bot = None

        for bot in lista_bots:
            if type(bot) != Bot:
                raise Exception('Tipo de BOT inválido')
        self.__lista_bots = lista_bots

    def boas_vindas(self):
        print(
            f'Seja bem vindo ao sistema de chat bots da empresa {self.__empresa}')

    def mostra_menu(self):
        print('Os bots disponíveis para lhe atender no momento são: ')
        for index, bot in enumerate(self.__lista_bots):
            print(
                f'{index+1} - Bot: {bot.nome} - Mensagem de apresentação: {bot.apresentacao}')

        self.escolhe_bot()

    def escolhe_bot(self):
        while True:
            bot_escolhido = input('Digite o número do bot desejado: ')
            if not bot_escolhido.isnumeric:
                print('Entrada inválida, escolha um número')
            elif int(bot_escolhido) > len(self.__lista_bots) or int(bot_escolhido) < 1:
                print(f'Escolha um bot entre 1 e {len(self.__lista_bots)}')
            else:
                break

        self.__bot = self.__lista_bots[bot_escolhido - 1]

    def mostra_comandos_bot(self):
        self.__bot.mostra_comandos()

    def le_envia_comando(self):
        comando_escolhido = input(
            'Digite o comando desejado (-1 para fechar o programa): ')
        if comando_escolhido == -1:
            return True
        else:
            self.__bot.executa_comando(comando_escolhido)

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        self.__bot.boas_vindas()
        print()
        while True:
            self.mostra_comandos_bot()
            fechar_programa = self.le_envia_comando()

            if fechar_programa:
                self.__bot.despedida()
                break
            print()
