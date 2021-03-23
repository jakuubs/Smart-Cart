import os
import pygame
BLOCK_SIZE = 100
DIRT = pygame.image.load(os.path.join('resources', 'dirt.png'))
DIRT = pygame.transform.scale(DIRT, (BLOCK_SIZE, BLOCK_SIZE))
FARMLAND = pygame.image.load(os.path.join('resources', 'farmland.png'))
FARMLAND = pygame.transform.scale(FARMLAND, (BLOCK_SIZE, BLOCK_SIZE))
FARMLANDMOIST = pygame.image.load(os.path.join('resources', 'farmland_moist.png'))
FARMLANDMOIST = pygame.transform.scale(FARMLANDMOIST, (BLOCK_SIZE, BLOCK_SIZE))
FPS = 1
WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
TRACTOR = pygame.image.load(os.path.join('resources', 'tractor.png'))
TRACTOR = pygame.transform.scale(TRACTOR, (BLOCK_SIZE, BLOCK_SIZE))
WHEAT_GROW_TIME = 5
WHEAT_MAXIMUM_STATE = 21
WHEATSTAGE1 = pygame.image.load(os.path.join('resources', 'wheat_stage1.png'))
WHEATSTAGE1 = pygame.transform.scale(WHEATSTAGE1, (BLOCK_SIZE, BLOCK_SIZE))
WHEATSTAGE2 = pygame.image.load(os.path.join('resources', 'wheat_stage2.png'))
WHEATSTAGE2 = pygame.transform.scale(WHEATSTAGE2, (BLOCK_SIZE, BLOCK_SIZE))
WHEATSTAGE3 = pygame.image.load(os.path.join('resources', 'wheat_stage3.png'))
WHEATSTAGE3 = pygame.transform.scale(WHEATSTAGE3, (BLOCK_SIZE, BLOCK_SIZE))
WHEATSTAGE4 = pygame.image.load(os.path.join('resources', 'wheat_stage4.png'))
WHEATSTAGE4 = pygame.transform.scale(WHEATSTAGE4, (BLOCK_SIZE, BLOCK_SIZE))
WHEATSTAGE5 = pygame.image.load(os.path.join('resources', 'wheat_stage5.png'))
WHEATSTAGE5 = pygame.transform.scale(WHEATSTAGE5, (BLOCK_SIZE, BLOCK_SIZE))