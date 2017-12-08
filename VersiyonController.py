import os
class Dosya:
    def __init__(self, ad):
        self.ad = ad
        self.kesin_yolu = os.path.abspath(self.ad)
        self.degisme_tarihi = os.path.getmtime(self.kesin_yolu)

class Directory(Dosya):
    def icindekiler(self):
        sozluk = dict()
        for dosya_adi in os.listdir(self.kesin_yolu):
            buffer_list = [0,0]
            buffer_list[0] = os.path.abspath(os.path.join(self.kesin_yolu, dosya_adi))
            buffer_list[1] = os.path.getmtime(buffer_list[0])
            sozluk[dosya_adi] = buffer_list
        return sozluk

ana_klasor = Directory("Mutant")
print(ana_klasor.icindekiler())
