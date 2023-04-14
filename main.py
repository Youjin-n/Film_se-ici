import random

dosya_adi = "Filmler.txt"
dict_list = {}
i_allmovies = []
allmovies = []
i_bilimKurgu = []
bilimKurgu = []
i_komedi = []
komedi = []
i_aksiyon = []
aksiyon = []
i_macera = []
macera = []
i_animasyon = []
animasyon = []
i_suc = []
suc = []
i_dram = []
dram = []
i_fantastik = []
fantastik = []

with open(dosya_adi, "r", encoding="utf-8") as file:
    satirlar = file.readlines()

for index, satir in enumerate(satirlar):
    dict_list[satir.strip()] = index


def allf():
    for index1 in range(dict_list["Bilim kurgu"] + 1, dict_list["<bilimson>"]):
        i_allmovies.append(index1)
    for index2 in range(dict_list["Komedi"] + 1, dict_list["<komedison>"]):
        i_allmovies.append(index2)
    for index3 in range(dict_list["Aksiyon"] + 1, dict_list["<aksiyonson>"]):
        i_allmovies.append(index3)
    for index4 in range(dict_list["Macera"] + 1, dict_list["<macerason>"]):
        i_allmovies.append(index4)
    for index5 in range(dict_list["Animasyon"] + 1, dict_list["<animasyonson>"]):
        i_allmovies.append(index5)
    for index6 in range(dict_list["Suç"] + 1, dict_list["<suçson>"]):
        i_allmovies.append(index6)
    for index7 in range(dict_list["Dram"] + 1, dict_list["<dramson>"]):
        i_allmovies.append(index7)
    for index8 in range(dict_list["Fantastik"] + 1, dict_list["<fantastikson>"]):
        i_allmovies.append(index8)
    for key, value in dict_list.items():
        if value in i_allmovies:
            allmovies.append(key)
    rastgeleall = random.choice(allmovies)
    print(rastgeleall)


def bilimKurguf():
    for index1 in range(dict_list["Bilim kurgu"] + 1, dict_list["<bilimson>"]):
        i_bilimKurgu.append(index1)
    for key1, value1 in dict_list.items():
        if value1 in i_bilimKurgu:
            bilimKurgu.append(key1)
    rastgeleBilimKurgu = random.choice(bilimKurgu)
    print(rastgeleBilimKurgu)


def komedif():
    for index2 in range(dict_list["Komedi"] + 1, dict_list["<komedison>"]):
        i_komedi.append(index2)
    for key2, value2 in dict_list.items():
        if value2 in i_komedi:
            komedi.append(key2)
    rastgeleKomedi = random.choice(komedi)
    print(rastgeleKomedi)


def aksiyonf():
    for index3 in range(dict_list["Aksiyon"] + 1, dict_list["<aksiyonson>"]):
        i_aksiyon.append(index3)
    for key3, value3 in dict_list.items():
        if value3 in i_aksiyon:
            aksiyon.append(key3)
    rastgeleAksiyon = random.choice(aksiyon)
    print(rastgeleAksiyon)


def maceraf():
    for index4 in range(dict_list["Macera"] + 1, dict_list["<macerason>"]):
        i_macera.append(index4)
    for key4, value4 in dict_list.items():
        if value4 in i_macera:
            macera.append(key4)
    rastgeleMacera = random.choice(macera)
    print(rastgeleMacera)


def animasyonf():
    for index5 in range(dict_list["Animasyon"] + 1, dict_list["<animasyonson>"]):
        i_animasyon.append(index5)
    for key5, value5 in dict_list.items():
        if value5 in i_animasyon:
            animasyon.append(key5)
    rastgeleAnimasyon = random.choice(animasyon)
    print(rastgeleAnimasyon)


def sucf():
    for index6 in range(dict_list["Suç"] + 1, dict_list["<suçson>"]):
        i_suc.append(index6)
    for key6, value6 in dict_list.items():
        if value6 in i_suc:
            suc.append(key6)
    rastgeleSuc = random.choice(suc)
    print(rastgeleSuc)


def dramf():
    for index7 in range(dict_list["Dram"] + 1, dict_list["<dramson>"]):
        i_dram.append(index7)
    for key7, value7 in dict_list.items():
        if value7 in i_dram:
            dram.append(key7)
    rastgeleDram = random.choice(dram)
    print(rastgeleDram)


def fantastikf():
    for index8 in range(dict_list["Fantastik"] + 1, dict_list["<fantastikson>"]):
        i_fantastik.append(index8)
    for key8, value8 in dict_list.items():
        if value8 in i_fantastik:
            fantastik.append(key8)
    rastgeleFantastik = random.choice(fantastik)
    print(rastgeleFantastik)


while True:
    sayi = input("""1) Bütün filmler
2) Bilim kurgu
3) Komedi
4) Aksiyon
5) Macera
6) Animasyon
7) Suç
8) Dram
9) Fantastik
0) Programdan çıkış
Bir sayı giriniz ve ENTER'a basınız (Girdiğiniz sayıya göre rastgele filminiz seçilecektir): """)

    if sayi == "1":
        allf()
        x = input("Yeniden seçim yapmak için 1'e, çıkmak için 2'ye basın: ")
        if x == "1":
            continue
        elif x == "2":
            quit()
    elif sayi == "2":
        bilimKurguf()
        x = input("Yeniden seçim yapmak için 1'e, çıkmak için 2'ye basın: ")
        if x == "1":
            continue
        elif x == "2":
            quit()
    elif sayi == "3":
        komedif()
        x = input("Yeniden seçim yapmak için 1'e, çıkmak için 2'ye basın: ")
        if x == "1":
            continue
        elif x == "2":
            quit()
    elif sayi == "4":
        aksiyonf()
        x = input("Yeniden seçim yapmak için 1'e, çıkmak için 2'ye basın: ")
        if x == "1":
            continue
        elif x == "2":
            quit()
    elif sayi == "5":
        maceraf()
        x = input("Yeniden seçim yapmak için 1'e, çıkmak için 2'ye basın: ")
        if x == "1":
            continue
        elif x == "2":
            quit()
    elif sayi == "6":
        animasyonf()
        x = input("Yeniden seçim yapmak için 1'e, çıkmak için 2'ye basın: ")
        if x == "1":
            continue
        elif x == "2":
            quit()
    elif sayi == "7":
        sucf()
        x = input("Yeniden seçim yapmak için 1'e, çıkmak için 2'ye basın: ")
        if x == "1":
            continue
        elif x == "2":
            quit()
    elif sayi == "8":
        dramf()
        x = input("Yeniden seçim yapmak için 1'e, çıkmak için 2'ye basın: ")
        if x == "1":
            continue
        elif x == "2":
            quit()
    elif sayi == "9":
        fantastikf()
        x = input("Yeniden seçim yapmak için 1'e, çıkmak için 2'ye basın: ")
        if x == "1":
            continue
        elif x == "2":
            quit()
    elif sayi == "0":
        quit()
    else:
        print("Lütfen geçerli bir sayı giriniz.")
        continue