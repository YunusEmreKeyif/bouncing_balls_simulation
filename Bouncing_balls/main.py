"""
ana oyun dongusu - bütün parçaları bi araya getiriyo burda
"""
import pygame
from config import GENISLIK, TOPLAM_YUKSEKLIK, FPS, BEYAZ, SIYAH, YUKSEKLIK
from game_state import OyunDurumu
from ui_manager import ArayuzYoneticisi


class Oyun:
    """ana oyun sınfı - bütün parcaları koordine ediyo"""
    
    def __init__(self):
        pygame.init()
        self.ekran = pygame.display.set_mode((GENISLIK, TOPLAM_YUKSEKLIK))
        pygame.display.set_caption("Ball Animation")
        self.saat = pygame.time.Clock()
        
        self.oyun_durumu = OyunDurumu()
        self.arayuz_yoneticisi = ArayuzYoneticisi()
        self.calisiyo = True
        
    def olaylari_isle(self):
        """olayları isliycez burda"""
        fare_pozisyonu = pygame.mouse.get_pos()
        
        for olay in pygame.event.get():
            if olay.type == pygame.QUIT:
                self.calisiyo = False
                
            if olay.type == pygame.MOUSEBUTTONDOWN:
                # boyut seçimi - direkt top olusucak
                self.arayuz_yoneticisi.boyut_tiklama_isle(
                    fare_pozisyonu, 
                    self.oyun_durumu.secili_renk, 
                    self.oyun_durumu
                )
                
                # renk seçimi
                yeni_renk = self.arayuz_yoneticisi.renk_tiklama_isle(fare_pozisyonu)
                if yeni_renk:
                    self.oyun_durumu.secili_renk = yeni_renk
                
                # kontrol butonları
                self.arayuz_yoneticisi.kontrol_tiklama_isle(fare_pozisyonu, self.oyun_durumu)
        
        # buton hover efektleri
        self.arayuz_yoneticisi.uzerinde_mi_kontrol(fare_pozisyonu)
        
    def guncelle(self):
        """oyun durumunu guncelliycez"""
        self.oyun_durumu.guncelle()
        
    def ciz(self):
        """ekrana cizicez"""
        self.ekran.fill(BEYAZ)
        
        # animasyon alanı
        pygame.draw.rect(self.ekran, BEYAZ, (0, 0, GENISLIK, YUKSEKLIK))
        pygame.draw.rect(self.ekran, SIYAH, (0, 0, GENISLIK, YUKSEKLIK), 3)
        
        # topları cizicez
        self.oyun_durumu.toplari_ciz(self.ekran)
        
        # arayuzu cizicez
        self.arayuz_yoneticisi.ciz(self.ekran)
        
        pygame.display.flip()
        
    def calistir(self):
        """ana oyun dongusu burda"""
        while self.calisiyo:
            self.olaylari_isle()
            self.guncelle()
            self.ciz()
            self.saat.tick(FPS)
        
        pygame.quit()


def main():
    """programın giris noktası burası"""
    oyun = Oyun()
    oyun.calistir()


if __name__ == "__main__":
    main()