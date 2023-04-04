"""import pygame as pg
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

taust = pg.Surface((ekraani_laius, ekraani_pikkus))

screen.fill((25, 26, 50))

gameplay = True

while gameplay:
    kirjuta("Mängu algus!", font, tekst_värv, 135, 100)
    kirjuta("Press Space to continue", font, tekst_värv, 50, 400)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameplay = False
            break
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print("läks!")




    pg.display.update()"""
"""
import pygame as pg
import random
import time
pg.init()
aeg = pg.time.Clock()

screen = pg.display.set_mode((800,400))

gameplay = True
algus = True

koordid = []
skoor = 0

ringi_raadius = random.randint(30,100)
X_voimalik_positsioon = 800-ringi_raadius #X koordinaat kuhu ring saab tekkida arvestades tema raadiust
Y_voimalik_positsioon = 400-ringi_raadius
X_positsioon = random.randint(ringi_raadius, X_voimalik_positsioon) # suvaline X koordinaat kuhu ringi X tekib
Y_positsioon = random.randint(ringi_raadius, Y_voimalik_positsioon)

def ring():
    pg.draw.circle(screen, (255, 0, 0), (X_positsioon, Y_positsioon), ringi_raadius, ringi_raadius)

while gameplay:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameplay = False
            break
        ring()
        if event.type == pg.MOUSEBUTTONDOWN:
            hiirePositsioon = pg.mouse.get_pos() # vaatab kas positsioon on sama mis ringidel oli
            # (x,y)
            X_positsioon = random.randint(ringi_raadius,X_voimalik_positsioon) # suvaline X koordinaat kuhu ringi X tekib
            Y_positsioon = random.randint(ringi_raadius, Y_voimalik_positsioon)
            väiksemX = X_positsioon + 2 * ringi_raadius

            if hiirePositsioon[0] >= X_positsioon and hiirePositsioon[0] <= väiksemX:
                väiksemY = Y_positsioon + 2 * ringi_raadius
                if hiirePositsioon[1] >= Y_positsioon and hiirePositsioon[1] <= väiksemY:
                        skoor += 1
                        print(skoor)
                        algus = True

    screen.fill((255, 255, 255))
    pg.draw.circle(screen, (255, 0, 0), (X_positsioon, Y_positsioon), ringi_raadius, ringi_raadius)
    ring()
    pg.display.update()"""
