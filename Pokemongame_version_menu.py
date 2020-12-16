import pygame
 
pygame.init()
pygame.font.init()
screenwidth = 1500  #Choose your screen size
screenheight = int((625/1000)*screenwidth)
RUNNING = True
 
fenetre = pygame.display.set_mode((screenwidth,screenheight))
background1Img = pygame.image.load('Forest.png')
background1Img = pygame.transform.scale(background1Img, (screenwidth, screenheight))
background1X = 0
background1Y = 0

pokemon1Img = pygame.image.load('Feuillausaure.png')
pokemon1Img = pygame.transform.scale(pokemon1Img, (int((22/100)*screenwidth), int((43/100)*screenheight)))
pokemon1X = (1/100)*screenwidth
pokemon1Y = (10/100)*screenheight

#Barre de vie pokemon 1
HPbar = pygame.image.load('Sprite barre de vie.png')
HPbar = pygame.transform.scale(HPbar, (int((43/100)*screenwidth), int((67/100)*screenheight)))
HPbarX = (1/100)*screenwidth
HPbarY = (5/100)*screenheight
colorHPbar = (0, 255, 0)

#barre vie 1
barposX = ((1/100)*screenwidth)+(1/100)*int((33/100)*screenwidth)
barposY = ((22/100)*screenheight)+(100/1000)*int((33/100)*screenheight)
barwidth = int((440/1000)*(33/100)*screenwidth)
barheight = int((17/100)*(9/100)*screenheight)



