
#Primeramente es necesario importar los modulos necesarios para realizar este proyecto.
import sys, pygame
from pygame.locals import *
from math import *
import random

#Posteriormente se inicia el modulo de Pygame para obtener algunas de las variables necesarias
pygame.init()

blanco = (255,255,255)
#Se establecen los parametros de la pantalla.
WIDTH  = 1156 
HEIGHT = 650
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS    = pygame.time.Clock()

pygame.display.set_caption('PyDeathRace')
#Se declaran tanto la imagen de la pista, como la imagen del automovil que el jugador va a utilizar.
track = pygame.image.load('Recursos/Pista.jpg').convert()

Pista = pygame.transform.scale (pygame.image.load('Recursos/Carro1.png') .convert (),(30,60))
#Se definen los grupos donde se van a colocar los sprites para hacer mas facil su acomodo y llamada. 
todos_los_sprites = pygame.sprite.Group ()

font_name = pygame.font.match_font ('arial')

#Estas lineas de codigo establecen el color, forma y fuente de la letra a utilizar para disponer de la puntiacion y el tiempo.
#Se utiliza Arial para evitar inconvenientes con otra fuente necesaria.
def text(surf,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface,text_rect)

def on_track(sprite):
    '''Tests to see if car is on the track'''
    if sprite.x > 1 and sprite.x < WIDTH - 1 and sprite.y > 1 and sprite.y < HEIGHT - 1:
        if track.get_at((int(sprite.x), int(sprite.y))).r == 163 or track.get_at((int(sprite.x), int(sprite.y))).r == 0 or track.get_at((int(sprite.x), int(sprite.y))).r == 255:
            return True
    return False

#Se define la clase Car que es la clase principal del jugador, la cual, define posiciones iniciales
#y tambien los angulos mediante los cuales va a girar. Ademas se establece el metodo "super"
#que pretende evitar cualquier tipo de error de reconocimiento.
class Car(pygame.sprite.Sprite):
    def __init__(self, start_pos = (190, 530), start_angle = 0, image = 'Recursos/Carro1.png'):
        super () .__init__()
        '''Initialises the Car object'''
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.angle = start_angle
        self.speed = 0

#Se establece un tamaño a la imagen del auto del jugador y tambien se aplica la base del rotate que
#este va a necesitar.         
        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (70, 40))
        self.rotcar   = pygame.transform.rotate(self.image, self.angle)

        self.rect = self.image.get_rect ()
        
#El metodo move define  las variables de velocidad y direccion que el auto del jugador va a tener,como
#lo son los inputs para su movimiento y rotacion. 
    def move(self, forward_speed = 1, rearward_speed = 0.2):

#Aqui se define que cuando un input se mantenga precionado que el carro comiente a acelerar a esa
#direccion de manera constante. 
        keys = pygame.key.get_pressed()
        if keys[K_a] or keys[K_LEFT]:
            self.angle += self.speed
        if keys[K_d] or keys[K_RIGHT]:
            self.angle -= self.speed
        if keys[K_w] or keys[K_UP]:
            self.speed += forward_speed
        if keys[K_s] or keys[K_DOWN]:
            self.speed -= rearward_speed

#Con esta variable se define el input necesario para que el auto del jugador logre disparar.
        if keys [K_SPACE]:
            self.shoot ()

#Se define el angulo para que de esta manera el auto no gire de manera precipida.
        self.angle %= 359

#En esta parte se define la velocidad que el auto va a tener y ademas se definen las variables de angulo
#Coseno Y Seno que permiten una rotacion delicada. 
        if on_track(self): self.speed *= 0.95
        else: self.speed *= 0.80

        self.x += self.speed * cos(radians(self.angle))
        self.y -= self.speed * sin(radians(self.angle))

#El render dibuja el carro en la pantalla del jugador segun el rectangulo colocado.
    def render(self):
        '''Renders the car on the screen'''
        self.rotcar   = pygame.transform.rotate(self.image, self.angle)

        SCREEN.blit(self.rotcar, self.rotcar.get_rect(center = (self.x, self.y)))
#Shoot nos permite crear una bala cada vez que el usuario presiona Espacio y ademas
#se crea una variable global para evitar un problema al llamar la clase.
    def shoot(self):
        global balas
        bullet = Bullet(self.x,self.y)
        balas.add(bullet)
        todos_los_sprites.add (bullet)

