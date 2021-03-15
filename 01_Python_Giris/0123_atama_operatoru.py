"""
s=1.838895465
print(round(s,2))

kg=62
boy=1.55
vki=kg/(boy**2)
print(round(vki,2))

"""
#region sonuc_atama

i=2
i+=1
print(i)
sayi=10
sayi-=1
sayi*=2
print(sayi)

#endregion

#region az_sayida_degisken_kullanma
sayi=5
toplam=1
toplam+=sayi
print(toplam)
sayi=10
sayi+=1
toplam+=sayi
print(toplam)
#endregion

#region ornek
skor = 0
can = 3
#engeli geçtiğinde skor 1 artar
skor += 1
#engele çarptığında can 1 azalır
can -= 1
print("anlık skorunuz", skor)
print("kalan canınız", can)
#endregion