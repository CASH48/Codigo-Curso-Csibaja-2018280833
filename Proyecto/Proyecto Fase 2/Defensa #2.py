import sys, pygame
from pygame.locals import *
from math import *
import random

## Inserta el reproductor de musica de Pygame par aser utilizado posteriormente.
pygame.mixer.pre_init (44100,16,2,4096)
pygame.init()

blanco = (255,255,255)

WIDTH  = 1156 
HEIGHT = 650
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS    = pygame.time.Clock()

pygame.display.set_caption('PyDeathRace')
pista1 = pygame.image.load('Recursos/Pista1-1.png').convert()
pista2 = pygame.image.load('Recursos/Pista2-1.png').convert()
pista3 = pygame.image.load('Recursos/Pista3-1.png').convert()

todos_los_sprites = pygame.sprite.Group ()
font_name = pygame.font.match_font ('arial')

## Estas variables de niveles verifican donde debe dibujarse todos los objetos por nivel especifico.
Level1 = False
Level2 = False
Level3 = True 

## Coloca la musica de los 3 niveles diferentes con la instruccion anterior.
if Level1 == True:
    pygame.mixer.music.load ("Recursos/Track1.ogg")
    pygame.mixer.music.set_volume (0.5)
    pygame.mixer.music.play (-1)

if Level2 == True:
    pygame.mixer.music.load ("Recursos/Track2.ogg")
    pygame.mixer.music.set_volume (0.5)
    pygame.mixer.music.play (-1)

if Level3 == True:
    pygame.mixer.music.load ("Recursos/Track3.ogg")
    pygame.mixer.music.set_volume (0.5)
    pygame.mixer.music.play (-1)

 
def text(surf,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface,text_rect)

class Car(pygame.sprite.Sprite):
    def __init__(self, start_pos = (190, 530), start_angle = 0, image = 'Recursos/Carro1.png'):
        super () .__init__()
        pygame.transform.scale (pygame.image.load('Recursos/Carro1.png') .convert (),(20,30))
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.angle = start_angle
        self.speed = 0
        
        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (60, 35))
        self.rotcar   = pygame.transform.rotate(self.image, self.angle)

        self.rect = self.image.get_rect ()

##Estas seran las coordenadas de aparicion del jugar en pantalla dependiendo del nivel.
        if Level2 == True:
            self.x = 354
            self.y = 396
            self.angle = 0
            
        if Level3 == True:
            self.x = 364
            self.y = 531
            self.angle = 0

    def move(self, forward_speed = 1, rearward_speed = 0.2):

        self.foward_speed = 0.5
        self.rearward_speed = 0.2
        self.max_speed = 3
        self.max_reverse = -1

        keys = pygame.key.get_pressed()
        if keys[K_a] or keys[K_LEFT]:
            self.angle += self.speed
        if keys[K_d] or keys[K_RIGHT]:
            self.angle -= self.speed
        if keys[K_w] or keys[K_UP]:
            self.speed += forward_speed
        if keys[K_s] or keys[K_DOWN]:
            self.speed -= rearward_speed


        if self.speed > self.max_speed:
            self.speed = self.max_speed
            
        if self.speed < self.max_reverse:
            self.speed = self.max_reverse

        self.angle %= 359

## Estos son los bordes de los cuales el jugador no se puede salir de la pantalla . 
        if self.x < 0:
            self.x = 1
        if self.x > 1156:
            self.x = 1155
        if self.y < 0:
            self.y = 1
        if self.y > 650:
            self.y = 649


        self.x += self.speed * cos(radians(self.angle))
        self.y -= self.speed * sin(radians(self.angle))

    def render(self):
        self.rotcar   = pygame.transform.rotate(self.image, self.angle)
        SCREEN.blit(self.rotcar, self.rotcar.get_rect(center = (self.x, self.y)))

    def shoot(self):
        global balas
        bullet = Bullet(self.x,self.y)
        balas.add(bullet)
        todos_los_sprites.add (bullet)
  
