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


def yedekle(ana_klasor, yedek_klasor):
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
                        yeni_ad = str(int(yedek_klasor_klasoru.dosyalar[-1].ad[:-1]) + 1)+"+"
                        copy2(dosya.kesin_yolu, os.path.join(yedek_klasor.kesin_yolu, dosya.ad, yeni_ad))
                else:
                    pass
    # Silinen Dosyaların Yedeklerini Çöpe At
    for klasor in yedek_klasor.klasorler:
        if (not os.path.isfile(os.path.join(ana_klasor.kesin_yolu, klasor.ad))) and (klasor.dosyalar[-1].ad[-1] == "+"):
            yeni_ad = str(int(klasor.dosyalar[-1].ad[:-1]) + 1) + "-"
            with open(os.path.join(klasor.kesin_yolu, yeni_ad), "w") as f:
                pass


def geri_yukle(ana_klasor: Klasor, yedek_klasor: Klasor, tarih: int):

    for klasor in yedek_klasor.klasorler:
        try:
            os.remove(os.path.join(ana_klasor.kesin_yolu, klasor.ad))
        except FileNotFoundError as hata:
            pass
        for yedek in klasor.dosyalar[::-1]:
            if yedek.degisme_tarihi <= tarih and yedek.ad[-1] == "-":
                break
            if yedek.degisme_tarihi <= tarih:
                copy2(yedek.kesin_yolu, os.path.join(ana_klasor.kesin_yolu, klasor.ad + ".geri"))

import datetime
def calis():
    yedekle(ana, yedek)
    print("Yedeklendi")
    if input("Geri Yüklemek istediğiniz tarih var mı?(y/n)") == "y":
        deger = input("Lütfen tarihinizi Yıl,Ay,Gün olarak giriniz").split(",")
        deger2 = datetime.datetime(int(deger[0]), int(deger[1]), int(deger[2])).timestamp()
        geri_yukle(ana, yedek, int(deger2))
calis()