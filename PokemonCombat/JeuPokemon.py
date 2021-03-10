import pygame, sys


pygame.init()
clock = pygame.time.Clock()
import pygame.mixer
import pygame.mixer_music
pygame.mixer.init()
#screen width and height
screenwidth = 1200  #Choose your screen size
screenheight = int((610/1000)*screenwidth)





#create screen
screen = pygame.display.set_mode((screenwidth, screenheight))



#title and icon
pygame.display.set_caption("Bourg Courmomble")
icon = pygame.image.load('Pokeball.png')
pygame.display.set_icon(icon)


#basic colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

XNat=450
YNat=700


class NATHANOVERH(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []



        num26 = 0
        for i in range (1, 5):
            num26 += 1

            name26 = str('HerosOverworldHaut-' + str(num26) + '.png')

            frame26 = pygame.image.load(name26)
            frame26 = pygame.transform.scale(frame26, (int((3/100)*screenwidth), int((6/100)*screenheight)))

            self.sprites.append(frame26)


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = (XNat,YNat)
        



    def update(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        global XNat
        global YNat
       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            YNat-=6
            self.rect.center = (XNat, YNat)
           

        self.image = self.sprites[int(self.current_sprite)]


class NATHANOVERB(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []



        num27 = 0
        for i in range (1, 5):
            num27 += 1

            name27 = str('HerosOverworldBas-' + str(num27) + '.png')

            frame27 = pygame.image.load(name27)
            frame27 = pygame.transform.scale(frame27, (int((3/100)*screenwidth), int((6/100)*screenheight)))

            self.sprites.append(frame27)


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = (XNat,YNat)

    def update(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        global XNat
        global YNat
       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            YNat+=6
            self.rect.center = (XNat, YNat)


        self.image = self.sprites[int(self.current_sprite)]

class NATHANOVERD(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []



        num28 = 0
        for i in range (1, 5):
            num28 += 1

            name28 = str('HerosOverworldDroite-' + str(num28) + '.png')

            frame28 = pygame.image.load(name28)
            frame28 = pygame.transform.scale(frame28, (int((3/100)*screenwidth), int((6/100)*screenheight)))

            self.sprites.append(frame28)


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = (XNat,YNat)

    def update(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        global XNat
        global YNat
       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            XNat+=6
            self.rect.center = (XNat, YNat)


        self.image = self.sprites[int(self.current_sprite)]

class NATHANOVERG(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []



        num29 = 0
        for i in range (1, 5):
            num29 += 1

            name29 = str('HerosOverworldGauche-' + str(num29) + '.png')

            frame29 = pygame.image.load(name29)
            frame29 = pygame.transform.scale(frame29, (int((3/100)*screenwidth), int((6/100)*screenheight)))

            self.sprites.append(frame29)


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = (XNat,YNat)

    def update(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        global XNat
        global YNat
       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            XNat-=6
            self.rect.center = (XNat, YNat)


        self.image = self.sprites[int(self.current_sprite)]

all_spritesNOH = pygame.sprite.Group()
Nathanoverh=NATHANOVERH()
all_spritesNOH.add(Nathanoverh)
all_spritesNOB = pygame.sprite.Group()
Nathanoverb=NATHANOVERB()
all_spritesNOB.add(Nathanoverb)
all_spritesNOD = pygame.sprite.Group()
Nathanoverd=NATHANOVERD()
all_spritesNOD.add(Nathanoverd)
all_spritesNOG = pygame.sprite.Group()
Nathanoverg=NATHANOVERG()
all_spritesNOG.add(Nathanoverg)


background1Img = pygame.image.load('MapPokemon4.png')
background1Img = pygame.transform.scale(background1Img, (2400, int((1800/1000)*screenwidth)))
background1X = 0
background1Y = 0

background2Img = pygame.image.load('MapPokemon4.png')
background2Img = pygame.transform.scale(background2Img, (2400, int((1800/1000)*screenwidth)))
background2X = -1200
background2Y = 0

background3Img = pygame.image.load('MapPokemon4.png')
background3Img = pygame.transform.scale(background3Img, (2400, int((1800/1000)*screenwidth)))
background3X = 0
background3Y = -730

Barretexte = pygame.image.load('barretexte.png')
Barretexte = pygame.transform.scale(Barretexte,(int((100/100)*screenwidth),int((75/100)*screenheight)))
BarretexteX= (0/100)*screenwidth
BarretexteY= (30/100)*screenheight

DialogueRival = pygame.image.load('KalTalks.png')
DialogueRival = pygame.transform.scale(DialogueRival,(int((30/100)*screenwidth),int((27/100)*screenheight)))
DialogueRivalX= (0/100)*screenwidth
DialogueRivalY= (73/100)*screenheight

background4Img = pygame.image.load('MapPokemon4.png')
background4Img = pygame.transform.scale(background4Img, (2400, int((1800/1000)*screenwidth)))
background4X = -1200
background4Y = -730

background5Img = pygame.image.load('MapPokemon4.png')
background5Img = pygame.transform.scale(background5Img, (2400, int((1800/1000)*screenwidth)))
background5X = 0
background5Y = -1425

background6Img = pygame.image.load('MapPokemon4.png')
background6Img = pygame.transform.scale(background6Img, (2400, int((1800/1000)*screenwidth)))
background6X = -1200
background6Y = -1425

HerosStatique = pygame.image.load('HerosOverworldBas-1.png')
HerosStatique = pygame.transform.scale(HerosStatique, (int((3.6/100)*screenwidth), int((7.2/100)*screenheight)))
HerosStatiqueX = 40
HerosStatiqueY = 60

def background1():
    screen.blit(background1Img, (background1X, background1Y))

def background2():
    screen.blit(background2Img, (background2X, background2Y))

def background3():
    screen.blit(background3Img, (background3X, background3Y))

def background4():
    screen.blit(background4Img, (background4X, background4Y))

def background5():
    screen.blit(background5Img, (background5X, background5Y))

def background6():
    screen.blit(background6Img, (background6X, background6Y))

def Heros():
    screen.blit(HerosStatique, (HerosStatiqueX, HerosStatiqueY))

def barretexte():
    screen.blit(Barretexte, (BarretexteX, BarretexteY))

def KalDialogue():
    screen.blit(DialogueRival, (DialogueRivalX, DialogueRivalY))

def txtchallengeKal():
    screen.blit(textchallengeKal, (int((40/100)*screenwidth), int((85/100)*screenheight)))

def txtchallengeKal2():
    screen.blit(textchallengeKal2, (int((40/100)*screenwidth), int((95/100)*screenheight)))

MapPart1=False
MapPart2=False
MapPart3=False
MapPart4=False
MapPart5=True
MapPart6=False
Rivalfight=False
txtChallengeKal=False
widthB = int((90/100)*screenwidth)
heightB = int((90/100)*screenheight)

policearialdialogue = pygame.font.Font("Pokemon.ttf", 20)
textchallengeKal = policearialdialogue.render("Tu es prêt ?", 1, white)
pygame.mixer_music.load("Bourg-Courmomble.wav")
pygame.mixer.music.play(loops=-1, fade_ms=2)
running = True
while running:
   
    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()

  
    if MapPart1==True:
        background1()
        all_spritesNOH.update()
        all_spritesNOH.draw(screen)
        all_spritesNOD.update()
        all_spritesNOD.draw(screen)
        all_spritesNOG.update()
        all_spritesNOG.draw(screen)
        all_spritesNOB.update()
        all_spritesNOB.draw(screen)
    
    
    if XNat>=screenwidth and MapPart1 ==True:
       MapPart2=True
       MapPart1=False
       XNat-=1150
   
    if MapPart2==True:
        background2()
        all_spritesNOH.update()
        all_spritesNOH.draw(screen)
        all_spritesNOD.update()
        all_spritesNOD.draw(screen)
        all_spritesNOG.update()
        all_spritesNOG.draw(screen)
        all_spritesNOB.update()
        all_spritesNOB.draw(screen)

    if MapPart3==True:
        background3()
        all_spritesNOH.update()
        all_spritesNOH.draw(screen)
        all_spritesNOD.update()
        all_spritesNOD.draw(screen)
        all_spritesNOG.update()
        all_spritesNOG.draw(screen)
        all_spritesNOB.update()
        all_spritesNOB.draw(screen)

    if MapPart4==True:
        background4()
        all_spritesNOH.update()
        all_spritesNOH.draw(screen)
        all_spritesNOD.update()
        all_spritesNOD.draw(screen)
        all_spritesNOG.update()
        all_spritesNOG.draw(screen)
        all_spritesNOB.update()
        all_spritesNOB.draw(screen)

    if MapPart5==True:
        background5()
        all_spritesNOH.update()
        all_spritesNOH.draw(screen)
        all_spritesNOD.update()
        all_spritesNOD.draw(screen)
        all_spritesNOG.update()
        all_spritesNOG.draw(screen)
        all_spritesNOB.update()
        all_spritesNOB.draw(screen)

    if MapPart6==True:
        background6()
        all_spritesNOH.update()
        all_spritesNOH.draw(screen)
        all_spritesNOD.update()
        all_spritesNOD.draw(screen)
        all_spritesNOG.update()
        all_spritesNOG.draw(screen)
        all_spritesNOB.update()
        all_spritesNOB.draw(screen)
    
    
    if XNat<=0 and MapPart2==True:
        MapPart2=False
        MapPart1=True
        XNat+=1150

    if YNat >=screenheight and MapPart1==True:
        MapPart1=False
        MapPart3=True
        YNat-= 702
    
    if YNat<=0 and MapPart3==True:
        MapPart3=False
        MapPart1=True
        YNat+=702

    if YNat>=screenheight and MapPart2==True:
        MapPart2=False
        MapPart4=True
        YNat-=702

    if YNat<=0 and MapPart4==True:
        MapPart4=False
        MapPart2=True
        YNat+=702

    if XNat<=0 and MapPart4==True:
        MapPart4=False
        MapPart3=True
        XNat+=1150

    if XNat>=screenwidth and MapPart3==True:
        MapPart3=False
        MapPart4=True
        XNat-=1150
    
    if YNat>=screenheight and MapPart3==True:
        MapPart3=False
        MapPart5=True
        YNat-=702

    if YNat<=0 and MapPart5==True:
        MapPart5=False
        MapPart3=True
        YNat+=702

    if XNat>=screenwidth and MapPart5==True:
        MapPart5=False
        MapPart6=True
        XNat-=1150

    if XNat<=0 and MapPart6==True:
        MapPart6=False
        MapPart5=True
        XNat+=1150

    if YNat>=screenheight and MapPart4==True:
        MapPart4=False
        MapPart6=True
        YNat-=702

    if YNat<=0 and MapPart6==True:
        MapPart6=False
        MapPart4=True
        YNat+=702
        
    
    if 1000<XNat<1060 and 200<YNat<250 and MapPart2==True:
            barretexte()
            KalDialogue()
            txtchallengeKal()
            if BarretexteX <= mouse[0] <= BarretexteX+widthB and BarretexteY <= mouse[1] <= BarretexteY+heightB:
                if click[0] == 1:
                    txtChallengeKal=True
            
            if txtChallengeKal==True:
                import Pokemon_Interface_GénésisTrue

               
        








       
     
   
 
    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            all_spritesNOD.add(Nathanoverd)
            all_spritesNOD.update()
            all_spritesNOD.draw(screen)
            all_spritesNOB.remove(Nathanoverb)
            all_spritesNOG.remove(Nathanoverg)
            all_spritesNOH.remove(Nathanoverh)
        if keys[pygame.K_LEFT]:
            all_spritesNOG.add(Nathanoverg)
            all_spritesNOG.update()
            all_spritesNOG.draw(screen)
            all_spritesNOB.remove(Nathanoverb)
            all_spritesNOD.remove(Nathanoverd)
            all_spritesNOH.remove(Nathanoverh)
        if keys[pygame.K_DOWN]:
            all_spritesNOB.add(Nathanoverb)
            all_spritesNOB.update()
            all_spritesNOB.draw(screen)
            all_spritesNOD.remove(Nathanoverd)
            all_spritesNOG.remove(Nathanoverg)
            all_spritesNOH.remove(Nathanoverh)
        if keys[pygame.K_UP]:
            all_spritesNOH.add(Nathanoverh)
            all_spritesNOH.update()
            all_spritesNOH.draw(screen)
            all_spritesNOB.remove(Nathanoverb)
            all_spritesNOG.remove(Nathanoverg)
            all_spritesNOD.remove(Nathanoverd)
        
     
            #import Pokemon_Interface_GénésisTrue.py

        
  
    

   
      

    pygame.display.update()
    clock.tick(20)