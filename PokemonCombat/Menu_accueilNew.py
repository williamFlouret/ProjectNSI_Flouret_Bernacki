import pygame, sys


pygame.init()           #on importe tous les modules nécessaires
clock = pygame.time.Clock()
import pygame.mixer
import pygame.mixer_music
pygame.mixer.init()
#screen width and height
screenwidth = 1200  #Choose your screen size
screenheight = int((625/1000)*screenwidth)





#create screen
screen = pygame.display.set_mode((screenwidth, screenheight))


#basic colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

policearial = pygame.font.Font("Pokemon.ttf", 15)       #importation de la police d'ecriture pokemon
Xpika= (-15/100)*screenwidth


class POKEMON2(pygame.sprite.Sprite):           #classe qui gère l'animation du gros logo pokemon
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []



        num3 = 1
        for i in range (1, 20):         #grace a une boucle on appelle chaque image de l'animation dans une liste, dans l'update de la classe qui va constamment s'actualiser tant que la classe est active on va alors afficher ces images une par une à la suite, donnant un effet d'animation fluide
            num3 += 1

            name3 = str('POKEMON2-' + str(num3) + '.png')

            frame3 = pygame.image.load(name3)
            frame3 = pygame.transform.scale(frame3, (int((70/100)*screenwidth), int((50/100)*screenheight)))

            self.sprites.append(frame3)


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = ((50/100)*screenwidth, (14/100)*screenheight)

    def update(self):
        self.current_sprite += 0.2

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

class POKEMONP(pygame.sprite.Sprite):       #classe qui gere l'animation du petit pikachu qui traverse l'ecran
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []



        num10 = 0
        for i in range (1, 5):      #grace a une boucle on appelle chaque image de l'animation dans une liste, dans l'update de la classe qui va constamment s'actualiser tant que la classe est active on va alors afficher ces images une par une à la suite, donnant un effet d'animation fluide
            num10 += 1

            name10 = str('pi-' + str(num10) + '.png')

            frame10 = pygame.image.load(name10)
            frame10 = pygame.transform.scale(frame10, (int((7/100)*screenwidth), int((7/100)*screenheight)))

            self.sprites.append(frame10)


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = (Xpika, (74/100)*screenheight)

    def update(self):
        self.current_sprite += 0.5


        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        global Xpika
        Xpika +=7           #on augmente à chaque update son abscisse, le pikachu avance donc vers la droite
        self.rect.center = (Xpika, (74/100)*screenheight)

        if Xpika>=1370:     #lorsque l'abscisse du pika depasse celle du screen, il revient à la gauche de l'ecran, donnant l'impression qu'il cours à l'infini
            Xpika-=1385
            self.rect.center = (Xpika, (74/100)*screenheight)

        self.image = self.sprites[int(self.current_sprite)]










all_sprites3 = pygame.sprite.Group()        #on aujoute les classes dans des groupes pour pouvoir les appeler quand nécessaire
all_spritesP = pygame.sprite.Group()
pokemonp=POKEMONP()
Pokemon2 = POKEMON2()
all_sprites3.add(Pokemon2)
all_spritesP.add(pokemonp)


button1Img = pygame.image.load('Jouer.png')             #ici on va importer toutes les images statiques qu'on veut afficher
button1Img = pygame.transform.scale(button1Img, (int((15/100)*screenwidth), int((9.5/100)*screenheight)))
button1X = (41.5/100)*screenwidth
button1Y = (85/100)*screenheight


Titre = pygame.image.load('Genesis.png')
Titre = pygame.transform.scale(Titre, (int((60/100)*screenwidth), int((65/100)*screenheight)))
TitreX = (19.5/100)*screenwidth
TitreY = (20/100)*screenheight



button1v2Img = pygame.image.load('Jouer2.png')
button1v2Img = pygame.transform.scale(button1v2Img, (int((15/100)*screenwidth), int((9.5/100)*screenheight)))
button1v2X = (41.5/100)*screenwidth
button1v2Y = (85/100)*screenheight

background1Img = pygame.image.load('ImageMenuTitre.png')
background1Img = pygame.transform.scale(background1Img, (screenwidth, screenheight))
background1X = 0
background1Y = 0



widthB = int((15/100)*screenwidth)
heightB = int((9.5/100)*screenheight)
click1=0

textcredits = policearial.render("Réalisé par Luc Bernacki et William Flouret",1,black)


pygame.mixer_music.load("PokemonTitleTrue.wav")         #importation de la musique
pygame.mixer.music.play(loops=-1, fade_ms=2)


def button1():          #les fonction qui servent à afficher à l'ecran les images importées
    screen.blit(button1Img, (button1X, button1Y))

def button1v2():
    screen.blit(button1v2Img, (button1v2X, button1v2Y))

def background1():
    screen.blit(background1Img, (background1X, background1Y))

def credits():
    screen.blit(textcredits, (int((2/100)*screenwidth), int((95/100)*screenheight)))

def title():
    screen.blit(Titre, (TitreX, TitreY))

gameopen=pygame.mixer.Sound('opengame.wav')
TranSition=False
running = True
while running:      #boucle principale



    background1()
    button1()
    all_sprites3.update()   #on appelle les fonctions images et les classes
    all_sprites3.draw(screen)
    all_spritesP.update()
    all_spritesP.draw(screen)
    credits()
    title()



    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:       #la boucle s'arrete lorsque on quitte la page avec le bouton even QUIT (croix rouge)
            pygame.quit()
            sys.exit()


        if button1X <= mouse[0] <= button1X+widthB and button1Y <= mouse[1] <= button1Y+heightB:    #verifie à chaque event si on clique sur le bouton jouer
            if click[0] == 1:
                TranSition=True
                gameopen.play()


        if TranSition==True:                #si on a cliqué, le programme va lancer Poke_true_version.py, le jeu en lui meme
            import Poke_true_version.py
            all_spritesT.update()
            all_spritesT.draw(screen)







    if button1X <= mouse[0] <= button1X+widthB and button1Y <= mouse[1] <= button1Y+heightB:    #change la couleur du bouton jouer quand on passe dessus
        button1v2()


    pygame.display.update()   #cloture toute boucle principale de programme pygame, s'assure de refresh l'ecran à une vitesse (ici 20 tick)
    clock.tick(20)