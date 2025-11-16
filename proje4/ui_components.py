"""
arayüz parçaları - butonlar falan işte
"""
import pygame
import math
from config import SIYAH


class Buton:
    """dikdörtgen buton (START, STOP falan işte)"""
    
    def __init__(self, x, y, genislik, yukseklik, yazi, renk):
        self.dikdortgen = pygame.Rect(x, y, genislik, yukseklik)
        self.yazi = yazi
        self.renk = renk
        self.temel_renk = renk
        self.uzerine_gelinc_renk = tuple(min(r + 30, 255) for r in renk)
        self.ustunde_mi = False
        
    def ciz(self, yuzey):
        """butonu ekrana cizicez"""
        simdiki_renk = self.uzerine_gelinc_renk if self.ustunde_mi else self.temel_renk
        pygame.draw.rect(yuzey, simdiki_renk, self.dikdortgen, border_radius=8)
        pygame.draw.rect(yuzey, SIYAH, self.dikdortgen, 3, border_radius=8)
        
        font = pygame.font.Font(None, 24)
        yazi_yuzeyi = font.render(self.yazi, True, SIYAH)
        yazi_dikdortgeni = yazi_yuzeyi.get_rect(center=self.dikdortgen.center)
        yuzey.blit(yazi_yuzeyi, yazi_dikdortgeni)
        
    def uzerinde_mi_kontrol(self, pozisyon):
        """fare butonun ustunde mi diye bakıcaz"""
        self.ustunde_mi = self.dikdortgen.collidepoint(pozisyon)
        
    def tiklandi_mi(self, pozisyon):
        """butona tıklandı mı diye bakıcaz"""
        return self.dikdortgen.collidepoint(pozisyon)


class BoyutButonu:
    """yuvarlak boyut seçme butonu işte"""
    
    def __init__(self, x, y, yaricap):
        self.x = x
        self.y = y
        self.yaricap = yaricap
        self.secili_mi = False
        
    def ciz(self, yuzey):
        """boyut butonunu cizicez"""
        from config import KOYU_GIRI, ACIK_GIRI
        renk = KOYU_GIRI if self.secili_mi else ACIK_GIRI
        pygame.draw.circle(yuzey, renk, (self.x, self.y), self.yaricap)
        pygame.draw.circle(yuzey, SIYAH, (self.x, self.y), self.yaricap, 3)
        
    def tiklandi_mi(self, pozisyon):
        """butona tıklandı mı diye bakıcaz"""
        uzaklik = math.sqrt((pozisyon[0] - self.x) ** 2 + (pozisyon[1] - self.y) ** 2)
        return uzaklik <= self.yaricap


class RenkButonu:
    """kare renk seçme butonu"""
    
    def __init__(self, x, y, boyut, renk):
        self.dikdortgen = pygame.Rect(x - boyut // 2, y - boyut // 2, boyut, boyut)
        self.renk = renk
        self.secili_mi = False
        
    def ciz(self, yuzey):
        """renk butonunu cizicez"""
        pygame.draw.rect(yuzey, self.renk, self.dikdortgen)
        kenar_kalinligi = 5 if self.secili_mi else 3
        pygame.draw.rect(yuzey, SIYAH, self.dikdortgen, kenar_kalinligi)
        
    def tiklandi_mi(self, pozisyon):
        """butona tıklandı mı diye bakıcaz"""
        return self.dikdortgen.collidepoint(pozisyon)
