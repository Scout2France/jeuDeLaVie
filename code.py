from tkinter import*                                                                    ## importation module tkinter
from math import*                                                                       ## importation modules mathematqies
from random import*                                                                     ## importation module aléatoire
fen = Tk()                                                                              ## creation de la fenetre tkinter
fen.title('fenetre')                                                                   ## on nomme la fenetre du nom de notre ami younousse qui ne fait plus nsi
n = 40                                                                               ## la taille du cadrillage 
l=600                                                                                   ## largeur de la fenetre
h = 600                                                                                 ## longueur de la fenetre
couleur = ["blue", "yellow", "black", "red", "purple", "pink"]                          ## mise en couleur des cases optionnel
epaisseurLigne = 2                                                                      ## épasseur des lignes du cadrillage
aire = Canvas(fen, width = l, height = h, bg="black")                                   ## création du canvas
aire.pack()
## création des coordoonees pour figure prédéfinit
planeur = [0, 1, 2, 2-n, 1-2*n]
canonAPlaneur = [0, 1, n, 1+n, 10, 10+n, 10+2*n, 11-n, 11+3*n, 12-2*n, 12+4*n, 13-2*n, 13+4*n, 14+n, 15-n, 15+3*n, 16, 16+n, 16+2*n, 17+n, 20, 20-n, 20-2*n, 21, 21-n, 21-2*n, 22-3*n, 22+n, 24-3*n, 24-4*n, 24+n, 24+2*n, 34-n, 34-2*n, 35-n, 35-2*n]
bombe = [0, 1, 2, -n, -2*n, 1-2*n, 2-n, 2-2*n, 4, 5 , 6, 4-n, 4-2*n, 5-2*n, 6-n, 6-2*n]
spacefiller = [0, 1, 2, 3, n, 4+n, 5+n, 7+n, 2*n, 6+2*n, 7+2*n, 1+3*n, 4+3*n, 5+3*n, 7+3*n, 7+4*n, 1+5*n, 4+5*n, 5+5*n, 7+5*n, 6*n, 6+6*n, 7+6*n, 7*n, 4+7*n, 5+7*n, 7+7*n, 8*n, 1+8*n, 2+8*n, 3+8*n, 1+11*n, 2+11*n, 2+12*n, 3+12*n, 4+12*n, 6+12*n, 3+13*n, 2+13*n, 7+13*n, 2+14*n, 3+14*n, 5+14*n, 7+14*n, 7+15*n, 5+15*n, 4+16*n, 5+16*n, 7+16*n, 7+17*n,  6+17*n, 7+18*n, 8+18*n, 9+18*n, 8+19*n, 9, 9+n, 10+n, 11, 11+n, 12-n, 10-2*n, 10-3*n, 11-4*n, 12-5*n, 13-5*n, 14-5*n, 14-4*n, 14-3*n, 15-2*n, 15-4*n, 16, 16-3*n, 16-4*n, 17-n, 17-2*n, 14+n, 13+n, 13+2*n, 13+3*n, 13+4*n, 13+5*n, 13+6*n, 13+7*n, 13+8*n, 13+9*n, 13+10*n, 13+11*n, 12+11*n, 9+4*n, 9+7*n, 9+8*n, 10+3*n, 10+5*n, 10+7*n, 10+9*n, 11+4*n, 11+6*n, 11+8*n, 11+9*n, 15+3*n, 15+4*n, 15+6*n, 15+8*n, 15+11*n, 15+12*n, 15+16*n, 16+15*n, 16+14*n, 16+11*n, 16+9*n, 16+7*n, 16+5*n, 16+3*n, 17+4*n, 17+5*n, 17+8*n, 17+11*n, 17+12*n, 14+13*n, 9+13*n, 9+14*n, 10+12*n, 10+15*n, 10+16*n, 11+16*n, 11+14*n, 12+15*n, 12+16*n, 12+17*n, 13+17*n, 14+17*n, 17-6*n, 18-6*n, 18-7*n, 19-6*n, 19-5*n, 19-4*n, 19-3*n, 19-2*n, 19-n, 20, 20-5*n, 21-2*n, 21-3*n, 21-4*n, 22, 22-4*n, 23, 23-n, 23-2*n, 24-2*n, 24-n, 24, 24+n, 25+n, 19+5*n, 19+6*n, 19+7*n, 19+8*n, 19+9*n, 19+10*n, 19+11*n, 20+6*n, 20+10*n, 21+11*n, 21+9*n, 21+7*n, 21+5*n, 22+5*n, 22+7*n, 22+9*n, 22+11*n, 23+4*n, 24+4*n, 25+4*n, 26+4*n, 26+5*n, 26+6*n, 25+7*n, 25+9*n, 26+10*n, 26+11*n, 26+12*n, 25+12*n, 24+12*n, 23+12*n]
puffer = [0, 3, 4+n, 4+2*n, 4+3*n, 3+3*n, 2+3*n, 1+3*n, 2*n, 17, 17+2*n, 18-n, 19-n, 20-n, 21, 21-n, 21+n, 20+2*n, 17-5*n, 18-6*n, 19-6*n, 19-7*n, 19-8*n, 18-9*n, 17-12*n, 17-14*n, 18-15*n, 19-15*n, 20-15*n, 20-12*n, 21-15*n, 21-14*n, 21-13*n, 9-13*n, 9-14*n, 10-14*n, 10-13*n, 10-12*n, 11-12*n, 11-13*n, 11-15*n, 12-15*n, 12-14*n, 12-13*n, 13-14*n]
tour = 0                                                                                ## initialisationdu nombre de mis a jour que fait le programme



