inventaris = [
    {"produk": "Produk 1", "harga": 100000, "stok": 20},
    {"produk": "Produk 2", "harga": 500000, "stok": 30},
    {"produk": "Produk 3", "harga": 20000, "stok": 15}
]
penjualanan = 0
def tampilkan():
    print("Sistem Inventaris Toko")
    print("Inventaris Awal:")
    for i, produk in enumerate(inventaris, 1):
        print(f"{i}. {produk['produk']} Harga: Rp.{produk['harga']} Stok: {produk['stok']}")

def penjualan(menu):
    if 1 <= menu <= len(inventaris):
        produk = inventaris[menu- 1]
        jumlahbarang = int(input(f"Masukkan jumlah {produk['produk']} yang akan dijual: "))
        if jumlahbarang <= produk['stok']:
            produk['stok'] -= jumlahbarang
            total_harga = jumlahbarang * produk['harga']
            print("Struk Pembelian:")
            print(f"Produk: {produk['produk']} Harga: Rp.{produk['harga']} Jumlah: {jumlahbarang} Total Harga: Rp.{total_harga}")
            return total_harga
        else:
            print("Stok habis.")
    else:
        print("Pilihan salah.")
while True:
    tampilkan()
    print("Transaksi Penjualan")
    menu = int(input("Pilih nomor produk yang akan dijual: "))
    penjualanan += penjualan(menu)
    if penjualanan > 1000000:
        diskon = 0.15
    elif penjualanan > 500000:
        diskon = 0.1
    else:
        diskon = 0
    if diskon > 0:
        penjualanan -= penjualanan * diskon
    print(f"Diskon {diskon*100}% diberikan. Total Pembayaran setelah Diskon: Rp.{penjualanan}")
    melanjutkanPenjualanan = input("Apakah Anda ingin melanjutkan penjualan?(iya/tidak): ")
    if melanjutkanPenjualanan.lower() != 'iya':
        print("Terima kasih! Program selesai.")
        exit()
