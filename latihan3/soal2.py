#program menentukan hadiah
belanja=int(input("masukan total harga belanja:"))

if belanja > 1.500000 and belanja < 5000000 :
    print("SELAMAT ANDA MENDAPAT TV BRACKET")
elif belanja > 5.000000:
    print("SELAMAT ANDA MENDAPATKAN SOUND BAR")
else:
    print("tidak ada bonus")