#Se inicializa la clase de la bala y se le dan los atributos del carro para que esta salga directamente de su posicion.
#Es por esta razon que se llama a la instancia de Carro en las siguientes lineas.        
class Bullet (pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        car = Car ()
        self.image = pygame.transform.scale (pygame.image.load ('Recursos/Bala.png').convert_alpha (), (15,15))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x= x
        self.speedy = 10
        self.angle =car.angle

#Con el Update se asegura que la rotacion de el vehiculo del jugador no afecte la direccion de las balas
#y se hubiquen sobre el carro.        
        def update (self):
            self.rect.x += self.speed * cos ( radians (self.angle))
            self.rect.y -= self.speed * sin ( radians (self.angle))
            
#Con la clase Dummy se pretende crear los bots que el jugador va a eliminar, con parametros establecidos
#como su salida y angulo inicial.       
class Dummy (pygame.sprite.Sprite):
    def __init__ (self, start_angle = 0, image = 'Recursos/Carro2.png' ):
        pygame.sprite.Sprite .__init__ (self)
        self.image = pygame.transform.scale (pygame.image.load ("Recursos/Carro2.png").convert_alpha (), (70,40))
        self.rect = self.image.get_rect (). inflate (-8,-8)
        self.rect.x = random.randint (500,550)
        self.rect.y = random.randint (510,570)
        self.speed = random.randint (2,5)
        self.angle = 0
        self.up= False
        self.down = False
        self.right = True
        self.left = False
                                             
#El update define las variables de movimiento que los Dummys deben tener.
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
        
#Con las siguientes lineas de codigo se pretende que el bot sepa un promedio de cuales deben ser las
#coordenadas en las cuales debe girar de manera aproximada.         
        if self.rect.x > 1050 and self.rect.x < random.randint(1050,1150) and self.right:
            self.image = pygame.transform.rotate(self.image, 90)
            self.right = False
            self.up = True
        if self.rect.y < 80 and self.rect.y > random.randint(10,150) and self.up:
            self.image = pygame.transform.rotate(self.image, 90)
            self.up = False
            self.left = True
        if self.rect.x > 70  and self.rect.x < random.randint(5,120) and self.left:
            self.image = pygame.transform.rotate(self.image, 90)
            self.left = False
            self.down = True
        if self.rect.y < 560  and self.rect.y > random.randint(480,610) and self.down:
            self.image = pygame.transform.rotate(self.image, 90)
            self.down = False
            self.right = True
            
def main():
    #Se llaman las instancias en el loop que se utilizan en el resto del codigo.
    car   = Car()
    bala = (Bullet (car.x,car.y))

#Se crean los grupos donde se colocan los sprites para que funcionen de la manera esperada
    jugadores = pygame.sprite.Group ()
    jugadores.add (car)

    global balas
    balas = pygame.sprite.Group ()
    enemigos = pygame.sprite.Group ()

#Se definen la cantidad de dummys en pantalla con una instancia para cada uno de ellos, en este caso, 7.
    for i in range (7):
        bot = Dummy ()
        todos_los_sprites.add (bot)
        enemigos.add

#Se definen las variables de tiempo y puntuacion en pantalla
        tiempo = 180
        score = 0
        point = 0

#Este es el loop principal del proyecto
        
    while True:
        SCREEN.blit(track, (0, 0))


#Este es el evento que cierra el juego al precionar ESC.
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

#Se definen las coliciones necesarias con el centro de la pista y el cambio en el Score.
        r1 = pygame.Rect (180,147,815,354)
        if pygame.Rect.colliderect (car.rect,r1):
            car.speed = 1.5
            score -= 5

#Se establecen los rectangulos que ayudan a sumar el puntaje de Score en pantalla con la linea de meta.
        meta = pygame.Rect (548,524,596,609)
        check = pygame.Rect (570,34,648,122)

#Aqui se suman los puntos respectivos al pasar por la meta una vez.
        if pygame.Rect.colliderect (car.rect,check):
            point += 1
        if point > 0:
            if pygame.Rect.colliderect (car.rect,meta):
                score += 500
                point = 0

#Se establece que las balas y los objetivos coliciones y que con ello se sumen 100 puntos.
        if  pygame.sprite.groupcollide (enemigos,balas,True,True):
            score += 100
            
#Se define que si el tiempo del contador es igual a Cero que se cierre la ventana del juego.
        if tiempo == 0:
            pygame.quit ()

#Se aplican los metodos necesarios para la carga de los sprites.
        car.move()
        car.render()
        bala.update ()

        todos_los_sprites.update ()

        tiempo = int (180 - (pygame.time.get_ticks () / 1000))

        todos_los_sprites.draw (SCREEN)
#Se fija donde aparece el tiempo y el Score en pantalla y ademas los frames por segundo.       
        text (SCREEN, str (tiempo), 50,600,220)
        text (SCREEN, str (score), 50,600,300)
        pygame.display.update()
        FPS.tick(60)
        

if __name__ == '__main__': main()
