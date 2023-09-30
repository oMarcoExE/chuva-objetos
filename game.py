import pygame
from sys import exit

def animacao_perso():
    global jogador_ìndex
    jogador_parado_rect.x += movimento_personagem

    #Voando
    if movimento_personagem == 0:
        jogador_surface = jogador_parado_surfaces
    else: 
        jogador_surface = jogador_voar

    #Passa de imagem para realiza a Animação
    jogador_ìndex += 0.11
    if jogador_ìndex > len(jogador_surface) -1:
        jogador_ìndex = 0

    if direcao_perso == 1:
        jogador = pygame.transform.flip(jogador_surface[int(jogador_ìndex)], True, False)
    else:
        jogador = jogador_surface[int(jogador_ìndex)]

    #Desenha o personagem na tela
    tela.blit(jogador, jogador_parado_rect)

#Inicializa o pygame
pygame.init()

#criar tela
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)

#Defini o Titulo da Janela
pygame.display.set_caption("Cara que anda")

##
## Importar arquivos necessários
##
plano_fundo = pygame.image.load('assets/fundo/Night-Background8.png').convert_alpha()
fundo_estrelas = pygame.image.load('assets/fundo/Night-Background7.png').convert_alpha()
fundo_estrelas_2 = pygame.image.load('assets/fundo/Night-Background6.png').convert_alpha()
fundo_estrelas_3 = pygame.image.load('assets/fundo/Night-Background5.png').convert_alpha()
fundo_rochas = pygame.image.load('assets/fundo/Night-Background4.png').convert_alpha()
fundo_chao = pygame.image.load('assets/fundo/Night-Background3.png').convert_alpha()
fundo_lua = pygame.image.load('assets/fundo/Night-Background2.png').convert_alpha()
fundo_rochas_voadoras = pygame.image.load('assets/fundo/Night-Background1.png').convert_alpha()

##Importa o jogador voando
jogador_voar = []

for imagem in range(1, 9):
    img = pygame.image.load(f'assets/jogador/voar/Hero Boy Fly{imagem}.png')
    jogador_voar.append(img)

##importa personagem
jogador_ìndex = 0
jogador_parado_surfaces = []

for imagem in range(1, 14):
    img = pygame.image.load(f'assets/jogador/parado/Hero Boy Idle{imagem}.png')
    jogador_parado_surfaces.append(img)

jogador_parado_rect = jogador_parado_surfaces[jogador_ìndex].get_rect(midbottom = (100, 530))

#Transforma o tamanho da imagem de fundo
plano_fundo = pygame.transform.scale(plano_fundo, tamanho)
fundo_estrelas = pygame.transform.scale(fundo_estrelas, tamanho)
fundo_estrelas_2 = pygame.transform.scale(fundo_estrelas_2, tamanho)
fundo_estrelas_3 = pygame.transform.scale(fundo_estrelas_3, tamanho)
fundo_rochas = pygame.transform.scale(fundo_rochas, tamanho)
fundo_chao = pygame.transform.scale(fundo_chao, tamanho)
fundo_lua = pygame.transform.scale(fundo_lua, tamanho)
fundo_rochas_voadoras = pygame.transform.scale(fundo_rochas_voadoras, tamanho)

#Cria um relógio para controlar o FPS
relogio = pygame.time.Clock()

movimento_personagem = 0
direcao_perso = 0
#loop principal do jogo
while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_RIGHT:
                direcao_perso = 1
                movimento_personagem = 5

            if evento.key == pygame.K_LEFT:
                direcao_perso = 0
                movimento_personagem = -5
    else:
        movimento_personagem = 0


    tela.blit(plano_fundo, (0, 0))
    tela.blit(fundo_estrelas, (0, 0))
    tela.blit(fundo_estrelas_2, (0, 0))
    tela.blit(fundo_estrelas_3, (0, 0))
    tela.blit(fundo_rochas, (0, 0))
    tela.blit(fundo_chao, (0, 0))
    tela.blit(fundo_lua, (0, 0))
    tela.blit(fundo_rochas_voadoras, (0, 0))

    #Calcula o movimento do personagem
    
    animacao_perso()

    #Atualiza a tela do conteudo
    pygame.display.update()

    #Defini a quantidade de frames por segundo
    relogio.tick(60)