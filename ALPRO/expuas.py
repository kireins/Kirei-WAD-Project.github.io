import time

# Variabel dan tipe data (5)
data_parkir = {}
tarif_60_detik = 10000
admin_pin = "1234"

# Konstanta (5)
TARIF_DENDA_1 = 0.1
TARIF_DENDA_2 = 0.25

# Fungsi saat kendaraan masuk area parkir (5)
def masuk_parkir():
    try:
        nomor_plat = input("\nMasukkan nomor/plat kendaraan: ")
        waktu_masuk = time.time()
        gerbang_masuk_terbuka()
        data_parkir[nomor_plat] = {'waktu_masuk': waktu_masuk}
    except Exception as e:
        print(f"\nError: {e}")


# Fungsi saat kendaraan ingin keluar area parkir (5)
def keluar_parkir():
    try:
        nomor_plat = input("\nMasukkan nomor/plat kendaraan: ")
        
        if nomor_plat not in data_parkir:
            raise ValueError("\nKendaraan tidak tercatat masuk area parkir.")
        
        waktu_keluar = time.time()
        gerbang_keluar_terbuka()
        lama_parkir_detik = hitung_lama_parkir(data_parkir[nomor_plat]['waktu_masuk'], waktu_keluar)
        biaya_parkir = hitung_harga_parkir(lama_parkir_detik)
        print(f"\nBiaya parkir: Rp {biaya_parkir}")
        nominal_pembayaran = input("\nMasukkan nominal pembayaran: Rp  ")
        pembayaran_parkir(biaya_parkir, nominal_pembayaran)
    except ValueError as ve:
        print(f"\nError: {ve}")
    except Exception as e:
        print(f"\nError: {e}")

# Fungsi menampilkan data kendaraan di area parkir (5)
def tampilkan_data_parkir():
    try:
        print("\nDaftar Kendaraan yang Parkir:")
        for nomor_plat in data_parkir:
            print(f"\nNomor Kendaraan: {nomor_plat}")
    except Exception as e:
        print(f"\nError: {e}")


# Fungsi menghitung lama parkir (5)
def hitung_lama_parkir(waktu_masuk, waktu_keluar):
    lama_parkir_detik = waktu_keluar - waktu_masuk
    if lama_parkir_detik < 60:
        lama_parkir_detik = 60
    elif lama_parkir_detik > 240:
        lama_parkir_detik = 240
    return lama_parkir_detik

# Fungsi menghitung biaya waktu (5)
def hitung_harga_parkir(lama_parkir_detik):
    biaya_parkir = (lama_parkir_detik // 60) * tarif_60_detik
    if lama_parkir_detik > 240:
        denda = biaya_parkir * TARIF_DENDA_1
        biaya_parkir += denda
    elif lama_parkir_detik > 360:
        denda = biaya_parkir * TARIF_DENDA_2
        biaya_parkir += denda
    return biaya_parkir

# Fungsi saat menentukan pembayaran (5)
def pembayaran_parkir(biaya_parkir, nominal_pembayaran):
    if float(nominal_pembayaran) >= biaya_parkir:
        print("\nPembayaran diterima. Terima kasih!")
    else:
        print("\nPembayaran kurang. Transaksi dibatalkan.")

# Fungsi saat gerbang masuk terbuka (5)
def gerbang_masuk_terbuka():
    print("\nSilahkan masuk")

# Fungsi saat gerbang keluar terbuka (5)
def gerbang_keluar_terbuka():
    print("\nTerima Kasih")

# Fungsi untuk masuk ke admin parkir (5)
def admin_parkir():
    while True:
        pin_input = input("\nMasukkan PIN Admin Parkir: ")

        if pin_input == admin_pin:
            print("\n1. Cetak Seluruh Transaksi Parkir")
            print("2. Tampilkan Daftar Kendaraan yang Parkir")
            print("3. Kembali ke Menu Utama")

            choice = input("\nPilih menu: ")

            if choice == "1":
                cetak_transaksi()
            elif choice == "2":
                tampilkan_data_parkir()
            elif choice == "3":
                break  # Exit the admin menu loop and go back to the main menu
            else:
                print("\nPilihan tidak valid.")
        else:
            print("\nPIN Admin Parkir salah.")


# Fungsi untuk mencetak daftar transaksi (5)
def cetak_transaksi():
    print("\nTransaksi Parkir:")
    for nomor_plat, data in data_parkir.items():
        print(f"\nNomor Plat: {nomor_plat}, Waktu Masuk: {time.ctime(data['waktu_masuk'])}")

# Percabangan dan pemanggilan (5)

while True:
    print("\n1. Masuk Area Parkir")
    print("2. Keluar Area Parkir")
    print("3. Admin Parkir")
    print("4. Keluar")

    choice = input("\nPilih menu: ")

    try:
        if choice == "1":
            masuk_parkir()
        elif choice == "2":
            keluar_parkir()
        elif choice == "3":
            admin_parkir()
        elif choice == "4":
            break
        else:
            raise ValueError("Pilihan tidak valid. Silahkan coba lagi.")
    except ValueError as ve:
        print(f"\nError: {ve}")
    except Exception as e:
        print(f"\nError: {e}")
