import pygame, sys, random

pygame.init()
laius, kõrgus = 800, 800
screen = pygame.display.set_mode((laius, kõrgus))

#font
font = pygame.font.SysFont("arialblack", 40)

#värvid
TEXT_COL = (255, 255, 255)


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))



tee_ruut = False
peida_ruut = False
jooned = False


kõik_ruudud =[] #  salvestada koordinaadid ja teada, mitme ruudu koordinaadid seal on
õiged = 0#  vaja, et peale ühte "levelit" saaks aru, et on vaja teha juurde üks ruut
vajutused = 0#  loeb mitu korda on vajutatud ühes levelis ja vaatab, kas vajutatakse õiges järjeskorras
i = 0# vaja põhimõtteliselt selleks, et aru saada, kas on veel vaja ruute kuvada või mitte

screen.fill((71, 30, 255))
algus_tekst = draw_text("Space, et alusatada", font, TEXT_COL, 60, 250)

algus_tekst = True
elud = 3
mäng = True
while mäng == True:


    pygame.time.Clock().tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:#  toimub vajutus
            if vajutused+1 < len(kõik_ruudud):
                x, y = event.pos
                if kõik_ruudud[vajutused][0] < x < kõik_ruudud[vajutused][0] + laius//5 and kõik_ruudud[vajutused][1] < y < kõik_ruudud[vajutused][1] + kõrgus//5:#   kontrollib, kas õigesse kohta vajutati
                   vajutused += 1
                else:
                    elud -= 1
                    print("elud: " + str(elud))
                    if elud == 0:
                        mäng = False
                        print("kaotasid")
                    elif elud == 1:
                        print("Ära nüüd mööda vajuta!")


            elif vajutused+1 == len(kõik_ruudud):
                x, y = event.pos
                if kõik_ruudud[vajutused][0] < x < kõik_ruudud[vajutused][0] + laius//5 and kõik_ruudud[vajutused][1] < y < kõik_ruudud[vajutused][1] + kõrgus//5:
                    print("Läbisid taseme " + str(len(kõik_ruudud)))
                    õiged += 1
                    tee_ruut = True
                    vajutused = 0
                else:
                    elud -= 1
                    print("elud: " + str(elud))

                    if elud == 0:
                        mäng = False
                        print("kaotasid")
                    elif elud == 1:
                        print("Ära nüüd mööda vajuta!")



        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill((71, 30, 255))
                algus_tekst = False
                tee_ruut = True
                for u in range(5):
                    pygame.draw.line(screen, (255, 255, 255), (laius // 5 * u, 0),
                                     (laius // 5 * u, kõrgus))  # horisontaalsed jooned
                    pygame.draw.line(screen, (255, 255, 255), (0, kõrgus // 5 * u),
                                     (laius, kõrgus // 5 * u))  # vertikaalsed jooned



    if peida_ruut:#   Peidab ruudu
        pygame.draw.rect(screen, (71, 30, 255), ((kõik_ruudud[i][0] + 2, kõik_ruudud[i][1] + 2), (laius // 5 - 2, kõrgus // 5 - 2)))#   all tehtud punase ruudu peale joonistatakse must ruut ja tahetakse vajutust
        if i+1 < len(kõik_ruudud):
            i += 1
            tee_ruut = True
        else:
            i = 0
        peida_ruut = False



    if tee_ruut:#   Teeb ruudu
        if len(kõik_ruudud) <= õiged:
            rx, ry = random.randint(0, 4) * laius // 5, random.randint(0, 4) * kõrgus // 5#   esimene kord teeb ruudu ja ülejäänud korrad teeb lisaks vanadele uue ruudu
            kõik_ruudud.append([rx, ry])
        else:
            pygame.draw.rect(screen, (255, 0, 0), ((kõik_ruudud[i][0] + 2, kõik_ruudud[i][1] + 2), (laius // 5 - 2, kõrgus // 5 - 2)))#   kui uus ruut on tehtud on len(kõik_ruudud) suurem kui õiged ja saab joonistama hakata
            tee_ruut = False
            peida_ruut = True

    pygame.display.update()