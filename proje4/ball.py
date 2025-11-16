"""
top sınfı burda - topun hareketleri falan işte
"""
import pygame
import random
from config import GENISLIK, YUKSEKLIK, SIYAH


class Top:
    """animasyonda ziplayan toplar bunlar işte"""
    
    def __init__(self, x, y, yaricap, renk):
        self.x = x
        self.y = y
        self.yaricap = yaricap
        self.renk = renk
        self.hiz_x = random.uniform(-3, 3)
        self.hiz_y = random.uniform(-3, 3)
        self.hiz_carpani = 1.0
        
    def hareket_et(self):
        """topu hareket ettir duvara carpınca seksin"""
        self.x += self.hiz_x * self.hiz_carpani
        self.y += self.hiz_y * self.hiz_carpani
        
        # duvarlara carpma kontrol edicez
        if self.x - self.yaricap <= 0 or self.x + self.yaricap >= GENISLIK:
            self.hiz_x *= -1
            self.x = max(self.yaricap, min(GENISLIK - self.yaricap, self.x))
            
        if self.y - self.yaricap <= 0 or self.y + self.yaricap >= YUKSEKLIK:
            self.hiz_y *= -1
            self.y = max(self.yaricap, min(YUKSEKLIK - self.yaricap, self.y))
    
    def ciz(self, yuzey):
        """topu ekrana cizicez"""
        pygame.draw.circle(yuzey, self.renk, (int(self.x), int(self.y)), self.yaricap)
        pygame.draw.circle(yuzey, SIYAH, (int(self.x), int(self.y)), self.yaricap, 2)
