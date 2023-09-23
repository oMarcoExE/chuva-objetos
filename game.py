import pygame

#inicializa o pygame
pygame.init()

#criar tela
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)

#Defini o Titulo da Janela
pygame.display.set_caption("Chuva Mortal")

#Cria um relógio para controlar o FPS
relogio = pygame.time.Clock()