def trouverCase(l, c):
    a = l*n+c
    return cadrillage[a]

class Case:

    def __init__(self, ligne, colonne, estVivante, vaMourir):                           ## initialisation dans la class de ligne, colonne, case vivante et case morte
        self.ligne = ligne
        self.colonne = colonne
        self.estVivante = estVivante
        self.vaMourir = vaMourir

    def tuer(self):                                                                     ## fonction pour tuer une cellule
        self.vaMourir = False

    def vivre(self):                                                                    ## fonction pour faire vivre une cellule
        self.vaMourir = True

    def testT(self):
        self.estVivante = True
        self.vaMourir = True

    def testF(self):
        self.estVivante = False
        self.vaMourir = False

    def compteVivants(self):
        compteur = 0
        for i in range(3):
            for a in range(3):
                if i != 1 or a != 1:
                    if self.ligne+a-1<0:
                        if self.colonne-1+i<0:
                            ui = trouverCase(n-1, n-1)
                        elif self.colonne-1+i > n-1:
                            ui = trouverCase(n-1, 0)
                        else:
                            ui = trouverCase(n-1, self.colonne+i-1)


                    elif self.ligne+ a-1>n-1:
                        if self.colonne-1+i<0:
                            ui = trouverCase(0, n-1)
                        elif self.colonne-1+i > n-1:
                            ui = trouverCase(0, 0)
                        else:
                            ui = trouverCase(0, self.colonne+i-1)


                    else:
                        if self.colonne-1+i<0:
                            ui = trouverCase(self.ligne+a-1, n-1)
                        elif self.colonne-1+i > n-1:
                            ui = trouverCase(self.ligne+a-1, 0)
                        else:
                            ui = trouverCase(self.ligne-1+a, self.colonne-1+i)
                    compteur += int(ui.estVivante)
        return compteur

cadrillage = []
for ligne in range(n):
    for colonne in range(n):
        cadrillage.append(Case(ligne, colonne, False, False))
lmodif = l+epaisseurLigne
hmodif = l+epaisseurLigne
aled = []
for a in range(n):
    for b in range(n):
        aled.append(aire.create_rectangle(b*(lmodif/n)+epaisseurLigne, a*(hmodif/n)+epaisseurLigne, (b+1)*(lmodif/n), (a+1)*(hmodif/n), outline="white", fill="white", tag=str(n*a+b)))




def voir():
    for a in cadrillage:
        print(a.ligne, a.colonne, a.estVivante)

