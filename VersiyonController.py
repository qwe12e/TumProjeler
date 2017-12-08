import os
from shutil import copy2, copytree, rmtree
from typing import List


class Dosya:

    def __init__(self, yol):
        self.kesin_yolu = os.path.abspath(yol)
        self.ad = os.path.split(self.kesin_yolu)[1]
        self.degisme_tarihi = os.path.getmtime(self.kesin_yolu)

class Klasor(Dosya):
    def __init__(self, yol):
        Dosya.__init__(self, yol)
        self.klasorler = []  # type: List[Klasor]
        self.dosyalar = []  # type: List[Dosya]

    def icerigi_oku(self):
        for dosya_adi in os.listdir(self.kesin_yolu):
            if os.path.isfile(os.path.join(self.kesin_yolu, dosya_adi)):
                self.dosyalar.append(Dosya(os.path.join(self.kesin_yolu, dosya_adi)))
            else:
                k = Klasor(os.path.join(self.kesin_yolu, dosya_adi))
                k.icerigi_oku()
                self.klasorler.append(k)

yedek = Klasor("MutantArchive")
yedek.icerigi_oku()
ana = Klasor("Mutant")
ana.icerigi_oku()
cop = Klasor("MutantBin")
cop.icerigi_oku()
def yedekle(ana_klasor, yedek_klasor, cop_klasor):
    # Değişiklikleri Yedekle
    for dosya in ana_klasor.dosyalar:
        try:
            os.mkdir(os.path.join(yedek_klasor.kesin_yolu, dosya.ad))
            copy2(dosya.kesin_yolu, os.path.join(yedek_klasor.kesin_yolu, dosya.ad, "1+"))
            continue
        except FileExistsError as hata:
            for yedek_klasor_klasoru in yedek_klasor.klasorler:
                if dosya.ad == yedek_klasor_klasoru.ad:
                    if not dosya.degisme_tarihi == yedek_klasor_klasoru.dosyalar[-1].degisme_tarihi:
                        print("asd")
                        yeni_ad = str(int(yedek_klasor_klasoru.dosyalar[-1].ad[:-1]) + 1)+"+"
                        copy2(dosya.kesin_yolu, os.path.join(yedek_klasor.kesin_yolu, dosya.ad, yeni_ad))
                else:
                    print(dosya.ad, "!= ", yedek_klasor_klasoru.ad)
    # Silinen Dosyaların Yedeklerini Çöpe At
    for klasor in yedek_klasor.klasorler:
        if (not os.path.isfile(os.path.join(ana_klasor.kesin_yolu,klasor.ad))) and (klasor.dosyalar[-1].ad[-1] == "+"):
            yeni_ad = str(int(klasor.dosyalar[-1].ad[:-1]) + 1) + "-"
            with open(os.path.join(klasor.kesin_yolu, yeni_ad), "w") as f:
                pass

def geri_yukle(ana_klasor: Klasor, yedek_klasor: Klasor, cop_klasor: Klasor, tarih: int):

    for klasor in yedek_klasor.klasorler:
        try:
            os.remove(os.path.join(ana_klasor.kesin_yolu, klasor.ad))
        except FileNotFoundError as hata:
            pass
        for yedek in klasor.dosyalar[::-1]:
            if yedek.degisme_tarihi <= tarih:
                copy2(yedek.kesin_yolu, os.path.join(ana_klasor.kesin_yolu, klasor.ad + ".geri"))



yedekle(ana, yedek, cop)
# geri_yukle(ana, yedek, cop, 1512741266)