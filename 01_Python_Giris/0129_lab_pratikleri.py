print("""
    Martı Uygulamasına Hoş Geldiniz.
    Sürüş İcreti → 0.59/dk
""")
saat=int(input("Sürüş için geçen süre (saat) :"))
dakika= int(input("Sürüş için geçen süre (dakika) :"))
toplamSüre= saat*60 +dakika # dakikaya çeviriyoruz.
ucret= 0.59*toplamSüre
print(f"""
        Sürüş saati: {saat}
        Sürüş dakikası: {dakika}
        Toplam Sürüş süresi: {toplamSüre}
        Ödenecek ücret: {round(ucret,1)}""")