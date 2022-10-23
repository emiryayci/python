#Sınav notunu hangi harfle geçtiğini hesaplayan program
sinavNotu=int(input("Sınav notunuz :"))
if sinavNotu<50:
    print("Sınav notunuz :F (GEÇEMEDİNİZ)")
elif 64>sinavNotu>=50:
    print("Sınav notunuz DD ( Sorumlu Geçtiniz)")
elif 74>sinavNotu>65:
    print("Sınav notunuz CC (Geçtiniz)")
elif 89>sinavNotu>75:
    print("Sınav notunuz BB (Geçtiniz)")
elif 100>=sinavNotu>90:
    print("Sınav notunuz AA (Geçtiniz)")