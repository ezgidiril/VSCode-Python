# break-point
#region ornek1
"""
kullanici = input("Kullanıcı adı giriniz:")
print("a")
if kullanici != "admin":
    print(f"{kullanici} yetkisi ile giremezsiniz.")
    print("b")
print("c")

bir=int(input("Birinci sayıyı giriniz:"))
iki=int(input("İkinci sayıyı giriniz:"))
if bir>iki:
    print(f"{bir} > {iki}")
"""
#endregion

#region ornek2
"""
sayi=int(input("Sayı giriniz:"))
if sayi<0:
    sayi*=(-1)
print(f"Sayının mutlak değeri {sayi}")
"""
#endregion

#region ornek3

"""
bakiye=5000
bankaKodu=101
kod=int(input("Banka kodunuzu giriniz:"))
transferucret=int(input("Transfer tutarını giriniz:"))
eksilen=0
if kod!=bankaKodu:
    eksilen=(transferucret*0.5)
print(f"Güncel bakiye: {bakiye-transferucret-eksilen}")
"""
#endregion

#region ornek4
"""
biletFiyati=int(input("Bilet Fiyatı:"))
agirlik=int(input("Bavul ağırlığı giriniz."))
kdv=0.18
ekfiyat=0
if agirlik>15:
    ekfiyat=(agirlik-15)*5
print(f"Güncel bilet fiyatınız={biletFiyati+(biletFiyati*kdv)+ekfiyat}")
"""
#endregion

#region ornek5
#3 adet sayı girilecek en büyüğü seçilecek.
"""
eb=0
s=int(input("lütfen sayı giriniz."))
if s>eb:
    eb=s
s=int(input("lütfen sayı giriniz."))
if s>eb:
    eb=s
s=int(input("lütfen sayı giriniz."))
if s>eb:
    eb=s
print("Girilen sayıların en büyüğü :",eb)
"""
#endregion