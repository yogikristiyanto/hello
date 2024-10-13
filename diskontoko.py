# Fungsi untuk menghitung harga setelah diskon
def hitung_diskon(harga_asli, diskon):
    harga_setelah_diskon = harga_asli - (harga_asli * diskon / 100)
    return harga_setelah_diskon

# Input harga barang
harga_barang = float(input("Masukkan harga barang: Rp "))

# Diskon 20%
diskon = 20

# Hitung harga setelah diskon
harga_diskon = hitung_diskon(harga_barang, diskon)

# Output hasil
print(f"Harga asli barang: Rp {harga_barang}")
print(f"Harga setelah diskon 20%: Rp {harga_diskon:.2f}")
