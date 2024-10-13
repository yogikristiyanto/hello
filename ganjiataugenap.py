# Fungsi untuk mengecek apakah bilangan ganjil atau genap
def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return f"{angka} adalah bilangan genap"
    else:
        return f"{angka} adalah bilangan ganjil"

# Input dari pengguna
angka = int(input("Masukkan bilangan: "))

# Panggil fungsi dan tampilkan hasilnya
hasil = cek_ganjil_genap(angka)
print(hasil)
