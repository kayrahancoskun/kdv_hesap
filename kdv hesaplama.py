def kdv_hesaplama8():
    adet=int(input("Adet giriniz"))
    birim_fiyati=int(input("birim fiyati giriniz"))
    toplam_kdvsiz=adet*birim_fiyati
    kdv = toplam_kdvsiz*0.18
    sonuc=toplam_kdvsiz+kdv
    print("kdv ile fiyat",sonuc)
kdv_hesaplama8()