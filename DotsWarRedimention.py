import pygame
import sys
import random
#from math import atan2, sin, cos
from Dot import *

class DotsWar:
    def __init__(self):
        # Inicializar Pygame
        pygame.init()
        
        # Configuración de la pantalla
        self.width, self.height = 400, 600 #1080, 2185
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption("Dots War")
        
        # Definir colores
        self.colores = {
            "white" : (255, 255, 255),
            "black" : (0, 0, 0),
            "red" : (255, 0, 0),
            "green" : (0, 255, 0),
            "blue" : (0, 0, 255),
            "lightblue" : (185,232,234),
        }
         
        # Crear puntos
        self.num_dots = 20
        self.dots = [Dot(self.width, self.height) for _ in range(self.num_dots)]
        
        self.clock = pygame.time.Clock()

    def buclePrincipal(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Este es el código que redimensiona la ventana
                if event.type == pygame.VIDEORESIZE:
                    # Recrea la ventana con el nuevo tamaño
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.width = event.w
                    self.height = event.h
                    
            self.screen.fill(self.colores["black"])
        
            # Mover y dibujar puntos
            for i, self.dot in enumerate(self.dots):
                self.dot.move(self.width, self.height)
                
                # self.dot.draw(self.screen, self.colores["red"], self.dot.pos_x, self.dot.pos_x, self.dot.radius)
                self.dot.draw(self.screen, self.colores["red"])
                
                # Verificar colisiones con otros puntos
                for other_dot in self.dots[i + 1:]:
                     self.dot.check_collision(other_dot)
        
            pygame.display.flip()
            self.clock.tick(30) #60
            
dotsWar = DotsWar()
dotsWar.buclePrincipal()
