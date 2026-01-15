#mill ke kilometer
def mill_ke_km(mill):
    kilometer = mill / 1000
    return kilometer

mill = float(input("masukan jarak dalam mill:"))
km = mill_ke_km(mill)

print(f"jarak dalam kilometer adalah {km} km")
