import pygame
import os
import random

# Tamanho da Tela
TELA_LARGURA = 500
TELA_ALTURA = 800

# Definindo as imagens padrão
IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


class Passaro:
    # CONSTANTES DO PASSÁRO
    IMGS = IMAGENS_PASSARO
    ## animações da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    # ATRIBUTOS INICIAIS DO PASSÁRO
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]
    
    # FUNÇÃO PARA O PASSÁRO PULAR
    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y
    
    # FUNÇÃO DE MOVIMENTO DO PASSÁRO
    def mover(self):
        ## calcular deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        ## restrigir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2
        
        self.y += deslocamento

        ## definir angulo do passáro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO
    
    def desenhar(self, tela):
        # DEFINIR IMAGEM DA ANIMAÇÃO

        # definir a imagem que o passáro vai utilizar
        self.contagem_imagem += 1
        
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]

        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO * 4+1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        # se o passáro estiver caindo, não bater asa
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO * 2
            
        # desenhar a imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y).center)
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        # CRIANDO MÁSCARA PARA COLISÃO PELOS PIXELS PREENCHIDOS DA IMAGEM DO PASSÁRO

        ## criando máscara para o passáro
        pygame.mask.from_surface(self.imagem)

class Cano:
    pass

class Chao:
    pass