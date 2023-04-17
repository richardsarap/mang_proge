import pygame, sys, random

pygame.init()
laius, kõrgus = 400, 400
screen = pygame.display.set_mode((laius, kõrgus))

for i in range(5):
    pygame.draw.line(screen, (255, 255, 255), (laius // 5 * i, 0), (laius // 5 * i, kõrgus)) #horisontaalsed jooned
    pygame.draw.line(screen, (255, 255, 255), (0, kõrgus // 5 * i), (laius, kõrgus // 5 * i)) # vertikaalsed jooned


tee_ruut = True
peida_ruut = False
kõik_ruudud =[] #  salvestada koordinaadid ja teada, mitme ruudu koordinaadid seal on
õiged = 0#  vaja, et peale ühte "levelit" saaks aru, et on vaja teha juurde üks ruut
vajutused = 0#  loeb mitu korda on vajutatud ühes levelis ja vaatab, kas vajutatakse õiges järjeskorras

i = 0#  vaja põhimõtteliselt selleks, et aru saada, kas on veel vaja ruute kuvada või mitte
while True:
    pygame.time.Clock().tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:#  toimub vajutus
            if vajutused+1 < len(kõik_ruudud):
                x, y = event.pos
                if kõik_ruudud[vajutused][0] < x < kõik_ruudud[vajutused][0] + laius//5 and kõik_ruudud[vajutused][1] < y < kõik_ruudud[vajutused][1] + kõrgus//5:#   kontrollib, kas õigesse kohta vajutati
                   vajutused += 1

            elif vajutused+1 == len(kõik_ruudud):
                x, y = event.pos
                if kõik_ruudud[vajutused][0] < x < kõik_ruudud[vajutused][0] + laius//5 and kõik_ruudud[vajutused][1] < y < kõik_ruudud[vajutused][1] + kõrgus//5:
                    print("Läbisid taseme " + str(len(kõik_ruudud)))
                    õiged += 1
                    tee_ruut = True
                    vajutused = 0


    if peida_ruut:#   Peidab ruudu
        pygame.draw.rect(screen, (0, 0, 0), ((kõik_ruudud[i][0] + 2, kõik_ruudud[i][1] + 2), (laius // 5 - 2, kõrgus // 5 - 2)))#   all tehtud punase ruudu peale joonistatakse must ruut ja tahetakse vajutust
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