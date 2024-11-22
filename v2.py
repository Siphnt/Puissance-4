#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 10:13:41 2023

@author: jp.giard

d'après
https://www.zonensi.fr/Miscellanees/Pygame/Base_pygame/
"""

import pygame
from pygame import*
from pygame.locals import *
import time
pygame.init()

fenetre = pygame.display.set_mode((1000, 800))

fond=pygame.image.load("fond.jpg")
fond.convert()
#position2={[a1,(58,658)],[b1,(165,658)]}
diablo = pygame.image.load("jeton.png").convert_alpha()
diablo2 =pygame.image.load("jeton2.png").convert_alpha()
pygame.event.get()
song_background = pygame.mixer.music.load('thune.mp3')
pygame.mixer.music.play(-1, 0.0, 0)
position=(0,0)
clock=pygame.time.Clock()
touche = key.get_pressed()
i=850
j=80
m=850
n=200
jouer={}
tour1=True
tour2=False
a=650
b=650
c=650
d=650
e=650
f=650
g=650
a1=0
b1=0
c1=0
d1=0
e1=0
f1=0
g1=0
etat=0
continuer=True
tab=[#colonne par colonne
   [0,0,0,0,0,0],#col 0
   [0,0,0,0,0,0],#col 1
   [0,0,0,0,0,0],#col 2
   [0,0,0,0,0,0],#col 3
   [0,0,0,0,0,0],#col 4
   [0,0,0,0,0,0],#col 5
   [0,0,0,0,0,0]]#col 6
colonnes=[27,107,187,267,347,427,507]
lignes=[329,409,489,569,649,729]
def ifwin(x,y,color):#coordonnées et couleur du nouveau jeton
    l=[(x,y)]
    #test gauche-droite
    while True:
        if len(l)==4:
            return True
        if l[-1][0]<6 and tab[ l[-1][0] +1 ][l[-1][1] ]==color:#regarde à droite
            l.append(( l[-1][0]+1 , l[-1][1] ))
        elif l[0][0]>0 and tab[ l[0][0] -1 ][l[0][1] ]==color:#regarde à gauche
            l.insert(0,( l[0][0] -1 , l[0][1] ))
        else:
            break
    #test haut-bas
    l=[(x,y)]
    while True:
        if len(l)==4:
            return True
        if l[0][1]>0 and tab[ l[0][0] ][ l[0][1] -1 ]==color:#regarde en bas
            l.insert(0,( l[0][0] , l[0][1]-1 ))
        else:
            break
    #test en haut à gauche - en bas à droite
    l=[(x,y)]
    while True:
        if len(l)==4:
            return True
        if l[-1][0]<6 and l[-1][1]>0 and tab[ l[-1][0] +1 ][ l[-1][1] -1 ]==color:#regarde en bas à droite
            l.append(( l[-1][0] +1 , l[-1][1] -1 ))
        elif l[0][0]>0 and l[0][1]<5 and tab[ l[0][0] -1 ][ l[0][1] +1 ]==color:#regarde en haut à gauche
            l.insert(0, ( l[0][0]-1 , l[0][1]+1 ))
        else:
            break
    #test en bas à gauche - en haut à droite
    l=[(x,y)]
    while True:
        if len(l)==4:
            return True
        if l[-1][0]<6 and l[-1][1]<5 and tab[ l[-1][0] +1 ][ l[-1][1] +1 ]==color:#regarde en haut à droite
            l.append(( l[-1][0] +1 , l[-1][1] +1 ))
        elif l[0][0]>0 and l[0][1]>0 and tab[ l[0][0] -1 ][ l[0][1] -1 ]==color:#regarde en bas à gauche
            l.insert(0, ( l[0][0]-1 , l[0][1]-1 ))
        else:
            break
    return False
while continuer:

    if etat==0:
        time.sleep(0.01)
        fenetre.blit(fond, (0,0))
        fenetre.blit(diablo, (i,j)) 
        fenetre.blit(diablo2, (m,n))
        #print('a')
        
    if pygame.mouse.get_pressed(num_buttons=3)==(True,False,False):
        position=pygame.mouse.get_pos()
    if tour1==True : 
        if etat==0:
            fonte = font.SysFont('comicsansms', 40)
            text = fonte.render('Joueur 1 joue !', True, (255, 255, 255), (0, 0, 0))
            fenetre.blit(text, (20, 20))
        if i<=position[0]<=i+100 and j<=position[1]<=j+106:
            i=position[0]-50
            j=position[1]-50
            if event.type == MOUSEBUTTONUP:
                if 40<i<100:
                    while j<a:
                        j=j+0.5
                        fenetre.blit(diablo, (50,j))

                    if j==a:
                        jouer[(50,a)]='D'
                    a=a-105
                    j=80
                    i=850
                    tab[0][a1]=1
                    if ifwin(0,a1,1)==True:
                        etat=1
                        if etat==1:
                           fonte = font.SysFont('comicsansms', 40)
                           text = fonte.render('Joueur 1 a gagné !', True, (255, 255, 255), (0, 0, 0))
                           fenetre.fill((0,0,0))
                           fenetre.blit(text, (350, 290))
                           a=650
                           a1=0
                        tab=[#colonne par colonne
                          [0,0,0,0,0,0],#col 0
                          [0,0,0,0,0,0],#col 1
                          [0,0,0,0,0,0],#col 2
                          [0,0,0,0,0,0],#col 3
                          [0,0,0,0,0,0],#col 4
                          [0,0,0,0,0,0],#col 5
                          [0,0,0,0,0,0]]#col 6
                        jouer={}

                    a1=a1+1
                    tour1=False
                    tour2=True
                if 140<i<200:
                    while j<b:
                        j=j+0.5
                        fenetre.blit(diablo, (155,j))
                    if j==b:
                        jouer[(155,b)]='D'
                    j=80
                    i=850
                    
                    b=b-105
                    tab[1][b1]=1
                    if ifwin(1,b1,1)==True:
                       fonte = font.SysFont('comicsansms', 40)
                       text = fonte.render('Joueur 1 a gagné !', True, (255, 255, 255), (0, 0, 0))
                       fenetre.fill((0,0,0))
                       fenetre.blit(text, (350, 290)) 
                       
                       etat=1
                       b=650
                       b1=0
                       tab=[#colonne par colonne
                      [0,0,0,0,0,0],#col 0
                      [0,0,0,0,0,0],#col 1
                      [0,0,0,0,0,0],#col 2
                      [0,0,0,0,0,0],#col 3
                      [0,0,0,0,0,0],#col 4
                      [0,0,0,0,0,0],#col 5
                      [0,0,0,0,0,0]]#col 6
                       jouer={}
                    b1=b1+1
                    tour1=False
                    tour2=True
                if 240<i<300:
                    while j<c:
                        j=j+0.5
                        fenetre.blit(diablo, (260,j))
                    if j==c:
                        jouer[(260,c)]='D'
                    j=80
                    i=850
                   
                    c=c-105
                    tab[2][c1]=1
                    if ifwin(2,c1,1)==True:
                       fonte = font.SysFont('comicsansms', 40)
                       text = fonte.render('Joueur 1 a gagné !', True, (255, 255, 255), (0, 0, 0))
                       fenetre.fill((0,0,0))
                       fenetre.blit(text, (350, 290))
                       etat=1
                       c=650
                       c1=0
                       tab=[#colonne par colonne
                      [0,0,0,0,0,0],#col 0
                      [0,0,0,0,0,0],#col 1
                      [0,0,0,0,0,0],#col 2
                      [0,0,0,0,0,0],#col 3
                      [0,0,0,0,0,0],#col 4
                      [0,0,0,0,0,0],#col 5
                      [0,0,0,0,0,0]]#col 6
                       jouer={}
                    c1=c1+1
                    tour1=False
                    tour2=True
                if 340<i<400:
                    while j<d:
                        j=j+0.5
                        fenetre.blit(diablo, (365,j))
                    if j==d:
                        jouer[(365,d)]='D'
                    j=80
                    i=850

                    d=d-105
                    tab[3][d1]=1
                    if ifwin(3,d1,1)==True:
                       fonte = font.SysFont('comicsansms', 40)
                       text = fonte.render('Joueur 1 a gagné !', True, (255, 255, 255), (0, 0, 0))
                       fenetre.fill((0,0,0))
                       fenetre.blit(text, (350, 290))
                       etat=1
                       d=650
                       d1=0
                       tab=[#colonne par colonne
                      [0,0,0,0,0,0],#col 0
                      [0,0,0,0,0,0],#col 1
                      [0,0,0,0,0,0],#col 2
                      [0,0,0,0,0,0],#col 3
                      [0,0,0,0,0,0],#col 4
                      [0,0,0,0,0,0],#col 5
                      [0,0,0,0,0,0]]#col 6
                       jouer={}
                    d1=d1+1
                    tour1=False
                    tour2=True
                if 440<i<500:
                    while j<e:
                        j=j+0.5
                        fenetre.blit(diablo, (470,j))
                    if j==e:
                        jouer[(470,e)]='D'
                    j=80
                    i=850
                    e=e-105
                    tab[4][e1]=1
                    if ifwin(4,e1,1)==True:
                       fonte = font.SysFont('comicsansms', 40)
                       text = fonte.render('Joueur 1 a gagné !', True, (255, 255, 255), (0, 0, 0))
                       fenetre.fill((0,0,0))
                       fenetre.blit(text, (350, 290))
                       etat=1
                       e=650
                       e1=0
                       tab=[#colonne par colonne
                      [0,0,0,0,0,0],#col 0
                      [0,0,0,0,0,0],#col 1
                      [0,0,0,0,0,0],#col 2
                      [0,0,0,0,0,0],#col 3
                      [0,0,0,0,0,0],#col 4
                      [0,0,0,0,0,0],#col 5
                      [0,0,0,0,0,0]]#col 6
                       jouer={}
                    e1=e1+1
                    tour1=False
                    tour2=True
                if 540<i<600:
                    while j<f:
                        j=j+0.5
                        fenetre.blit(diablo, (575,j))
                    if j==f:
                        jouer[(575,f)]='D'
                    j=80
                    i=850
                    jouer[(575,f)]='D'
                    f=f-105
                    tab[5][f1]=1
                    if ifwin(5,f1,1)==True:
                       fonte = font.SysFont('comicsansms', 40)
                       text = fonte.render('Joueur 1 a gagné !', True, (255, 255, 255), (0, 0, 0))
                       fenetre.fill((0,0,0))
                       fenetre.blit(text, (350, 290))
                       etat=1
                       f=650
                       f1=0
                       tab=[#colonne par colonne
                      [0,0,0,0,0,0],#col 0
                      [0,0,0,0,0,0],#col 1
                      [0,0,0,0,0,0],#col 2
                      [0,0,0,0,0,0],#col 3
                      [0,0,0,0,0,0],#col 4
                      [0,0,0,0,0,0],#col 5
                      [0,0,0,0,0,0]]#col 6
                       jouer={}
                    f1=f1+1
                    tour1=False
                    tour2=True
                if 640<i<700:
                    while j<g:
                        j=j+0.5
                        fenetre.blit(diablo, (680,j))
                    if j==g:
                        jouer[(680,g)]='D'
                    j=80
                    i=850
                    g=g-105
                    tab[6][g1]=1
                    if ifwin(6,g1,1)==True:
                       fonte = font.SysFont('comicsansms', 40)
                       text = fonte.render('Joueur 1 a gagné !', True, (255, 255, 255), (0, 0, 0))
                       fenetre.fill((0,0,0))
                       fenetre.blit(text, (350, 290))
                       etat=1
                       g=650
                       g1=0
                       tab=[#colonne par colonne
                      [0,0,0,0,0,0],#col 0
                      [0,0,0,0,0,0],#col 1
                      [0,0,0,0,0,0],#col 2
                      [0,0,0,0,0,0],#col 3
                      [0,0,0,0,0,0],#col 4
                      [0,0,0,0,0,0],#col 5
                      [0,0,0,0,0,0]]#col 6
                       jouer={}
                    g1=g1+1
                    tour1=False
                    tour2=True
    if tour2==True :
        if etat==0:
            fonte = font.SysFont('comicsansms', 40)
            text = fonte.render('Joueur 2 joue !', True, (255, 255, 255), (0, 0, 0))
            fenetre.blit(text, (20, 20))
        if m<=position[0]<=m+100 and n<=position[1]<=n+106:
            m=position[0]-50
            n=position[1]-50
            if event.type == MOUSEBUTTONUP:
                if 40<m<100:
                    while n<a:
                        n=n+0.5
                        fenetre.blit(diablo2, (50,n))
                    if n==a:
                        jouer[(50,a)]='N'
                    m=850
                    n=200
                    a=a-105
                    
                    tab[0][a1]=2
                    if ifwin(0,a1,2):
                        fonte = font.SysFont('comicsansms', 40)
                        text = fonte.render('Joueur 2 a gagné !', True, (255, 255, 255), (0, 0, 0))
                        fenetre.fill((0,0,0))
                        fenetre.blit(text, (350, 290))
                        etat=1
                        a=650
                        a1=0
                        tab=[#colonne par colonne
                       [0,0,0,0,0,0],#col 0
                       [0,0,0,0,0,0],#col 1
                       [0,0,0,0,0,0],#col 2
                       [0,0,0,0,0,0],#col 3
                       [0,0,0,0,0,0],#col 4
                       [0,0,0,0,0,0],#col 5
                       [0,0,0,0,0,0]]#col 6
                        jouer={}
                    a1+=1
                    tour1=True
                    tour2=False
                if 140<m<200:
                    while n<b:
                        n=n+0.5
                        fenetre.blit(diablo2, (155,n))
                    if n==b:
                        jouer[(155,b)]='N'
                    m=850
                    n=200
                    b=b-105
                    
                    tab[1][b1]=2
                    if ifwin(1,b1,2):
                        fonte = font.SysFont('comicsansms', 40)
                        text = fonte.render('Joueur 2 a gagné !', True, (255, 255, 255), (0, 0, 0))
                        fenetre.fill((0,0,0))
                        fenetre.blit(text, (350, 290))
                        etat=1
                        b=650
                        b1=0
                        tab=[#colonne par colonne
                       [0,0,0,0,0,0],#col 0
                       [0,0,0,0,0,0],#col 1
                       [0,0,0,0,0,0],#col 2
                       [0,0,0,0,0,0],#col 3
                       [0,0,0,0,0,0],#col 4
                       [0,0,0,0,0,0],#col 5
                       [0,0,0,0,0,0]]#col 6
                        jouer={}
                    b1=b1+1
                    tour1=True
                    tour2=False
                if 240<m<300:
                    while n<c:
                        n=n+0.5
                        fenetre.blit(diablo2, (260,n))
                    if n==c:
                        jouer[(260,c)]='N'
                    m=850
                    n=200
                    c=c-105

                    tab[2][c1]=2
                    if ifwin(2,c1,2):
                        fonte = font.SysFont('comicsansms', 40)
                        text = fonte.render('Joueur 2 a gagné !', True, (255, 255, 255), (0, 0, 0))
                        fenetre.fill((0,0,0))
                        fenetre.blit(text, (350, 290))
                        etat=1 
                        c=650
                        c1=0
                        tab=[#colonne par colonne
                       [0,0,0,0,0,0],#col 0
                       [0,0,0,0,0,0],#col 1
                       [0,0,0,0,0,0],#col 2
                       [0,0,0,0,0,0],#col 3
                       [0,0,0,0,0,0],#col 4
                       [0,0,0,0,0,0],#col 5
                       [0,0,0,0,0,0]]#col 6
                        jouer={}
                    c1=c1+1
                    tour1=True
                    tour2=False
                if 340<m<400:
                    while n<d:
                        n=n+0.5
                        fenetre.blit(diablo2, (365,n))
                    if n==d:
                        jouer[(365,d)]='N'
                    m=850
                    n=200
                    d=d-105

                    tab[3][d1]=2
                    if ifwin(3,d1,2):
                        fonte = font.SysFont('comicsansms', 40)
                        text = fonte.render('Joueur 2 a gagné !', True, (255, 255, 255), (0, 0, 0))
                        fenetre.fill((0,0,0))
                        fenetre.blit(text, (350, 290))
                        etat=1
                        d=650
                        d1=0
                        tab=[#colonne par colonne
                       [0,0,0,0,0,0],#col 0
                       [0,0,0,0,0,0],#col 1
                       [0,0,0,0,0,0],#col 2
                       [0,0,0,0,0,0],#col 3
                       [0,0,0,0,0,0],#col 4
                       [0,0,0,0,0,0],#col 5
                       [0,0,0,0,0,0]]#col 6
                        jouer={}
                    d1=d1+1
                    tour1=True
                    tour2=False
                if 440<m<500:
                    while n<e:
                        n=n+0.5
                        fenetre.blit(diablo2, (470,n))
                    if n==e:
                        jouer[(470,e)]='N'
                    m=850
                    n=200
                    jouer[(470,e)]='N'
                    e=e-105

                    tab[4][e1]=2
                    if ifwin(4,e1,2):
                        fonte = font.SysFont('comicsansms', 40)
                        text = fonte.render('Joueur 2 a gagné !', True, (255, 255, 255), (0, 0, 0))
                        fenetre.fill((0,0,0))
                        fenetre.blit(text, (350, 290))
                        etat=1
                        e=650
                        e1=0
                        tab=[#colonne par colonne
                       [0,0,0,0,0,0],#col 0
                       [0,0,0,0,0,0],#col 1
                       [0,0,0,0,0,0],#col 2
                       [0,0,0,0,0,0],#col 3
                       [0,0,0,0,0,0],#col 4
                       [0,0,0,0,0,0],#col 5
                       [0,0,0,0,0,0]]#col 6
                        jouer={}
                    e1=e1+1
                    tour1=True
                    tour2=False
                if 540<m<600:
                    while n<f:
                        n=n+0.5
                        fenetre.blit(diablo2, (575,n))
                    if n==f:
                        jouer[(575,f)]='N'
                    m=850
                    n=200
                    f=f-105

                    tab[5][f1]=2
                    if ifwin(5,f1,2):
                        fonte = font.SysFont('comicsansms', 40)
                        text = fonte.render('Joueur 2 a gagné !', True, (255, 255, 255), (0, 0, 0))
                        fenetre.fill((0,0,0))
                        fenetre.blit(text, (350, 290))
                        etat=1
                        f=650
                        f1=0
                        tab=[#colonne par colonne
                       [0,0,0,0,0,0],#col 0
                       [0,0,0,0,0,0],#col 1
                       [0,0,0,0,0,0],#col 2
                       [0,0,0,0,0,0],#col 3
                       [0,0,0,0,0,0],#col 4
                       [0,0,0,0,0,0],#col 5
                       [0,0,0,0,0,0]]#col 6
                        jouer={}
                    f1=f1+1
                    tour1=True
                    tour2=False
                if 640<m<700:
                    while n<g:
                        n=n+0.5
                        fenetre.blit(diablo2, (680,n))
                    if n==g:
                        jouer[(680,g)]='N'
                    m=850
                    n=200
                    g=g-105

                    tab[6][g1]=2
                    if ifwin(6,g1,2):
                       fonte = font.SysFont('comicsansms', 40)
                       text = fonte.render('Joueur 2 a gagné !', True, (255, 255, 255), (0, 0, 0))
                       fenetre.fill((0,0,0))
                       fenetre.blit(text, (350, 290))
                       g=650
                       g1=0
                       tab=[
                      [0,0,0,0,0,0],#col 0
                      [0,0,0,0,0,0],#col 1
                      [0,0,0,0,0,0],#col 2
                      [0,0,0,0,0,0],#col 3
                      [0,0,0,0,0,0],#col 4
                      [0,0,0,0,0,0],#col 5
                      [0,0,0,0,0,0]]#col 6
                       jouer={}
                    g1=g1+1
                    tour1=True
                    tour2=False
    if etat==0:
        for cle in jouer:
            if jouer[cle]=='D':
                fenetre.blit(diablo, (cle))
            else :
                fenetre.blit(diablo2, (cle))
        
    for event in pygame.event.get() :
        if event.type==pygame.KEYDOWN :
            etat=0
            print('b')
            a=650
            b=650
            c=650
            d=650
            e=650
            f=650
            g=650
            a1=0
            b1=0
            c1=0
            d1=0
            e1=0
            f1=0
            g1=0
            tour1=True
            tour2=True
        if event.type == QUIT :
            continuer=False
    
    pygame.display.update()

pygame.quit()
