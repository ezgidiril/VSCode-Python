#region format
"""
rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
print("girdiğiniz rakamın bir fazlası {}".format(rakam+1))
print("girdiğiniz {} rakamının bir fazlası {}".format(rakam, (rakam+1)))
a = int(input("a. değeri giriniz: "))
b = int(input("b. değeri giriniz: "))
print("{} değeri ile {} değerinin toplamı {}". format(a, b, (a+b)))
"""
#endregion

#region fstring
#ekrana output formatlarken ilk yöntem → fstring
"""

rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
print(f"girdiğiniz {rakam} rakamının bir fazlası {rakam+1}")

a=int(input("a değeri giriniz:"))
b=int(input("b değeri giriniz:"))
print(f"{a} değeri ile {b} değerinin toplamı : {a+b} 'dir.")
"""
#endregion

#region ornek
s1=int(input("Dikdörtgenin kısa kenarını girin:"))
s2=int(input("Dikdörtgenin uzun kenarını girin:"))
print(f"Dikdörtgenin çevresi 2({s1} + {s2}) = {2*(s1+s2)}")
#endregion