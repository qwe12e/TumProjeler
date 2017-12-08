import os
from shutil import copy2
class Dosya:

    def __init__(self, yol):
        self.kesin_yolu = os.path.abspath(yol)
        self.ad = os.path.split(self.kesin_yolu)[1]
        self.degisme_tarihi = os.path.getmtime(self.kesin_yolu)

class Klasor(Dosya):
    def __init__(self, yol):
        Dosya.__init__(self, yol)
        self.klasorler = []
        self.dosyalar = []

    def icerigi_oku(self):
        for dosya_adi in os.listdir(self.kesin_yolu):
            if os.path.isfile(os.path.join(self.kesin_yolu, dosya_adi)):
                self.dosyalar.append(Dosya(os.path.join(self.kesin_yolu, dosya_adi)))
            else:
                k = Klasor(os.path.join(self.kesin_yolu, dosya_adi))
                k.icerigi_oku()
                self.klasorler.append(k)

yedek_klasor = Klasor("MutantArchive")
ana_klasor = Klasor("Mutant")
ana_klasor.icerigi_oku()
for dosya in ana_klasor.dosyalar:
    try:
        os.mkdir(os.path.join(yedek_klasor.kesin_yolu, dosya.ad))
    except FileExistsError as hata:
        pass
