import pygame
from sys import exit
from random import randint, choice

#Função para animação do personagem

def colisoes_jogador():

    global moeda, coracao

    for objeto in objetosPrinc:
        if jogador_parado_rect.colliderect(objeto['objeto']):
            if objeto['tipo'] == 'Projetil':
                coracao -= 1

            if objeto['tipo'] == 'Moeda':
                moeda += 1

            if objeto['tipo'] == 'Coração':
                coracao += 1

            objetosPrinc.remove(objeto)

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

def adicionar_objeto():
    global objetosPrinc

    objetos_lista_aleatorio = ['Coração'] * 10 + ['Moeda'] * 10 + ['Projetil'] * 80
    tipo_objeto = choice(objetos_lista_aleatorio)

    posicao = (randint(-10, 950), randint (-100, 0))
    velocidade = randint(5, 10)

    if tipo_objeto == 'Projetil':
        objeto_rect = proj_surface[0].get_rect(center=posicao)
    elif tipo_objeto == 'Coração':
         objeto_rect = coracao_surface[0].get_rect(center=posicao)
    elif tipo_objeto == 'Moeda':
         objeto_rect = moeda_surface[0].get_rect(center=posicao)

    objetosPrinc.append({
         'tipo': tipo_objeto,
         'objeto': objeto_rect,
         'velocidade': velocidade
    })

def movimento_objetos():
    global objetosPrinc

    for objeto in objetosPrinc:
        objeto['objeto'].y += objeto['velocidade']
        

        if objeto['tipo'] == 'Projetil':
            tela.blit(proj_surface[proj_index], objeto['objeto'])
        elif objeto['tipo'] == 'Coração':
            tela.blit(coracao_surface[coracao_index], objeto['objeto'])
        elif objeto['tipo'] == 'Moeda':
            tela.blit(moeda_surface[moeda_index], objeto['objeto'])

        if objeto['objeto'].y > 540:
             objetosPrinc.remove(objeto)
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


#coracao import
coracao_surface = []
coracao_index = 0

for imagem in range (1, 4):
    img = pygame.image.load(f'assets/objetos/coracao/Heart{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (80, 80))
coracao_surface.append(img)

#moeda import
moeda_surface = []
moeda_index = 0

for imagem in range (1, 5):
    img = pygame.image.load(f'assets\objetos\moeda\Coin-A{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (80, 80))
moeda_surface.append(img)

#projetil import
proj_surface = []
proj_index = 0

for imagem in range (1, 4):
    img = pygame.image.load(f'assets\objetos\projetil\Hero Bullet{imagem}.png').convert_alpha()
proj_surface.append(img)

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

#controla se o personagem esta movimentando
movimento_personagem = 0
direcao_perso = 0

new_objeto_timer = pygame.USEREVENT + 1
pygame.time.set_timer(new_objeto_timer, 500)

objetosPrinc = []
#loop principal do jogo

jogo_ativo = True

coracao = 3
moeda = 0

while jogo_ativo:

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

        if evento.key == pygame.K_ESCAPE:
            jogo_ativo = False
            
    if evento.type == pygame.KEYUP:
        if evento.key == pygame.K_RIGHT:
            movimento_personagem = 0
        if evento.key == pygame.K_LEFT:
            movimento_personagem = 0

    if evento.type == new_objeto_timer:
        adicionar_objeto()

    tela.blit(plano_fundo, (0, 0))
    tela.blit(fundo_estrelas, (0, 0))
    tela.blit(fundo_estrelas_2, (0, 0))
    tela.blit(fundo_estrelas_3, (0, 0))
    tela.blit(fundo_rochas, (0, 0))
    tela.blit(fundo_chao, (0, 0))
    tela.blit(fundo_lua, (0, 0))
    tela.blit(fundo_rochas_voadoras, (0, 0))

    #Chama a função para animar
    animacao_perso()
    movimento_objetos()
    colisoes_jogador()
    
    #Atualiza a tela do conteudo
    pygame.display.update()

    #Defini a quantidade de frames por segundo
    relogio.tick(60)