#pikachu ennemi animé
class Pikachu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        image1 = pygame.image.load('tile000.png')
        image1 = pygame.transform.scale(image1, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image2 = pygame.image.load('tile001.png')
        image2 = pygame.transform.scale(image2, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image3 = pygame.image.load('tile002.png')
        image3 = pygame.transform.scale(image3, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image4 = pygame.image.load('tile003.png')
        image4 = pygame.transform.scale(image4, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image5 = pygame.image.load('tile004.png')
        image5 = pygame.transform.scale(image5, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image6 = pygame.image.load('tile005.png')
        image6 = pygame.transform.scale(image6, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image7 = pygame.image.load('tile006.png')
        image7 = pygame.transform.scale(image7, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image8 = pygame.image.load('tile007.png')
        image8 = pygame.transform.scale(image8, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image9 = pygame.image.load('tile008.png')
        image9 = pygame.transform.scale(image9, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image10 = pygame.image.load('tile009.png')
        image10 = pygame.transform.scale(image10, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image11 = pygame.image.load('tile010.png')
        image11 = pygame.transform.scale(image11, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image12 = pygame.image.load('tile011.png')
        image12 = pygame.transform.scale(image12, (int((40/100)*screenwidth), int((60/100)*screenheight)))


        self.sprites.append(image1)
        self.sprites.append(image2)
        self.sprites.append(image3)
        self.sprites.append(image4)
        self.sprites.append(image5)
        self.sprites.append(image6)
        self.sprites.append(image7)
        self.sprites.append(image8)
        self.sprites.append(image9)
        self.sprites.append(image10)
        self.sprites.append(image11)
        self.sprites.append(image12)
        self.sprites.append(image12)
        self.sprites.append(image12)
        self.sprites.append(image12)
        self.sprites.append(image12)
        self.sprites.append(image12)
        self.sprites.append(image12)
        self.sprites.append(image12)
        self.sprites.append(image12)


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = ((75/100)*screenwidth, (35/100)*screenheight)

    def update(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]



all_sprites = pygame.sprite.Group()
pikachu = Pikachu()
all_sprites.add(pikachu)



#Barre de vie pokemon 2
HPbar2 = pygame.image.load('sprite barre de vie ennemy.png')
HPbar2 = pygame.transform.scale(HPbar2, (int((43/100)*screenwidth), int((67/100)*screenheight)))
HPbar2X = (68/100)*screenwidth
HPbar2Y = (5/100)*screenheight
colorHPbar = (0, 255, 0)

#barre vie 2
barpos2X = (HPbar2X+(11/100)*int((33/100)*screenwidth))
barpos2Y = (HPbar2Y+(105/1000)*int((33/100)*screenheight))
barwidth2 = int((783/1000)*(33/100)*screenwidth)
barheight2 = int((17/100)*(9/100)*screenheight)

#button1
button1Img = pygame.image.load('attack.png')
button1Img = pygame.transform.scale(button1Img, (int((63/100)*screenwidth), int((62/100)*screenheight)))
button1X = (1/100)*screenwidth
button1Y = (80/100)*screenheight

widthB1 = int((63/100)*screenwidth)
heightB1 = int((62/100)*screenheight)
click1=0

#button1v2
button1v2Img = pygame.image.load('attack2.png')
button1v2Img = pygame.transform.scale(button1v2Img, (int((63/100)*screenwidth), int((62/100)*screenheight)))
button1v2X = (1/100)*screenwidth
button1v2Y = (80/100)*screenheight



attackValue = 30

timeCount = 0

myfont = pygame.font.SysFont('Helvetic', 20)
 
 
def gerer_events_principale():
    global RUNNING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
 
def menu():
    rect = pygame.draw.rect(
        fenetre,
        (255,0,0),
        pygame.Rect(100, 200, 100, 100))

    text = myfont.render('ButtonA', False, (255,255,255))
    fenetre.blit(text, (100,200))
 
    gerer_mouse_menu(rect)

def background1():
    fenetre.blit(background1Img, (background1X, background1Y))
def pokemon1():
    fenetre.blit(pokemon1Img, (190, 350))
def button1():
    fenetre.blit(button1Img, (-80, 630))
def button1v2():
    fenetre.blit(button1v2Img, (-80, 630))
def barrevie1():
    fenetre.blit(HPbar, (855, 260))
def barrevie2():
    fenetre.blit(HPbar2, (-70, -160))

def jeu():
    background1()
    pokemon1()
    all_sprites.update()
    all_sprites.draw(fenetre)
    gerer_mouse_jeu()
   
 
def gerer_mouse_jeu():
    
     mouse = pygame.mouse.get_pos()

     click = pygame.mouse.get_pressed()
     button1()
     barrevie2()
     barrevie1()
     barposX = ((1/100)*screenwidth)+(1/100)*int((33/100)*screenwidth)
     barposY = ((22/100)*screenheight)+(100/1000)*int((33/100)*screenheight)
     barwidth = int((440/1000)*(33/100)*screenwidth)
     barheight = int((17/100)*(9/100)*screenheight)
     barpos2X = (HPbar2X+(11/100)*int((33/100)*screenwidth))
     barpos2Y = (HPbar2Y+(105/1000)*int((33/100)*screenheight))
     barwidth2 = int((783/1000)*(33/100)*screenwidth)
     barheight2 = int((17/100)*(9/100)*screenheight)
     attackValue = 30

     for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #si la souris est sur le button1
        if button1X <= mouse[0] <= button1X+widthB1 and button1Y <= mouse[1] <= button1Y+heightB1:
            if click[0] == 1:
                barwidth2 -= attackValue
        if barwidth2 < 0:
            attackValue = 0
        if button1X <= mouse[0] <= button1X+widthB1 and button1Y <= mouse[1] <= button1Y+heightB1:
            button1v2()

 
def gerer_mouse_menu(rectangle):
    global afficher
   
    click = pygame.mouse.get_pressed()
    if click[0]: # UP
        mouse = pygame.mouse.get_pos()
         
        if rectangle.collidepoint(mouse):
            print('Cliqué sur:', rectangle)
            afficher = jeu
 
## Affecte la fonction menu
afficher = menu

def boucle_principale():
    while RUNNING:
        fenetre.fill( (0,0,0) )
         
        gerer_events_principale()
         
        ## Exécute la fonction affecté à afficher (menu/jeu)
        afficher()
         
        
        pygame.display.update()
         
    pygame.quit()
 
 
 
boucle_principale()