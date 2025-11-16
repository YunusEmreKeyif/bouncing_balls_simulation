"""
kullanıcı arayüzü yoneticisi - bütün UI parçalarını yonetiyo burda
"""
import pygame
from ui_components import Buton, BoyutButonu, RenkButonu
from config import YUKSEKLIK, BEYAZ, KIRMIZI, MAVI, SARI, SIYAH, GIRI


class ArayuzYoneticisi:
    """UI parçalarını olusturup yoneten sınıf işte"""
    
    def __init__(self):
        # boyut butonları (küçük, orta, büyük)
        self.boyut_butonlari = [
            BoyutButonu(100, YUKSEKLIK + 60, 20),   # küçük
            BoyutButonu(200, YUKSEKLIK + 60, 35),   # orta
            BoyutButonu(320, YUKSEKLIK + 60, 50)    # büyük
        ]
        
        # renk butonları (kırmızı, mavi, sarı)
        self.renk_butonlari = [
            RenkButonu(100, YUKSEKLIK + 140, 50, KIRMIZI),
            RenkButonu(200, YUKSEKLIK + 140, 50, MAVI),
            RenkButonu(320, YUKSEKLIK + 140, 50, SARI)
        ]
        
        # kontrol butonları
        self.baslat_butonu = Buton(470, YUKSEKLIK + 20, 100, 45, "START", BEYAZ)
        self.durdur_butonu = Buton(580, YUKSEKLIK + 20, 100, 45, "STOP", BEYAZ)
        self.sifirla_butonu = Buton(470, YUKSEKLIK + 75, 100, 45, "RESET", BEYAZ)
        self.hizlan_butonu = Buton(580, YUKSEKLIK + 75, 100, 45, "SPEED UP", BEYAZ)
        
    def uzerinde_mi_kontrol(self, fare_pozisyonu):
        """fare pozisyonuna gore hover efektleri guncelliycez"""
        self.baslat_butonu.uzerinde_mi_kontrol(fare_pozisyonu)
        self.durdur_butonu.uzerinde_mi_kontrol(fare_pozisyonu)
        self.sifirla_butonu.uzerinde_mi_kontrol(fare_pozisyonu)
        self.hizlan_butonu.uzerinde_mi_kontrol(fare_pozisyonu)
        
    def boyut_tiklama_isle(self, fare_pozisyonu, secili_renk, oyun_durumu):
        """boyut butonuna tıklandıgında isliycez"""
        for boyut_btn in self.boyut_butonlari:
            if boyut_btn.tiklandi_mi(fare_pozisyonu):
                if secili_renk:
                    oyun_durumu.top_ekle(boyut_btn.yaricap, secili_renk)
                return True
        return False
    
    def renk_tiklama_isle(self, fare_pozisyonu):
        """renk butonuna tıklandıgında secili rengi dondurucez"""
        for renk_btn in self.renk_butonlari:
            if renk_btn.tiklandi_mi(fare_pozisyonu):
                for rb in self.renk_butonlari:
                    rb.secili_mi = False
                renk_btn.secili_mi = True
                return renk_btn.renk
        return None
    
    def kontrol_tiklama_isle(self, fare_pozisyonu, oyun_durumu):
        """kontrol butonlarına tıklandıgında isliycez"""
        if self.baslat_butonu.tiklandi_mi(fare_pozisyonu):
            oyun_durumu.baslat()
        elif self.durdur_butonu.tiklandi_mi(fare_pozisyonu):
            oyun_durumu.durdur()
        elif self.sifirla_butonu.tiklandi_mi(fare_pozisyonu):
            oyun_durumu.sifirla()
        elif self.hizlan_butonu.tiklandi_mi(fare_pozisyonu):
            oyun_durumu.hizlandir()
            
    def ciz(self, yuzey):
        """bütün UI parçalarını cizicez"""
        from config import GENISLIK, YUKSEKLIK
        
        # kontrol paneli arka planı
        pygame.draw.rect(yuzey, GIRI, (0, YUKSEKLIK, GENISLIK, 200))
        pygame.draw.line(yuzey, SIYAH, (0, YUKSEKLIK), (GENISLIK, YUKSEKLIK), 3)
        
        # etiketler
        font = pygame.font.Font(None, 26)
        boyut_etiketi = font.render("Size:", True, SIYAH)
        yuzey.blit(boyut_etiketi, (20, YUKSEKLIK + 50))
        
        renk_etiketi = font.render("Color:", True, SIYAH)
        yuzey.blit(renk_etiketi, (20, YUKSEKLIK + 130))
        
        # boyut butonları
        for boyut_btn in self.boyut_butonlari:
            boyut_btn.ciz(yuzey)
        
        # renk butonları
        for renk_btn in self.renk_butonlari:
            renk_btn.ciz(yuzey)
        
        # kontrol butonları
        self.baslat_butonu.ciz(yuzey)
        self.durdur_butonu.ciz(yuzey)
        self.sifirla_butonu.ciz(yuzey)
        self.hizlan_butonu.ciz(yuzey)
