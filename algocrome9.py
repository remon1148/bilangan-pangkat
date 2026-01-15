#program hitung faktorial
angka = int (input("masukan angka untuk di faktorialkan:"))
faktorial = 1

for i in range (1, angka + 1):
    faktorial = faktorial * i
    print (f"faktorial dari {i} adalah {faktorial}")