def MaJ():                                                                              ## application des regles du jeu:
    global toto                                                                         ## on s'assure que la variable toto est utilisable dans la fonction
    global tour                                                                         ## on s'assure que la variable tour est utilisable dans la fonction
    global affichage_tour                                                               ## on s'assure que la variable affichage_tour est utilisable dans la fonction
    tour+=1                                                                             ## ajout d'un tour pour chaque mis a jour faite, tour etant initialisé a 0 au debut du programme
    affichage_tour = Label(fen, text=str(tour), font = ("Helvetica", 12)).place(x=l-40, y=h+10)  ## affichage du nombre de tour dans la fenetre de dessin, en dessous du cadrillage

    for a in range(len(cadrillage)):                                                    ##pour chaque cellle qui compose le cadrillage:
        nonobstant = cadrillage[a].compteVivants()
        if nonobstant<2 or nonobstant>3:                                                ## si une cellule a moins de 2 cellule vivante autour d'elle ou plus de 3 cellules vivante autour d'elle alors elle la cellule decede
            cadrillage[a].tuer()
        if nonobstant == 3:                                                             ## si une cellule A 3 cellule vivante autour d'elle alors elle deviendra vivante
            cadrillage[a].vivre()
    for a in range(len(cadrillage)):
        if cadrillage[a].vaMourir == True:
            aire.itemconfigure(aled[a], fill = "black", outline="black")
            sheesh = choice(couleur)
            aire.itemconfigure(aled[a], fill = sheesh, outline=sheesh)
            cadrillage[a].estVivante = cadrillage[a].vaMourir
        else:
            cadrillage[a].estVivante = cadrillage[a].vaMourir
            aire.itemconfigure(aled[a], fill = "white", outline="white")
    toto = aire.after(1, MaJ)

def click(event):
    x = event.x
    y = event.y
    b=aire.find_closest(x,y)
    b=aire.gettags(b)
    ui = 0
    for a in b:
        if a != 'current':
            ui += int(a)

    if cadrillage[ui].estVivante == False:
        aire.itemconfigure(aled[ui], fill = "black", outline="black")
        cadrillage[ui].testT()
    else:
        aire.itemconfigure(aled[ui], fill = "white", outline="white")
        cadrillage[ui].testF()


def Stop():                                                                             ## création d'une fonction stop qui met en pause le programme tel un menu pause
    aire.after_cancel(toto)

def getEntry():
    res = myEntry.get()
    print(res)

## mise en place de divers figures prédéfinit, a savoir les figures planneur, bombe, spacefiller, puffer, ainsi que canon a planneur
def Planneur():
    top= Toplevel(fen)
    top.geometry("250x250")
    top.title("UwU")
    Label(top, text= "Coordonées (X,Y)", font=('Arial 18 bold')).place(x=20,y=80)       ## demande a l'utilisateur les coordonnes de la figure prédéfinit

    def getEntry():
        res = myEntry.get()
        res=res.split(",")
        b = int(res[1])*n + int(res[0])
        for a in planeur:
            cadrillage[b+a].testT()
            aire.itemconfigure(aled[b+a], fill = "black", outline="black")
        top.destroy()
        return

    myEntry = Entry(top, width=40)
    myEntry.pack(pady=20)

    btn = Button(top, height=1, width=10, text="Envoyer", command=getEntry)
    btn.pack()


def Bombe():
    top= Toplevel(fen)
    top.geometry("250x250")
    top.title("UwU")
    Label(top, text= "Coordonées (X,Y)", font=('Arial 18 bold')).place(x=20,y=80)       ## demande a l'utilisateur les coordonnes de la figure prédéfinit

    def getEntry():
        res = myEntry.get()
        res=res.split(",")
        b = int(res[1])*n + int(res[0])
        for a in bombe:
            cadrillage[b+a].testT()
            aire.itemconfigure(aled[b+a], fill = "black", outline="black")
        top.destroy()
        return

    myEntry = Entry(top, width=40)
    myEntry.pack(pady=20)

    btn = Button(top, height=1, width=10, text="Envoyer", command=getEntry)
    btn.pack()

def Spacefiller():
    top= Toplevel(fen)
    top.geometry("250x250")
    top.title("UwU")
    Label(top, text= "Coordonées (X,Y)", font=('Arial 18 bold')).place(x=20,y=80)       ## demande a l'utilisateur les coordonnes de la figure prédéfinit

    def getEntry():
        res = myEntry.get()
        res=res.split(",")
        b = int(res[1])*n + int(res[0])
        for a in spacefiller:
            cadrillage[b+a].testT()
            aire.itemconfigure(aled[b+a], fill = "black", outline="black")
        top.destroy()
        return

    myEntry = Entry(top, width=40)
    myEntry.pack(pady=20)

    btn = Button(top, height=1, width=10, text="Envoyer", command=getEntry)
    btn.pack()

