
import pygame
import sys,os
import numpy as np
from pygame import mixer


mixer.init()



mixer.music.load(os.path.join('New folder','dumro.mp3'))
# Setting the volume
mixer.music.set_volume(0.7)

pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Dusmanin")
font = pygame.font.SysFont('Consolas', 30)
count=0
taraba=pygame.image.load(os.path.join('New folder','3x3-grid-png-6.png'))
iks=pygame.image.load(os.path.join('New folder','iks.png'))
oks=pygame.image.load(os.path.join('New folder','oks.png'))
pob=pygame.image.load(os.path.join('New folder','thumb.jpg'))
gib=pygame.image.load(os.path.join('New folder','Gibanica.jpg'))
guzvara=pygame.image.load(os.path.join('New folder','гужвара.png'))
class Tabla:
    def __init__(self):
        self.matrica=np.zeros((3 ,3 ))

    def mark_matrica(self, red , kol ,igrac):
        self.matrica[red][kol]= igrac
    def prazno(self,red,kol):
        return self.matrica[red][kol]==0



class Igra:
    def __init__(self):
        self.igrac =1
        self.board=Tabla()
        self.crto()
        self.igra=True
    def crto(self):
        screen.blit(taraba,(0,0))
        screen.blit(gib, (20, 550))
        pygame.display.update()
    def promena(self):
        self.igrac=self.igrac+1
    def crtajx(self,red,kol):
        centar=(red*200+5)
        centary=(kol*200+5)
        screen.blit(iks, (centary, centar))
    def crtajo(self,i,n):
        centar=(i*200+5)
        centary=(n*200+5)
        screen.blit(oks, (centary, centar))
    def pobeda(self):
        screen.blit(pob, (100, 150))
    def poraz(self):

        self.igra=False
    def clear(self):
        b=1
        pim=""
        with open("pismo.txt", "r+") as pismo:
            pos=str(pismo.readlines())
            for t in range(0, 3):
                for h in range(0, 3):
                    pim=pim+str(self.board.matrica[t][h])

            if pim in pos:
                b=-1

            if b==1:
                for t in range(0, 3):
                     for h in range(0, 3):
                        pismo.write(str(self.board.matrica[t][h]))
                pismo.write("\n")

        for t in range(0,3):
            for h in range(0, 3):
                self.board.matrica[t][h]=0

    def skor(self):
        with open("pismo.txt", "r") as fp:
                x = len(fp.readlines())
                return x
    def clear1(self):
        for t in range(0,3):
            for h in range(0, 3):
                self.board.matrica[t][h]=0


