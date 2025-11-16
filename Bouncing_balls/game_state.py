"""
oyunun durumu yoneticisi - oyunun mantıgını falan yönetiyo burda
"""
import random
from ball import Top
from config import GENISLIK, YUKSEKLIK


class OyunDurumu:
    """oyunun durumunu ve mantıgını yoneten sınıf işte"""
    
    def __init__(self):
        self.toplar = []
        self.calisiyo_mu = False
        self.secili_renk = None
        self.hiz_carpani = 1.0
        
    def top_ekle(self, yaricap, renk):
        """rastgele yerde yeni top ekliycez"""
        kenar_boslugu = yaricap + 10
        rastgele_x = random.randint(kenar_boslugu, GENISLIK - kenar_boslugu)
        rastgele_y = random.randint(kenar_boslugu, YUKSEKLIK - kenar_boslugu)
        
        yeni_top = Top(rastgele_x, rastgele_y, yaricap, renk)
        yeni_top.hiz_carpani = self.hiz_carpani
        self.toplar.append(yeni_top)
        
    def baslat(self):
        """animasyonu baslatıcaz"""
        self.calisiyo_mu = True
        
    def durdur(self):
        """animasyonu durdurcaz"""
        self.calisiyo_mu = False
        
    def sifirla(self):
        """oyunu sıfırlıycaz"""
        self.toplar.clear()
        self.calisiyo_mu = False
        self.hiz_carpani = 1.0
        
    def hizlandir(self):
        """topların hızını artırıcaz"""
        self.hiz_carpani += 0.5
        for top in self.toplar:
            top.hiz_carpani = self.hiz_carpani
            
    def guncelle(self):
        """oyun durumunu guncelliycez (topları hareket ettircez)"""
        if self.calisiyo_mu:
            for top in self.toplar:
                top.hareket_et()
                
    def toplari_ciz(self, yuzey):
        """bütün topları cizicez"""
        for top in self.toplar:
            top.ciz(yuzey)