class Bullet (pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        car = Car ()
        self.image = pygame.transform.scale (pygame.image.load ('Recursos/Bala.png').convert_alpha (), (15,15))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x= x
        self.speedy = 10
        self.time = 2
        self.angle =car.angle
 
        def update (self):
            self.rect.x += self.speed * cos ( radians (self.angle))
            self.rect.y -= self.speed * sin ( radians (self.angle))

## Las siguientes 3 class son las encargadas de colocar las zonas fuera de la pista (Pasto).       
class Mascara1 (pygame.sprite.Sprite): 
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('Recursos/Pista1-2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Mascara2 (pygame.sprite.Sprite): 
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('Recursos/Pista2-2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Mascara3 (pygame.sprite.Sprite): 
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('Recursos/Pista3-2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

## Class para definir el sprite de todas las rocas.
class Roca (pygame.sprite.Sprite):
    def __init__ (self,x,y):
        super ().__init__()
        self.image = pygame.transform.scale (pygame.image.load ("Recursos/Roca.png").convert_alpha(), (40,30))
        self.rect = self.image.get_rect ()
        self.rect.x = x
        self.rect.y = y

## Class para definir el sprite de todas los conos.
class Cono (pygame.sprite.Sprite):
    def __init__ (self,x,y):
        super ().__init__()
        self.image = pygame.transform.scale (pygame.image.load ("Recursos/Cono.png").convert_alpha(), (30,30))
        self.rect = self.image.get_rect ()
        self.rect.x = x
        self.rect.y = y

## Class para definir el sprite de todas las manchas de gasolina.
class Gasolina (pygame.sprite.Sprite):
    def __init__ (self,x,y):
        super ().__init__()
        self.image = pygame.transform.scale (pygame.image.load ("Recursos/Gasolina.png").convert_alpha(), (50,50))
        self.rect = self.image.get_rect ()
        self.rect.x = x
        self.rect.y = y
        
class Dummy (pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite .__init__ (self)
        self.image = pygame.transform.scale (pygame.image.load ("Recursos/Carro2.png").convert_alpha (), (70,40))
        self.rect = self.image.get_rect (). inflate (-8,-8)
        self.rect.x = random.randint (500,550)
        self.rect.y = random.randint (510,570)
        self.speed = random.randint (2,4)
        self.angle = 0
        self.up= False
        self.down = False
        self.right = True
        self.left = False

## Coordenadas de los Dummies en los niveles 2 y 3.
        if Level2 == True:
            self.rect.x = random.randint(571,574)
            self.rect.y = random.randint(377,485)
                
        if Level3 == True:
            self.rect.x = random.randint(560,575)
            self.rect.y = random.randint(490,590)


    def update (self):
        if self.up:
            self.rect.y -= self.speed
        if self.down:
            self.rect.y += self.speed
        if self.right:
            self.rect.x += self.speed
        if self.left:
            self.rect.x -= self.speed
            
        self.angle %= 359

## Movimiento de los Dummies del nivel 1.
        if Level1 == True:
            if self.rect.x > 1050 and self.rect.x < random.randint(1050,1150) and self.right:
                self.image = pygame.transform.rotate(self.image, 90)
                self.right = False
                self.up = True
            if self.rect.y < 80 and self.rect.y > random.randint(10,150) and self.up:
                self.image = pygame.transform.rotate(self.image, 90)
                self.up = False
                self.left = True
            if self.rect.x > 70  and self.rect.x < random.randint(15,110) and self.left:
                self.image = pygame.transform.rotate(self.image, 90)
                self.left = False
                self.down = True
            if self.rect.y < 560  and self.rect.y > random.randint(520,610) and self.down:
                self.image = pygame.transform.rotate(self.image, 90)
                self.down = False
                self.right = True

## Movimiento de los Dummies del nivel 2.
        if Level2 == True:
            if self.rect.x > 760 and self.rect.x < random.randint(760,840) and self.right:
                self.image = pygame.transform.rotate(self.image, 90)
                self.right = False
                self.down = True

            if self.rect.y > 550 and self.rect.y < random.randint(560,590) and self.down:
                self.image = pygame.transform.rotate(self.image, 90)
                self.down = False
                self.right = True
                
            if self.rect.x > 1030 and self.rect.x < random.randint(1040,1120) and self.right:
                self.image = pygame.transform.rotate(self.image, 90)
                self.right = False
                self.up = True

            if self.rect.y > 50 and self.rect.y < random.randint(50,100) and self.up:
                self.image = pygame.transform.rotate(self.image, 90)
                self.up = False
                self.left = True

            if self.rect.x < 800 and self.rect.x > random.randint(760,800) and self.left:
                self.image = pygame.transform.rotate(self.image, 90)
                self.left = False
                self.down = True

            if self.rect.y > 180 and self.rect.y < random.randint(180,220) and self.down:
                self.image = pygame.transform.rotate(self.image, 90)
                self.down = False
                self.left = True

            if self.rect.x > 300 and self.rect.x < random.randint(300,350) and self.left:
                self.image = pygame.transform.rotate(self.image, 90)
                self.left = False
                self.up = True
        
            if self.rect.y < 100 and self.rect.y > random.randint(60,100) and self.up:
                self.image = pygame.transform.rotate(self.image, 90)
                self.up = False
                self.left = True

            if self.rect.x < 100 and self.rect.x > random.randint(60,100) and self.left:
                self.image = pygame.transform.rotate(self.image, 90)
                self.left = False
                self.down = True

            if self.rect.y < 500 and self.rect.y > random.randint(500,560) and self.down:
                self.image = pygame.transform.rotate(self.image, 90)
                self.down = False
                self.right = True

            if self.rect.x > 300 and self.rect.x < random.randint(300,350) and self.right:
                self.image = pygame.transform.rotate(self.image, 90)
                self.right = False
                self.up = True

            if self.rect.y > 400 and self.rect.y < random.randint(400,450) and self.rect.x < random.randint (400,450) and self.up:
                self.image = pygame.transform.rotate(self.image, 90)
                self.up = False
                self.right = True
                
## Movimiento de los Dummies del nivel 3. 
        if Level3 == True:
            if self.rect.x > 1020 and self.rect.x < random.randint(1020,1090) and self.rect.y > random.randint(500,550) and self.right:
                self.image = pygame.transform.rotate(self.image, 90)
                self.right = False
                self.up = True
                
            if self.rect.y < 410 and self.rect.y > random.randint(380,410) and self.up:
                self.image = pygame.transform.rotate(self.image, 90)
                self.up = False
                self.left = True

            if self.rect.x > 850 and self.rect.x < random.randint(850,900) and self.left:
                self.image = pygame.transform.rotate(self.image, -90)
                self.left = False
                self.up = True
                
            if self.rect.y > 200 and self.rect.y < random.randint(200,240) and self.up:
                self.image = pygame.transform.rotate(self.image, -90)
                self.up = False
                self.right = True

            if self.rect.x > 1020 and self.rect.x < random.randint(1020,1080) and self.rect.y < random.randint(200,290) and self.right:
                self.image = pygame.transform.rotate(self.image, 90)
                self.right = False
                self.up = True        
            
            if self.rect.y < 90 and self.rect.y > random.randint(50,90) and self.up:
                self.image = pygame.transform.rotate(self.image, 90)
                self.up = False
                self.left = True

            if self.rect.x < 110 and self.rect.x > random.randint(70,110) and self.left:
                self.image = pygame.transform.rotate(self.image, 90)
                self.left = False
                self.down = True

            if self.rect.y > 210 and self.rect.y < random.randint(210,250) and self.down:
                self.image = pygame.transform.rotate(self.image, 90)
                self.down = False
                self.right = True

            if self.rect.x > 240 and self.rect.x < random.randint(240,280) and self.right:
                self.image = pygame.transform.rotate(self.image, -90)
                self.right = False
                self.down = True

            if self.rect.y > 360 and self.rect.y < random.randint(360,400) and self.down:
                self.image = pygame.transform.rotate(self.image, 90)
                self.down = False
                self.left = True

            if self.rect.x > 60 and self.rect.x < random.randint(60,100) and self.left:
                self.image = pygame.transform.rotate(self.image, 90)
                self.left = False
                self.down = True

            if self.rect.y > 530 and self.rect.y < random.randint(530,590) and self.down:
                self.image = pygame.transform.rotate(self.image, 90)
                self.down = False
                self.right = True

def main():

    car   = Car()
    bala = (Bullet (car.x,car.y))

    jugadores = pygame.sprite.Group ()
    jugadores.add (car)

    global balas
    balas = pygame.sprite.Group ()

## Todos los sprites de rocas para los 3 niveles con sus coordenadas. 
    roca1 = Roca (291,580)
    roca2 = Roca (1090,423)
    roca3 = Roca (849,45)
    roca4 = Roca (110,220)
    roca5 = Roca (30,198)
    roca6 = Roca (125,470)
    roca7 = Roca (990,470)
    roca8 = Roca (990,155)
    roca9 = Roca (125,155)
    roca10 = Roca (895,315)
    roca11= Roca (215, 315)
    rocas = pygame.sprite.Group ()

## Todos los sprites de conos para los 3 niveles con sus coordenadas. 
    cono1 = Cono (830,515)
    cono2 = Cono (1016,224)
    cono3 = Cono (360,107)
    cono4 = Cono (109,413)
    cono5 = Cono (920,580)
    cono6 = Cono (200,40)
    cono7 = Cono (300,515)
    cono8 = Cono (600,515)
    cono9 = Cono (900,515)
    cono10 = Cono (450,585)
    cono11 = Cono (750,585)
    conos = pygame.sprite.Group ()

## Todos los sprites de gasolina para los 3 niveles con sus coordenadas.
    gasolina1 = Gasolina (440,160)
    gasolina2 = Gasolina (660, 240)
    gasolina3 = Gasolina (895,95)
    gasolina4 = Gasolina (575, 95)
    gasolina5 = Gasolina (260, 95)
    gasolina6 = Gasolina (738, 35)
    gasolina7 = Gasolina (410, 35)
    gasolinas = pygame.sprite.Group ()

## Esto dibuja las coordenadas del las mascaras de los 3 niveles (Pasto).
    mapa = pygame.sprite.Group()
    track1 = Mascara1(0,0)
    track2 = Mascara2(0,0)
    track3 = Mascara3(0,0)
    
##Todas las instancias de nivel para que los objetos del juego se dibujen.
    if Level1 == True:
        mapa.add(track1)
        conos.add(cono1,cono2,cono3,cono4)
        rocas.add(roca1,roca2,roca3,roca4)
        
    if Level2 == True:
        mapa.add(track2)
        conos.add(cono2,cono4,cono6,cono5)
        rocas.add(roca1,roca2,roca3, roca5)
        gasolinas.add(gasolina1,gasolina2)

    if Level3 == True:
        mapa.add(track3)
        conos.add(cono7,cono8,cono9,cono10,cono11)
        rocas.add(roca6,roca7,roca8,roca9,roca10,roca11)
        gasolinas.add(gasolina3,gasolina4,gasolina5,gasolina6,gasolina7)

## Dummies.
    enemigos = pygame.sprite.Group ()
    for i in range (7):
        bot = Dummy ()
        todos_los_sprites.add (bot)
        enemigos.add (bot)

    tiempo = 180
    score = 0
    point = 0

##-------LOOP-------##
        
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == K_SPACE:
                    car.shoot()
        

        car.rect.x = car.x-20
        car.rect.y = car.y-20

## Meta y Checkpoint nivel 1 con sus coordenadas. 
        meta = pygame.Rect (548,524,60,120)
        check = pygame.Rect (570,34,60,120)

        if pygame.Rect.colliderect (car.rect,check) and Level1 == True:
            point += 1
        if point > 0:
            if pygame.Rect.colliderect (car.rect,meta)and Level1 == True:
                score += 1000
                point = 0

## Meta y Checkpoint nivel 2 con sus coordenadas. 
        check = pygame.Rect (551,161,60,120)
        meta = pygame.Rect (550,374,60,120)

        if pygame.Rect.colliderect (car.rect,check) and Level2 == True:
            point += 1
        if point > 0:
            if pygame.Rect.colliderect (car.rect,meta)and Level2 == True:
                score += 1000
                point = 0

## Meta y Checkpoint nivel 3 con sus coordenadas. 
        check = pygame.Rect (565,34,60,120)
        meta = pygame.Rect (565,522,60,120)

        if pygame.Rect.colliderect (car.rect,check) and Level3 == True:
            point += 1
        if point > 0:
            if pygame.Rect.colliderect (car.rect,meta)and Level3 == True:
                score += 1000
                point = 0

## Coliciones con objetos y sus cualidades especificas de puntuacion y velocidad del jugador.
        if  pygame.sprite.groupcollide (enemigos,balas,True,True):
            score += 100
            
        if pygame.sprite.groupcollide (jugadores,conos,False,True):
            score -= 100
            
        if pygame.sprite.groupcollide (jugadores,rocas,False,False):
             car.speed *= -4
             
        if pygame.sprite.groupcollide (jugadores,gasolinas,False,False):
             car.speed *= 0.2

        if pygame.sprite.collide_mask (car,track1) and Level1 == True:
            car.speed *= 0.6
            score -= 2
            
        if pygame.sprite.collide_mask (car,track2) and Level2 == True:
            car.speed *= 0.6
            score -= 2

        if pygame.sprite.collide_mask (car,track3) and Level3 == True:
            car.speed *= 0.6
            score -= 2
             
        if tiempo == 0:
            pygame.quit ()

        tiempo = int (180 - (pygame.time.get_ticks () / 1000))

## Se dibujan las pistas en las posiciones (0,0)
        if Level1 == True:
            SCREEN.blit(pista1,(0,0))
            
        if Level2 == True:
            SCREEN.blit(pista2,(0,0))
            
        if Level3 == True:
            SCREEN.blit(pista3,(0,0))

        todos_los_sprites.draw (SCREEN)
        mapa.draw(SCREEN)
        todos_los_sprites.draw (SCREEN)
        rocas.draw (SCREEN)
        conos.draw (SCREEN)
        gasolinas.draw (SCREEN)

## Con esto se dibujan en las posiciones exactas para cada nivel de los marcadores de tiempo y puntuacion. 
        if Level1 == True:
            text (SCREEN, str (tiempo), 50,750,250)
            text (SCREEN, str (score), 50,775,200)

        if Level2 == True:
            text (SCREEN, str (tiempo), 50,660,510)
            text (SCREEN, str (score), 50,775,300)

        if Level3 == True:
            text (SCREEN, str (tiempo), 50,760,340)
            text (SCREEN, str (score), 50,740,290)

## Se colocan los updates respectivos para la diferentes funciones. 
        car.move()
        car.render()
        bala.update ()
        todos_los_sprites.update ()
        pygame.display.update()
        FPS.tick(60)

if __name__ == '__main__': main()