def main():

    game=Igra()
    board=game.board
    run = True
    igrac=game.igrac
    matrica=game.board.matrica
    k=0
    red=0
    kol=0
    igra=game.igra
    tablica=Tabla()
    skor=str(game.skor())



    while run:
        skor = str(game.skor())
        font = pygame.font.SysFont('Consolas', 30)
        screen.blit(gib, (20, 550))
        screen.blit(font.render("x"+skor.rjust(2), True, (0, 0, 0)), (120, 560))




        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()

            if game.igra==False:
                mixer.music.play(0)
                game.crto()
                game.clear()
                game.igra = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=event.pos
                red=pos[1]//200
                kol=pos[0]//200


                if board.prazno(red,kol)==True:
                    game.board.mark_matrica(red,kol,igrac)
                    game.crtajx(red,kol)
                    game.promena()
                    k = 0
                    #sporedna dijagonala -2
                    if k == 0:
                        if matrica[0][2]+matrica[1][1]+matrica[2][0]==3:
                            game.poraz()
                            k=1


                    # glavna dijagonala -2
                    if k == 0:
                        if matrica[0][0] + matrica[1][1] + matrica[2][2] == 3:
                            game.poraz()
                            k = 1

                    #redovi -2
                    if k==0:
                        for i in range(0,3):
                                if matrica[i][0]+matrica[i][1]+matrica[i][2]==3:
                                    game.poraz(skor,igra)
                                    k = 1


                    #kolone 2
                    if k==0:
                        for n in range(0,3):
                                if matrica[0][n]+matrica[1][n]+matrica[2][n]==3:
                                    game.poraz()
                                    k = 1


                    #sporedna dijagonala -2
                    if k == 0:
                        if matrica[0][2]+matrica[1][1]+matrica[2][0]==-2:
                            if matrica[1][1]==0:
                                matrica[1][1]=-1
                                game.crtajo(1, 1)
                                k = 1
                                game.pobeda()
                            elif matrica[0][2]==0:
                                matrica[0][2]=-1
                                game.crtajo(0, 2)
                                k = 1
                                game.pobeda()
                            elif matrica[2][0]==0:
                                matrica[2][0]=-1
                                game.crtajo(2, 0)
                                k = 1
                                game.pobeda()

                    # glavna dijagonala -2
                    if k == 0:
                        if matrica[0][0] + matrica[1][1] + matrica[2][2] == -2:
                            if matrica[1][1] == 0:
                                matrica[1][1] = -1
                                game.crtajo(1, 1)
                                k = 1
                                game.pobeda()
                            elif matrica[0][0]==0:
                                matrica[0][0]=-1
                                game.crtajo(0, 0)
                                k = 1
                                game.pobeda()

                            elif matrica[2][2]==0:
                                matrica[2][2]=-1
                                game.crtajo(2, 2)
                                k = 1
                                game.pobeda()
                    #redovi -2
                    if k==0:
                        for i in range(0,3):
                                if matrica[i][0]+matrica[i][1]+matrica[i][2]==-2:
                                    n=i
                                    for i in range(0, 3):
                                        if matrica[n][i]==0:
                                            matrica[n][i]=-1
                                            k=1
                                            game.crtajo(n,i)
                                            game.pobeda()


                    #kolone -2
                    if k==0:
                        for n in range(0,3):
                                if matrica[0][n]+matrica[1][n]+matrica[2][n]==-2:
                                    i=n
                                    for n in range(0, 3):
                                        if matrica[n][i]==0:
                                            matrica[n][i]=-1
                                            k=1
                                            game.crtajo(n,i)
                                            game.pobeda()

                    #glavna dijagonala 2

                    if k == 0:
                        if matrica[0][0]+matrica[1][1]+matrica[2][2]==2:
                            if matrica[1][1] == 0:
                                matrica[1][1] = -1
                                game.crtajo(1, 1)
                                k = 1
                            elif matrica[0][0]==0:
                                matrica[0][0]=-1
                                k = 1
                                game.crtajo(0, 0)

                            elif matrica[2][2]==0:
                                matrica[2][2]=-1
                                k = 1
                                game.crtajo(2, 2)

                    # sporedna dijagonala 2
                    if k == 0:
                        if matrica[0][2]+matrica[1][1]+matrica[2][0]==2:
                            if matrica[1][1]==0:
                                matrica[1][1]=-1
                                game.crtajo(1, 1)
                                k = 1
                            elif matrica[0][2]==0:
                                matrica[0][2]=-1
                                game.crtajo(0, 2)
                                k = 1
                            elif matrica[2][0]==0:
                                matrica[2][0]=-1
                                game.crtajo(2, 0)
                                k = 1
                            else:
                                pass
                    # redovi 2
                    if k==0:
                        for i in range(0,3):
                            if matrica[i][0]+matrica[i][1]+matrica[i][2]==2:
                                    n=i
                                    for i in range(0, 3):
                                        if matrica[n][i]==0:
                                            matrica[n][i]=-1
                                            k=1
                                            game.crtajo(n,i)





                    # kolone 2
                    if k==0:
                        for n in range(0,3):
                            if matrica[0][n]+matrica[1][n]+matrica[2][n]==2:
                                    i=n
                                    for n in range(0, 3):
                                        if matrica[n][i]==0:
                                            matrica[n][i]=-1
                                            k=1
                                            game.crtajo(n,i)


                    if k == 0:
                        if matrica[0][2]+matrica[1][1]+matrica[2][0]==1:
                            if matrica[1][1]==0:
                                matrica[1][1]=-1
                                game.crtajo(1, 1)
                                k = 1
                            elif matrica[0][2]==0:
                                matrica[0][2]=-1
                                game.crtajo(0, 2)
                                k = 1
                            elif matrica[2][0]==0:
                                matrica[2][0]=-1
                                game.crtajo(2, 0)
                                k = 1



                    if k == 0:
                        if matrica[0][0] + matrica[1][1] + matrica[2][2] == 1:
                            if matrica[1][1] == 0:
                                matrica[1][1] = -1
                                game.crtajo(1, 1)
                                k = 1
                            elif matrica[0][0]==0:
                                matrica[0][0]=-1
                                game.crtajo(0, 0)
                                k = 1

                            elif matrica[2][2]==0:
                                matrica[2][2]=-1
                                game.crtajo(2, 2)
                                k = 1


                    if k==0:
                        for n in range(0,3):
                            if matrica[0][n]+matrica[1][n]+matrica[2][n]==1:
                                i=n
                                for n in range(0, 3):
                                    if matrica[n][i]==0:
                                        k = 1
                                        matrica[n][i]=-1
                                        game.crtajo(n,i)
                                    break


                    if k==0:
                        for n in range(0,3):
                            if matrica[n][0]+matrica[n][1]+matrica[n][2]==1:
                                    i=n
                                    for n in range(0, 3):
                                        if matrica[i][n]==0:
                                            matrica[i][n]=-1
                                            k = 1
                                            game.crtajo(i,n)
                                        break



                    if matrica[0][0]!=0 and matrica[0][1]!=0 and matrica[0][2]!=0:
                        if  matrica[1][0]!=0 and matrica[1][1]!=0 and matrica[1][2]!=0:
                            if  matrica[2][0]!=0 and matrica[2][1]!=0 and matrica[2][2]!=0:
                                game.crto()
                                game.clear1()



        pygame.display.update()

main()

