import pygame as pg
import random
import time
pg.init()
ekraani_laius = 500

ekraani_pikkus = 500

pg.display.set_caption("Menüü")
font = pg.font.Font('arial.ttf', 40)
#C:/Users/richard.sarap/mang_proge/arial.ttf
#VÄRVID

tekst_värv = (255, 255, 255)
def kirjuta(text, font, tekst_värv, x, y):
    pilt = font.render(text, True, tekst_värv)
    screen.blit(pilt, (x, y))


screen = pg.display.set_mode((ekraani_laius, ekraani_pikkus))

screen.fill((25, 26, 50))
gameplay = True
while gameplay:
    kirjuta("Start", font, tekst_värv, 200, 100)
    kirjuta("Press Space to continue", font, tekst_värv, 50, 200)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameplay = False
            break
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                kirjuta("Läks", font, tekst_värv, 200, 300)


    #pg.draw.circle(screen, (255, 0, 0), (250, 250), 50, 50)



    pg.display.update()
