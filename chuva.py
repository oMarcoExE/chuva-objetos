import pygame
from sys import exit

# Inicializa o pygame
pygame.init()

# Cria a tela
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)

# Define o título da janela
pygame.display.set_caption('ChuvaMortal')

# Cria o relógio para controlar o FPS
relogio = pygame.time.Clock()

# Carrega os arquivos necessários para o jogo
fonte_pixel = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

## Carrega as imagens de fundo
plano_fundo = pygame.image.load('assets/fundo/Night-Background8.png').convert()
fundo_estrelas = pygame.image.load('assets/fundo/Night-Background7.png').convert()
fundo_estrelas_2 = pygame.image.load('assets/fundo/Night-Background6.png').convert()
fundo_estrelas_3 = pygame.image.load('assets/fundo/Night-Background5.png').convert()
fundo_rochas = pygame.image.load('assets/fundo/Night-Background4.png').convert()
fundo_chao = pygame.image.load('assets/fundo/Night-Background3.png').convert()
fundo_lua = pygame.image.load('assets/fundo/Night-Background2.png').convert()
fundo_rochas_voadoras = pygame.image.load('assets/fundo/Night-Background1.png').convert()

# Transforma as imagens de fundo para o tamanho da tela
plano_fundo = pygame.transform.scale(plano_fundo, tamanho)
fundo_estrelas = pygame.transform.scale(fundo_estrelas, tamanho)
fundo_estrelas_2 = pygame.transform.scale(fundo_estrelas_2, tamanho)
fundo_estrelas_3 = pygame.transform.scale(fundo_estrelas_3, tamanho)
fundo_rochas = pygame.transform.scale(fundo_rochas, tamanho)
fundo_chao = pygame.transform.scale(fundo_chao, tamanho)
fundo_lua = pygame.transform.scale(fundo_lua, tamanho)
fundo_rochas_voadoras = pygame.transform.scale(fundo_rochas_voadoras, tamanho)

## Carrega as imagens do jogador para dentro de uma lista
jogador_parado_surfaces = []
for imagem in range(1, 14):
    img = pygame.image.load(f'assets/jogador/parado/Hero Boy Idle{imagem}.png').convert_alpha()
    jogador_parado_surfaces.append(img)

# Define um index para qual imagem será usada
jogador_index = 0

# Define um retângulo para posicionar a imagem do jogador
jogador_parado_retangle = jogador_parado_surfaces[jogador_index].get_rect(center=(100, 430))

# Define a velocidade de movimento do jogador
movimento_jogador = 0

# Define a direção que o jogador está indo
direcao_jogador = 0

# Laço principal do jogo
while True:

    # Le os eventos do jogo
    for evento in pygame.event.get():

        # Verifica se o jogador quer sair
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Verifica se o jogador pressionou alguma tecla
        if evento.type == pygame.KEYDOWN:

            # Verifica se o jogador pressionou a seta para direita
            if evento.key == pygame.K_RIGHT:
                movimento_jogador = 5
                direcao_jogador = 1

            # Verifica se o jogador pressionou a seta para esquerda
            if evento.key == pygame.K_LEFT:
                movimento_jogador = -5
                direcao_jogador = -1

        # Verifica se o jogador soltou alguma tecla
        if evento.type == pygame.KEYUP:
                
                # Verifica se o jogador soltou a seta para direita
                if evento.key == pygame.K_RIGHT:
                    movimento_jogador = 0
    
                # Verifica se o jogador soltou a seta para esquerda
                if evento.key == pygame.K_LEFT:
                    movimento_jogador = 0

    # Desenha o fundo do jogo
    tela.blit(plano_fundo, (0, 0))
    tela.blit(fundo_estrelas, (0, 0))
    tela.blit(fundo_estrelas_2, (0, 0))
    tela.blit(fundo_estrelas_3, (0, 0))
    tela.blit(fundo_rochas, (0, 0))
    tela.blit(fundo_chao, (0, 0))
    tela.blit(fundo_lua, (0, 0))
    tela.blit(fundo_rochas_voadoras, (0, 0))

    # Desenha e atualiza a imagem do jogador
    if jogador_index >= 12:
        jogador_index = 0
    
    jogador_index += 0.11

    # Movimenta o jogador
    jogador_parado_retangle.x += movimento_jogador

    # Impede que o jogador saia da tela
    if jogador_parado_retangle.left <= -30:
        jogador_parado_retangle.left = -30
    elif jogador_parado_retangle.right >= 1000:
        jogador_parado_retangle.right = 1000

    # Vira o jogador para a direção que ele está indo
    if direcao_jogador == 1:
        jogador = pygame.transform.flip(jogador_parado_surfaces[int(jogador_index)], True, False)
    else:
        jogador = jogador_parado_surfaces[int(jogador_index)]

    # Desenha o jogador na tela
    tela.blit(jogador, jogador_parado_retangle)

    # Atualiza a tela
    pygame.display.update()

    # Define o FPS (quantas vezes o loop será executado por segundo)
    relogio.tick(60)