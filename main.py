import math

from math3D import *
import pygame


Display = Screen((800,800), (400,400, 200), (0,0,0))
Cam = Camera((0, 100, -10), (0, 0, 0))
Tiles = []
TileSize = 100
for x in range(-10, 11):
    for z in range(-10, 11):
        r = (x + z) % 2
        Tiles.append(Poly((
            (x*TileSize-TileSize/2, 500, z*TileSize-TileSize/2),
            (x*TileSize-TileSize/2, 500, z*TileSize+TileSize/2),
            (x*TileSize+TileSize/2, 500, z*TileSize+TileSize/2),
            (x*TileSize+TileSize/2, 500, z*TileSize-TileSize/2)),
            (255*r,0,255*(1-r))))

Display.DrawToScreen()

Move = [0, 0, 0]
Rote = [0, 0, 0]
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Move[2] = 2
            elif event.key == pygame.K_s:
                Move[2] = -2
            elif event.key == pygame.K_a:
                Move[0] = -2
            elif event.key == pygame.K_d:
                Move[0] = 2
            elif event.key == pygame.K_q:
                Rote[1] = 0.3
            elif event.key == pygame.K_e:
                Rote[1] = -0.3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                Move[2] = 0
            elif event.key == pygame.K_s:
                Move[2] = 0
            elif event.key == pygame.K_a:
                Move[0] = 0
            elif event.key == pygame.K_d:
                Move[0] = 0
            elif event.key == pygame.K_q:
                Rote[1] = 0
            elif event.key == pygame.K_e:
                Rote[1] = 0

    Cam.Update([Move[2] * math.sin(-radians(Cam.Rotations[1])) + Move[0] * math.cos(radians(Cam.Rotations[1])),
                0,
                Move[2] * math.cos(-radians(Cam.Rotations[1])) + Move[0] * math.sin(radians(Cam.Rotations[1]))],
               Rote)
    for Tile in Tiles:
        Tile.Draw(Cam, Display)
    Display.DrawToScreen()
    pass