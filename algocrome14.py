
#jam ke menit
pilihan = input("ketik 1 untuk konversi jam ke menit, ketik '2' untuk konversi menit ke jam:")
if pilihan == "1":
         jam = float(input("masukan jam:"))
         menit = jam * 60
         print(f"konversi jam kemenit adalah{menit} menit")
elif pilihan == "2":
         menit = float(input("masukan menit:"))
         jam = menit / 60
         print(f"konversi menit ke jam adalah{jam} jam")