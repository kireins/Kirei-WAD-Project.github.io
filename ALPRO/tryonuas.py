import time #Gunanya untuk mengimpor modul time dari pustaka standar Python.
# Modul ini menyediakan sejumlah fungsi terkait waktu dan penanganan waktu dalam berbagai konteks.

#membuat list kosong untuk data parkir.Gunanya untuk menyimpan dan mengelola data dalam bentuk urutan yang dapat diubah (mutable).
#  agar dapat melakukan berbagai operasi seperti menambahkan, menghapus, atau mengakses elemen-elemen dalam daftar tersebut.
data_parkir = {}

#variabel untuk tarif per 60 detiknya. Ini termasuk variabel global yang di mana dapat diakses dari seluruh bagian dalam program, 
# termasuk di dalam fungsi-fungsi yang didefinisikan di dalam program tersebut.
tarif_60_detik = 10000

#pin pada admin. Untuk akses saat program di jalankan dan memilih menu admin parkir. 
# Hanya admin yang mengetahui pin admin. dan setelah di lakukan pengecekan apakah ini benar atau salah akan di proses print error nya.
admin_pin = "1234" 

#fungsi 1 untuk memproses data saat kendaraan masuk area parkir. 
# Data yang di masukkan oleh pengguna akan di simpan dalam list data_parkir. 
def masuk_parkir():
    # ini adalah sebuah operasi yang di gunakan untuk meminta plat nomor kendaraan kepada user. 
    # dengan waktu yang bersamaan ini adalah sebuah operasi untuk mencatat waktu secara realtime kapan kendaraan masuk dan juga menjalankan fungsi buka gerbang,
    # yang dimana isinya sebuah print untuk memberi tahu user sudah masuk.
    nomor_plat = input("Masukkan nomor/plat kendaraan: ")
    waktu_masuk = time.time()
    gerbang_masuk_terbuka() # pemanggilan fungsi buka gerbang.
    #Karena kita telah membuat dictionary kosong data_parkir, sekarang kita akan memasukan data plat nomor ke dalam dictionary.
    data_parkir[nomor_plat] = {'waktu_masuk': waktu_masuk}

#fungsi 2 saat kendaraan ingin keluar area parkir.Disini berisikian logic dan operasi untuk memproses menu 'keluar parkir'. 
    # yang di mana user di minta input nomor parkir yang telah di buat. lalu terdapat sebuah percabangan untuk memastikan apakah plat yang telah di masukkan sudah benar atau belum.
def keluar_parkir():
    try: #blok try dan except digunakan untuk menangani pengecualian jika ada situasi tidak terduga atau kesalahan yang mungkin terjadi selama eksekusi program. 
    #menginput kembali plat kendaraan sesuai data awal
        nomor_plat = input("Masukkan nomor/plat kendaraan: ")
        
        #jika plat nomor tidak sesuai dengan data maka akan error
        if nomor_plat not in data_parkir:
            raise ValueError("\nKendaraan tidak tercatat masuk area parkir.")
        # ValueError adalah pengecualian yang dapat terjadi ketika ada masalah dengan tipe atau nilai suatu objek.
        
        waktu_keluar = time.time()
        gerbang_keluar_terbuka()

        #untuk lama parkir per detik nya, kita akan memanggil fungsi hitung lama yang di minta untuk menunjukkan list data parkir yang di dalamnya terdapat value nomor plat, waktu masuk, dan waktu keluar. 
        lama_parkir_detik = hitung_lama_parkir(data_parkir[nomor_plat]['waktu_masuk'], waktu_keluar)

        #untuk biaya parkir, kita akan memanggil fungsi hitung harga parkir, lama parkir agar dapat di print sesuai dengan data yang telah di proses dan di simpan.
        biaya_parkir = hitung_harga_parkir(lama_parkir_detik)

        #menampilkan biaya parkir kita hanya perlu mencetak biaya parkir dan agar variable biaya parkir dapat di panggil, 
        # kita menggunakan  menggunakan format f-string untuk menyisipkan nilai variabel ke dalam string.
        print(f"Biaya parkir: Rp {biaya_parkir}")

        #menginput nominal pembayaran
        nominal_pembayaran = input("Masukkan nominal pembayaran: Rp  ")

        # pemanggilan fungsi pembayaran agar pembayaran dapat di proses.
        pembayaran_parkir(biaya_parkir, nominal_pembayaran)
    except ValueError as ve:
        print(f"\nError: {ve}")

#fungsi 3 menampilkan data kendaraan di area parkir. disini menggunakan perulangan for untuk mengeksekusi serangkaian pernyataan secara berulang berdasarkan elemen-elemen dalam suatu urutan atau struktur data.
def tampilkan_data_parkir():
    print("Daftar Kendaraan yang Parkir:")
    for nomor_plat in data_parkir:
        print(f"Nomor Kendaraan: {nomor_plat}")

