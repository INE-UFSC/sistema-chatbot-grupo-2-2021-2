#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotCansado import BotCansado

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotZangado('Luke'), BotFeliz('João'), BotFeliz('Gabriel'), BotCansado('Pedro (Grupo 3)')]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
