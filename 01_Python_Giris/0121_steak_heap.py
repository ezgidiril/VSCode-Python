"""
a=1
b=2
a=b
b=1
print(a,b)

a=4
b=2
c=(a+b)//2
print("(",a,"+",b,")/2=",c)

sayi=562
bir=sayi//100
iki=(sayi-(bir*100))//10
üc=sayi-(bir*100+iki*10)

print(bir,iki,üc)
print(bir+iki+üc)
"""
# formatter shift+ alt+f
sayi = 562
bir = sayi % 10
kalan = sayi % 100
iki = kalan//10
üc = sayi//100
print(bir, iki, üc)
