#tebak angka
import random
rahasia_angka = random.randint(1, 100)
tebakan = None

while tebakan != rahasia_angka:
    tebakan = int(input("tebak angkaa antara 1 sampai 100:"))

    if tebakan < rahasia_angka:
        print("terlalu rendah! coba lagi.")
    elif tebakan > rahasia_angka:
        print("terlalu tinggi")
    else:
        print("selamat! angka yang anda tebak benar!")