def Puffer():
    top= Toplevel(fen)
    top.geometry("250x250")
    top.title("UwU")
    Label(top, text= "Coordonées (X,Y)", font=('Arial 18 bold')).place(x=20,y=80)      ## demande a l'utilisateur les coordonnes de la figure prédéfinit

    def getEntry():
        res = myEntry.get()
        res=res.split(",")
        b = int(res[1])*n + int(res[0])
        for a in puffer:
            cadrillage[b+a].testT()
            aire.itemconfigure(aled[b+a], fill = "black", outline="black")
        top.destroy()
        return

    myEntry = Entry(top, width=40)
    myEntry.pack(pady=20)

    btn = Button(top, height=1, width=10, text="Envoyer", command=getEntry)
    btn.pack()
def CanonAPlanneur():
    top= Toplevel(fen)
    top.geometry("250x250")
    top.title("UwU")
    Label(top, text= "Coordonées (X,Y)", font=('Arial 18 bold')).place(x=20,y=80)       ## demande a l'utilisatuer les coordonnes de la figure prédéfinit

    def getEntry():
        res = myEntry.get()
        res=res.split(",")
        b = int(res[1])*n + int(res[0])
        for a in canonAPlaneur:
            cadrillage[b+a].testT()
            aire.itemconfigure(aled[b+a], fill = "black", outline="black")
        top.destroy()
        return

    myEntry = Entry(top, width=40)
    myEntry.pack(pady=20)

    btn = Button(top, height=1, width=10, text="Envoyer", command=getEntry)
    btn.pack()

aire.bind("<Button-1>", click)

Bouton = Button(fen, text ='Mise a Jour', command = MaJ)                                ## bouton qui correspond a la fonction maj et qui permet de commencer le jeu ou relancer le jeu apres un stop
Bouton.pack(side = LEFT, padx = 5, pady = 5)                                            ## position du bouton Mise a Jour

Bouton1 = Button(fen, text ='Stop', command = Stop)                                     ## bouton qui correspond a la fonction stop et qui permet de mettre le jeu sur pause
Bouton1.pack(side = LEFT, padx = 5, pady = 5)                                           ## position du bouton Stop

Bouton2 = Button(fen, text ='Planneur', command = Planneur)                             ## bouton qui met en place la figure prédéfinit Planneur a l'aide la fonction a l'aide de la fonction du meme nom
Bouton2.pack(side = LEFT, padx = 5, pady = 5)                                           ## position du bouton Planneur

Bouton3 = Button(fen, text ='Canon A Planneur', command = CanonAPlanneur)               ## bouton qui met en place la figure prédéfinit canon a Planneur a l'aide la fonction a l'aide de la fonction du meme nom
Bouton3.pack(side = LEFT, padx = 5, pady = 5)                                           ## position du bouton Canon a Planneur

Bouton4 = Button(fen, text ='Bombe', command = Bombe)                                   ## bouton qui met en place la figure prédéfinit Bombe a l'aide la fonction a l'aide de la fonction du meme nom
Bouton4.pack(side = LEFT, padx = 5, pady = 5)                                           ## position du bouton Bombe

Bouton4 = Button(fen, text ='Spacefiller', command = Spacefiller)                       ## bouton qui met en place la figure prédéfinit Spacefiller a l'aide la fonction a l'aide de la fonction du meme nom
Bouton4.pack(side = LEFT, padx = 5, pady = 5)                                           ## position du bouton Spacefiller

Bouton5 = Button(fen, text ='Puffer', command = Puffer)                                 ## bouton qui met en place la figure prédéfinit Puffer a l'aide la fonction a l'aide de la fonction du meme nom
Bouton5.pack(side = LEFT, padx = 5, pady = 5)                                           ## position du bouton Puffer

fen.mainloop()                                                                          ##fermetur de la fenetre
