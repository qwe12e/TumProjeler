import os
from shutil import copy2
versiyonlanklasor = "Mutant"
mutantarc = "MutantArchive"

ana_klasor = os.path.abspath(versiyonlanklasor)
hedef_klasor = os.path.join(ana_klasor, "..", mutantarc)
for dosya_adi in os.listdir(ana_klasor):
    dosya_kesinyolu = os.path.join(ana_klasor, dosya_adi)
    ana_degisme_tarih = int(os.path.getmtime(dosya_kesinyolu))
    try:
        os.makedirs(os.path.join(hedef_klasor, dosya_adi))
    except FileExistsError as klasoryok:
        pass
    son_yedek_dosya_adi = os.listdir(os.path.join(hedef_klasor, dosya_adi))[-1]
    son_yedek_dosya_kesinyolu = os.path.join(hedef_klasor, dosya_adi, son_yedek_dosya_adi)
    son_yedek_degisme_tarih = int(os.path.getmtime(son_yedek_dosya_kesinyolu))
    print(son_yedek_degisme_tarih)
    if ana_degisme_tarih > son_yedek_degisme_tarih:
        versiyon_no = 1
        hedef_dosya = os.path.join(hedef_klasor, dosya_adi, str(versiyon_no))
        while os.path.isfile(hedef_dosya):
            versiyon_no += 1
            hedef_dosya = os.path.join(hedef_klasor, dosya_adi, str(versiyon_no))

        copy2(dosya_kesinyolu, hedef_dosya)

        print(os.path.join(hedef_klasor, dosya_adi, dosya_adi))
        print(dosya_kesinyolu, ana_degisme_tarih)



