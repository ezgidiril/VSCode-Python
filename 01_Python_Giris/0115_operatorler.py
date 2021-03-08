#aritmetik operatörler
#region islemler
"""
1→ + toplama
2→ - çıkarma
3→ * çarpma
4→ / bölme
5→ // tam bölme
6→ ** üst alma
7→  % kalan
"""
#endregion

#region örnekler
print(0.25*4)
print(type(0.25*4))
print(9/3)
print(type(9/3))
print(9//3)
print(type(9//3))
#endregion

#region öncelik
"""
1→ işaretleri (unary)
2→ ** üst alma
3→ çarpma, bölme,mod alma(kalan)
4→toplama, çıkarma

"""
print(15%4*2)  # önce mod almaya bakar left-side binding
print(2**2**3) # ** righ-side binding sağdan sola 2^3=8 2^8
#endregion

#print((3/(1**3))**0.5)
#print(((1+3)**0.5)-(2**2)/(1**2))
