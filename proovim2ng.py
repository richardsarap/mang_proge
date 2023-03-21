import pygame as pg
import random
import time
pg.init()
aeg = pg.time.Clock()


screen = pg.display.set_mode((800,400))

gameplay = True
while gameplay:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameplay = False
            break
    screen.fill((255,255,255))
    ringi_raadius = random.randint(30,100)
    X_voimalik_positsioon = 800-ringi_raadius            #X koordinaat kuhu ring saab tekkida arvestades tema raadiust
    Y_voimalik_positsioon = 400-ringi_raadius            #Y koordinaat kuhu ring saab tekkida arvestades tema raadiust
    X_positsioon = random.randint(ringi_raadius, X_voimalik_positsioon)     #suvaline X koordinaat kuhu ringi X tekib
    Y_positsioon = random.randint(ringi_raadius, Y_voimalik_positsioon)

    for i in range(4):
        pg.draw.circle(screen, 'red', (X_positsioon, Y_positsioon), 10, ringi_raadius)
        pg.time.wait(1000)
        pg.draw.circle(screen, 'white', (X_positsioon, Y_positsioon), 10, ringi_raadius)
    if event.type == pg.MOUSEBUTTONDOWN:
        if pg.mouse.get_pos() ==


    pg.display.update()