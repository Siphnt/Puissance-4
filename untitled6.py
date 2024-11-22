#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 10:13:41 2023

@author: jp.giard

d'après
https://www.zonensi.fr/Miscellanees/Pygame/Base_pygame/
"""

import pygame
from pygame.locals import *
import time

pygame.init()

fenetre = pygame.display.set_mode((1000, 800))

fond = pygame.image.load("fond.jpg").convert()
diablo = pygame.image.load("jeton.png").convert_alpha()
diablo2 = pygame.image.load("jeton2.png").convert_alpha()
pygame.mixer.music.load('thune.mp3')
pygame.mixer.music.play(-1, 0.0, 0)
position = (0, 0)
i = 850
j = 80
m = 850
n = 200
jouer = {}
tour1 = True
tour2 = False
a = 650
b = 650
c = 650
d = 650
e = 650
f = 650
g = 650
a1 = 0
b1 = 0
c1 = 0
d1 = 0
e1 = 0
f1 = 0
g1 = 0
continuer = True
tab = [  # colonne par colonne
    [0, 0, 0, 0, 0, 0],  # col 0
    [0, 0, 0, 0, 0, 0],  # col 1
    [0, 0, 0, 0, 0, 0],  # col 2
    [0, 0, 0, 0, 0, 0],  # col 3
    [0, 0, 0, 0, 0, 0],  # col 4
    [0, 0, 0, 0, 0, 0],  # col 5
    [0, 0, 0, 0, 0, 0]   # col 6
]
colonnes = [27, 107, 187, 267, 347, 427, 507]
lignes = [329, 409, 489, 569, 649, 729]

def ifwin(x, y, color):  # coordonnées et couleur du nouveau jeton
    l = [(x, y)]
    # test gauche-droite
    while True:
        if len(l) == 4:
            return True
        if l[-1][0] < 6 and tab[l[-1][0] + 1][l[-1][1]] == color:  # regarde à droite
            l.append((l[-1][0] + 1, l[-1][1]))
        elif l[0][0] > 0 and tab[l[0][0] - 1][l[0][1]] == color:  # regarde à gauche
            l.insert(0, (l[0][0] - 1, l[0][1]))
        else:
            break
    # test haut-bas
    l = [(x, y)]
    while True:
        if len(l) == 4:
            return True
        if l[0][1] > 0 and tab[l[0][0]][l[0][1] - 1] == color:  # regarde en bas
            l.insert(0, (l[0][0], l[0][1] - 1))
        else:
            break
    # test en haut à gauche - en bas à droite
    l = [(x, y)]
    while True:
        if len(l) == 4:
            return True
        if l[-1][0] < 6 and l[-1][1] > 0 and tab[l[-1][0] + 1][l[-1][1] - 1] == color:  # regarde en bas à droite
            l.append((l[-1][0] + 1, l[-1][1] - 1))
        elif l[0][0] > 0 and l[0][1] < 5 and tab[l[0][0] - 1][l[0][1] + 1] == color:  # regarde en haut à gauche
            l.insert(0, (l[0][0] - 1, l[0][1] + 1))
        else:
            break
    # test en bas à gauche - en haut à droite
    l = [(x, y)]
    while True:
        if len(l) == 4:
            return True
        if l[-1][0] < 6 and l[-1][1] < 5 and tab[l[-1][0] + 1][l[-1][1] + 1] == color:  # regarde en haut à droite
            l.append((l[-1][0] + 1, l[-1][1] + 1))
        elif l[0][0] > 0 and l[0][1] > 0 and tab[l[0][0] - 1][l[0][1] - 1] == color:  # regarde en bas à gauche
            l.insert(0, (l[0][0] - 1, l[0][1] - 1))
        else:
            break
    return False

while continuer:
    time.sleep(0.01)
    fenetre.blit(fond, (0, 0))
    fenetre.blit(diablo, (i, j))
    fenetre.blit(diablo2, (m, n))

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if tour1 and i <= position[0] <= i + 100 and j <= position[1] <= j + 106:
                dragging = 'D'
            elif tour2 and m <= position[0] <= m + 100 and n <= position[1] <= n + 106:
                dragging = 'N'
        if event.type == MOUSEBUTTONUP:
            if dragging == 'D':
                if 40 < i < 100:
                    j = 80
                    i = 850
                    jouer[(50, a)] = 'D'
                    a -= 105
                    tab[0][a1] = 1
                    if ifwin(0, a1, 1):
                        continuer = False
                    a1 += 1
                elif 140 < i < 200:
                    j = 80
                    i = 850
                    jouer[(155, b)] = 'D'
                    b -= 105
                    tab[1][b1] = 1
                    if ifwin(1, b1, 1):
                        continuer = False
                    b1 += 1
                elif 240 < i < 300:
                    j = 80
                    i = 850
                    jouer[(260, c)] = 'D'
                    c -= 105
                    tab[2][c1] = 1
                    if ifwin(2, c1, 1):
                        continuer = False
                    c1 += 1
                elif 340 < i < 400:
                    j = 80
                    i = 850
                    jouer[(365, d)] = 'D'
                    d -= 105
                    tab[3][d1] = 1
                    if ifwin(3, d1, 1):
                        continuer = False
                    d1 += 1
                elif 440 < i < 500:
                    j = 80
                    i = 850
                    jouer[(470, e)] = 'D'
                    e -= 105
                    tab[4][e1] = 1
                    if ifwin(4, e1, 1):
                        continuer = False
                    e1 += 1
                elif 540 < i < 600:
                    j = 80
                    i = 850
                    jouer[(575, f)] = 'D'
                    f -= 105
                    tab[5][f1] = 1
                    if ifwin(5, f1, 1):
                        continuer = False
                    f1 += 1
                elif 640 < i < 700:
                    j = 80
                    i = 850
                    jouer[(680, g)] = 'D'
                    g -= 105
                    tab[6][g1] = 1
                    if ifwin(6, g1, 1):
                        continuer = False
                    g1 += 1
                tour1 = False
                tour2 = True
            elif dragging == 'N':
                if 40 < m < 100:
                    m = 850
                    n = 200
                    jouer[(50, a)] = 'N'
                    a -= 105
                    tab[0][a1] = 2
                    if ifwin(0, a1, 2):
                        continuer = False
                    a1 += 1
                elif 140 < m < 200:
                    m = 850
                    n = 200
                    jouer[(155, b)] = 'N'
                    b -= 105
                    tab[1][b1] = 2
                    if ifwin(1, b1, 2):
                        continuer = False
                    b1 += 1
                elif 240 < m < 300:
                    m = 850
                    n = 200
                    jouer[(260, c)] = 'N'
                    c -= 105
                    tab[2][c1] = 2
                    if ifwin(2, c1, 2):
                        continuer = False
                    c1 += 1
                elif 340 < m < 400:
                    m = 850
                    n = 200
                    jouer[(365, d)] = 'N'
                    d -= 105
                    tab[3][d1] = 2
                    if ifwin(3, d1, 2):
                        continuer = False
                    d1 += 1
                elif 440 < m < 500:
                    m = 850
                    n = 200
                    jouer[(470, e)] = 'N'
                    e -= 105
                    tab[4][e1] = 2
                    if ifwin(4, e1, 2):
                        continuer = False
                    e1 += 1
                elif 540 < m < 600:
                    m = 850
                    n = 200
                    jouer[(575, f)] = 'N'
                    f -= 105
                    tab[5][f1] = 2
                    if ifwin(5, f1, 2):
                        continuer = False
                    f1 += 1
                elif 640 < m < 700:
                    m = 850
                    n = 200
                    jouer[(680, g)] = 'N'
                    g -= 105
                    tab[6][g1] = 2
                    if ifwin(6, g1, 2):
                        continuer = False
                    g1 += 1
                tour1 = True
                tour2 = False
            dragging = None

    if pygame.mouse.get_pressed()[0]:
        position = pygame.mouse.get_pos()
        if dragging == 'D':
            i = position[0] - 50
            j = position[1] - 50
        elif dragging == 'N':
            m = position[0] - 50
            n = position[1] - 50

    for cle in jouer:
        if jouer[cle] == 'D':
            fenetre.blit(diablo, cle)
        else:
            fenetre.blit(diablo2, cle)

    pygame.display.update()
    # print(position)
    print(tab)
    # print(m, n)

pygame.quit()
