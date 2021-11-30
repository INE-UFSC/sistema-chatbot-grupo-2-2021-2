#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotManezinho import BotManezinho
from Bots.BotMinerin import BotMinerin

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotZangado('Luke'), BotFeliz('João'), BotFeliz('Gabriel'), BotManezinho('Augusto'), BotMinerin('Thiago')]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