#fungsi 4 menghitung lama parkir yang dimana terdiri dari operasi pengirangan antara waktu keluar-masuk, 
# dan perulangan untuk menghitung durasi parkir dan di kembalikan ke variable lama parkir
def hitung_lama_parkir(waktu_masuk, waktu_keluar):
    lama_parkir_detik = waktu_keluar - waktu_masuk

    # percabangan untuk pembulatan waktu parkir per 60 detik
    if lama_parkir_detik < 60:
        lama_parkir_detik = 60
    elif lama_parkir_detik > 240:
        lama_parkir_detik = 240

    return lama_parkir_detik

#fungsi 5 menghitung biaya waktu, terdiri dari pengoperasian biaya parkir yang dimana durasi parkir dibagi dengan per 60 detik
# dan di kali oleh variable 60 detik yang berjumlah 10000. 
def hitung_harga_parkir(lama_parkir_detik):
    biaya_parkir = (lama_parkir_detik // 60) * tarif_60_detik

    #perulangan untuk menentukan denda parkir saat waktu melebihi batas maksimal,
    # jika lama parkir lebih dari 240 detik, maka denda biaya parkir di kali 0.1. jika lebih dari 360 detik di denda 25%
    if lama_parkir_detik > 240:
        denda = biaya_parkir * 0.1
        biaya_parkir += denda
    elif lama_parkir_detik > 360:
        denda = biaya_parkir * 0.25
        biaya_parkir += denda

    return biaya_parkir
# setelah di hitung, pengoperasian di kembalikan ke variable biaya parkir. 

#fungsi saat menentukan pembayaran. untuk menghitung apakah uang yang di beri telah mencukupi atau tidak di sini di buat pengoperasian dengan
#  pengulangan if-else. yang dimana jika nominal yang di berikan sesuai maka pembayaran berhasil, lalu pengendara boleh keluar.
def pembayaran_parkir(biaya_parkir, nominal_pembayaran):
    if float(nominal_pembayaran) >= biaya_parkir:
        print("Pembayaran diterima. Terima kasih!")
    #jika nominal yg dibayar kurang dari harga parkir maka error, dan akan kembali ke menu awal.
    else:
        print("Pembayaran kurang. Transaksi dibatalkan.")

#fungsi saat gerbang masuk terbuka
def gerbang_masuk_terbuka():
    print("Silahkan masuk")

#fungsi saat gerbang keluar terbuka
def gerbang_keluar_terbuka():
    print("Terima Kasih")

#fungsi untuk masuk ke admin parkir, user di minta untuk memasukkan pin admin yang sesuai dan jika salah maka akan keluar error 
# dan user di minta untuk mengulang PIN. 
def admin_parkir():
    while True: # Di gunakan while true agar terus berjalan selama kondisi yang diberikan selalu bernilai benar (True). 
    #input pin admin, pin telah di buat di variable global. 
        pin_input = input("Masukkan PIN Admin Parkir: ")
    
        if pin_input == admin_pin:
            #opsi pilihan pada sesi admin
            print("1. Cetak Seluruh Transaksi Parkir")
            print("2. Tampilkan Daftar Kendaraan yang Parkir")
            print("3. Kembali ke Menu Utama")
            
            choice = input("Pilih menu: ")
            
            if choice == "1":
                cetak_transaki()
            elif choice == "2":
                tampilkan_data_parkir()
            elif choice == "3":
                break  #Untuk menghentikan loop tak terbatas,kita dapat menggunakan 'break' ketika suatu kondisi tertentu terpenuhi. 
                       # keluar dari menu admin dan akan kembali ke menu utama.
            else:
                print("\nPilihan tidak valid.")
        else:
            print("\nPIN Admin Parkir salah.")

#fungsi untuk mencetak daftar transaksi, yang terdiri atas perulangan for dimana akan di ambil nomor plat dari data parkir 
# dan akan mencetak waktu masuknya menggunakan modul 'time'.
def cetak_transaki():
    print("Transaksi Parkir:")
    for nomor_plat, data in data_parkir.items():
        print(f"Nomor Plat: {nomor_plat}, Waktu Masuk: {time.ctime(data['waktu_masuk'])}")

#ini adalah menu yang menampilkan opsi menu yang didalamnya terdapat operasi percabangan untuk 
# mengambil sebuah keputusan apakah user memilih menu 1-4 dan menjalankan setiap operasi nya dengan memanggil fungsi" yang telah di buat di atas.
while True:
    print("1. Masuk Area Parkir")
    print("2. Keluar Area Parkir")
    print("3. Admin Parkir")
    print("4. Keluar")

    choice = input("Pilih menu: ")

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