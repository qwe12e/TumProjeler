import os
from shutil import copy2
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
ana = Klasor("Mutant")
ana.icerigi_oku()
def yedekle(ana_klasor, yedek_klasor):
    for dosya in ana_klasor.dosyalar:
        try:
            os.mkdir(os.path.join(yedek_klasor.kesin_yolu, dosya.ad))
            copy2(dosya.kesin_yolu, os.path.join(yedek_klasor.kesin_yolu, dosya.ad, "1"))
            return
        except FileExistsError as hata:
            pass
    for dosya in ana_klasor.dosyalar:
        for yedek_klasor_klasoru in yedek_klasor.klasorler:
            if dosya.ad == yedek_klasor_klasoru.ad:

                if not dosya.degisme_tarihi == yedek_klasor_klasoru.dosyalar[-1].degisme_tarihi:
                    print("asd")
                    copy2(dosya.kesin_yolu, os.path.join(yedek_klasor.kesin_yolu, dosya.ad, str(int(yedek_klasor_klasoru.dosyalar[-1].ad) +1)))
            else:
                print(dosya.ad ,"!= ", yedek_klasor_klasoru.ad)


yedekle(ana, yedek)