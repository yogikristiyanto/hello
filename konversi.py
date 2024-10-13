# Fungsi untuk konversi jam dan menit ke detik
def waktu_ke_detik(jam, menit):
    detik = (jam * 3600) + (menit * 60)
    return detik

# Fungsi untuk konversi tahun dan bulan ke hari
def waktu_ke_hari(tahun, bulan):
    hari_tahun = tahun * 365  # Asumsi 1 tahun = 365 hari
    hari_bulan = bulan * 30    # Asumsi 1 bulan = 30 hari
    total_hari = hari_tahun + hari_bulan
    return total_hari

# Input dari pengguna
jam = int(input("Masukkan jam: "))
menit = int(input("Masukkan menit: "))
tahun = int(input("Masukkan tahun: "))
bulan = int(input("Masukkan bulan: "))

# Konversi waktu
detik = waktu_ke_detik(jam, menit)
hari = waktu_ke_hari(tahun, bulan)

# Output
print(f"{jam} jam dan {menit} menit = {detik} detik")
print(f"{tahun} tahun dan {bulan} bulan = {hari} hari")
