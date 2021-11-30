#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotManezinho import BotManezinho
from Bots.BotMinerin import BotMinerin
from Bots.BotCansado import BotCansado
from Bots.BotLegal import BotLegal

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotZangado('Luke'), BotFeliz('João'), BotFeliz('Gabriel'), BotManezinho('Augusto'), BotMinerin('Thiago'),BotLegal('Feijao (grupo 4)',BotCansado('Pedro (Grupo 3)')]


sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
