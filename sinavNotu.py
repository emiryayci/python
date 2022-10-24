#Sınav notunu hangi harfle geçtiğini hesaplayan program
vizeNotu=int(input("Vize notunuz :"))
finalNotu=int(input("Final notunuz :"))
if vizeNotu<50:
    print("Sınav notunuz :F (GEÇEMEDİNİZ)")
if 64>vizeNotu>=50:
    print("Sınav notunuz :D ( Sorumlu Geçtiniz)")
if 74>vizeNotu>65:
    print("Sınav notunuz :C (Geçtiniz)")
if 89>vizeNotu>75:
    print("Sınav notunuz :B (Geçtiniz)")
if 100>=vizeNotu>90:
    print("Sınav notunuz :A (Geçtiniz)")
if finalNotu<35:
        print("Sınav notunuz: F (Geçemediniz)")
if 36<finalNotu<49:
    print("Sınav notunuz :E (Şartlı geçtiniz)")
if 50<finalNotu<64:
    print("Sınav notunuz :D (Geçtiniz)")
if 65<finalNotu<74:
    print("Sınav notunuz :C (Geçtiniz)")
if 75<finalNotu<84:
    print("Sınav notunuz :B (Geçtiniz)")
if 85<finalNotu<=100:
    print("Sınav notunuz :A (Geçtiniz)")