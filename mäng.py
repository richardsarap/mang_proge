import pygame, sys, random

pygame.init()
laius, kõrgus = 800, 800
screen = pygame.display.set_mode((laius, kõrgus))

#font
font = pygame.font.SysFont("arialblack", 40)

#värvid
teksti_värv = (255, 255, 255)


def kirjuta(text, font, teksti_värv, x, y):
  asi = font.render(text, True, teksti_värv)
  screen.blit(asi, (x, y))

algus_tekst = True
elud = 3


tee_ruut = False
peida_ruut = False



kõik_ruudud =[] #  salvestada koordinaadid ja teada, mitme ruudu koordinaadid seal on
õiged = 0#  vaja, et peale ühte "levelit" saaks aru, et on vaja teha juurde üks ruut
vajutused = 0#  loeb mitu korda on vajutatud ühes levelis ja vaatab, kas vajutatakse õiges järjeskorras
i = 0# vaja põhimõtteliselt selleks, et aru saada, kas on veel vaja ruute kuvada või mitte

screen.fill((71, 30, 255))
algus_tekst = kirjuta("Space, et alusatada", font, teksti_värv, laius // 4.5, kõrgus // 2)# peaks toimima



mäng = True
while mäng == True:

    font = pygame.font.SysFont('arialblack', 20)

    pygame.time.Clock().tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:#  toimub vajutus
            if vajutused+1 < len(kõik_ruudud):

                x, y = event.pos
                if kõik_ruudud[vajutused][0] < x < kõik_ruudud[vajutused][0] + laius//5 and kõik_ruudud[vajutused][1] < y < kõik_ruudud[vajutused][1] + kõrgus//5:#   kontrollib, kas õigesse kohta vajutati
                    pygame.draw.rect(screen, (0, 0, 255), ((kõik_ruudud[vajutused][0] + 2, kõik_ruudud[vajutused][1] + 2), (laius // 5 - 2, kõrgus // 5 - 2)))
                    vajutused += 1
                else:
                    elud -= 1
                    text = font.render("elud: " + str(elud), True, teksti_värv, (71, 30, 255))
                    textRect = text.get_rect()
                    screen.blit(text, (10, 50))
                    if elud == 0:
                        mäng = False
                    elif elud == 1:
                        print("Ära nüüd mööda vajuta!")


            elif vajutused+1 == len(kõik_ruudud):
                pygame.time.Clock().tick(1)
                x, y = event.pos
                if kõik_ruudud[vajutused][0] < x < kõik_ruudud[vajutused][0] + laius//5 and kõik_ruudud[vajutused][1] < y < kõik_ruudud[vajutused][1] + kõrgus//5:
                    pygame.draw.rect(screen, (0, 0, 255), ((kõik_ruudud[vajutused][0] + 2, kõik_ruudud[vajutused][1] + 2), (laius // 5 - 2, kõrgus // 5 - 2)))
                    õiged += 1
                    text = font.render("Õigeid:" + str(õiged), True, teksti_värv, (71, 30, 255))
                    textRect = text.get_rect()
                    screen.blit(text, (10, 110))
                    tee_ruut = True
                    vajutused = 0
                else:
                    elud -= 1
                    text = font.render("elud:" + str(elud), True, teksti_värv, (71, 30, 255))
                    textRect = text.get_rect()
                    screen.blit(text, (10, 50))

                    if elud == 0:
                        mäng = False
                    elif elud == 1:
                        print("Ära nüüd mööda vajuta!")



        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill((71, 30, 255))
                algus_tekst = False
                tee_ruut = True

                text = font.render("Õigeid:" + str(õiged), True, teksti_värv, (71, 30, 255))
                textRect = text.get_rect()
                screen.blit(text, (10, 110))

                text = font.render("elud:" + str(elud), True, teksti_värv, (71, 30, 255))
                textRect = text.get_rect()
                screen.blit(text, (10, 50))
                for u in range(5):
                    pygame.draw.line(screen, (255, 255, 255), (laius // 5 * u, 0),
                                     (laius // 5 * u, kõrgus))  # vertikaalsed jooned
                    pygame.draw.line(screen, (255, 255, 255), (0, kõrgus // 5 * u),
                                     (laius, kõrgus // 5 * u))  # horisontaalsed jooned



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
            rx, ry = random.randint(0, 4) * laius // 5, random.randint(0, 4) * kõrgus // 5
            if rx == 0 and ry == 0:
                rx, ry = random.randint(0, 4) * laius // 5, random.randint(0, 4) * kõrgus // 5
                kõik_ruudud.append([rx, ry])
            else:
                kõik_ruudud.append([rx, ry])
        else:
            pygame.draw.rect(screen, (255, 0, 0), ((kõik_ruudud[i][0] + 2, kõik_ruudud[i][1] + 2), (laius // 5 - 2, kõrgus // 5 - 2)))#   kui uus ruut on tehtud on len(kõik_ruudud) suurem kui õiged ja saab joonistama hakata
            tee_ruut = False
            peida_ruut = True

    pygame.display.update()