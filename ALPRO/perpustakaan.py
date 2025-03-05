judul1 =  "Python Programming"
stok_buku1 = 5

judul2 = "Introduction to Science"
stok_buku2 = 7  

judul3= "History of World"
stok_buku3 = 3
pilih = 0
while True:
    print("Daftar buku yang terserdia:")
    print(f"1.{judul1} ({stok_buku1} tersedia)")
    print(f"2.{judul2} ({stok_buku2} tersedia)")
    print(f"3.{judul3} ({stok_buku3} tersedia)")

    pilihmenu = int(input("Pilih buku yang ingin di pinjam atau ketik 'selesai' untuk keluar (1-3):"))

    if pilihmenu == 1:
        print("Berhasil meminjam", judul1)
        break
    elif pilihmenu == 2:
        print("Berhasil meminjam", judul2)
        break
    elif pilihmenu == 3:
       print("Berhasil meminjam", judul3)
       break

    else:
        print("Buku tidak tersedia")
        exit()


        


 