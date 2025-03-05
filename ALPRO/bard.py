def masuk_area_parkir(nomor_plat):
    # Input waktu masuk
    waktu_masuk = input("Masukkan waktu masuk (HH:MM:SS): ")

    # Cek apakah kendaraan pernah masuk
    if nomor_plat not in kendaraan_masuk:
        kendaraan_masuk.append(nomor_plat)
        waktu_masuk = datetime.strptime(waktu_masuk, "%H:%M:%S")
    else:
        raise Exception("Kendaraan sudah pernah masuk")

def keluar_area_parkir(nomor_plat):
    # Cek apakah kendaraan pernah masuk
    if nomor_plat not in kendaraan_masuk:
        raise Exception("Kendaraan belum pernah masuk")

    # Input waktu keluar
    waktu_keluar = input("Masukkan waktu keluar (HH:MM:SS): ")
    waktu_keluar = datetime.strptime(waktu_keluar, "%H:%M:%S")

    # Hitung biaya parkir
    biaya_parkir = (waktu_keluar - waktu_masuk).total_seconds() / 60 * tarif_parkir

    # Hitung denda
    if waktu_keluar - waktu_masuk > 240:
        biaya_parkir += biaya_parkir * (denda / 100)

    # Tampilkan biaya parkir
    print("Biaya parkir: Rp", biaya_parkir)

    # Input nominal pembayaran
    nominal_pembayaran = input("Masukkan nominal pembayaran: Rp")

    # Cek apakah nominal pembayaran mencukupi
    if int(nominal_pembayaran) < biaya_parkir:
        raise Exception("Nominal pembayaran tidak mencukupi")

    # Hapus kendaraan dari daftar kendaraan masuk
    kendaraan_masuk.remove(nomor_plat)

def menu_utama():
    # Tampilkan menu utama
    print("Menu Utama")
    print("1. Masuk Area Parkir")
    print("2. Keluar Area Parkir")
    print("3. Admin Parkir")

    # Pilih menu
    pilihan = int(input("Pilih menu: "))

    # Lakukan pilihan
    if pilihan == 1:
        masuk_area_parkir(input("Masukkan nomor plat kendaraan: "))
    elif pilihan == 2:
        keluar_area_parkir(input("Masukkan nomor plat kendaraan: "))
    elif pilihan == 3:
        menu_admin()
    else:
        print("Pilihan tidak valid")

def menu_admin():
    # Cek PIN
    pin = input("Masukkan PIN: ")
    if pin != "12345":
        raise Exception("PIN salah")

    # Tampilkan daftar transaksi
    print("Daftar Transaksi")
    for nomor_plat, waktu_masuk, waktu_keluar, biaya_parkir in transaksi:
        print("Nomor plat:", nomor_plat)
        print("Waktu masuk:", waktu_masuk)
        print("Waktu keluar:", waktu_keluar)
        print("Biaya parkir: Rp", biaya_)
