buku1 =  "Python Programming"
stok_buku1 = 5

buku2 = "Introduction to Science"
stok_buku2 = 7  

buku3 = "History of World"
stok_buku3 = 3

def show_stock():
    print("\nStok Buku di Perpumin:")
    print(f"1. {buku1}: {stok_buku1} buku")
    print(f"2. {buku2}: {stok_buku2} buku")
    print(f"3. {buku3}: {stok_buku3} buku")

def book_rent():
    show_stock()
    choose = int(input("\nPilih buku yang akan di pinjam (1-3): "))

    if choose == 1:
        bookname = buku1
        stock = stok_buku1
    elif choose == 2:
        bookname = buku2
        stock = stok_buku2
    elif choose == 3:
        bookname = buku3
        stock = stok_buku3
    else:
        print("Buku tidak tersedia")
        return
    
    if stock > 0:
        stock -= 1
        print(f"Buku {bookname} berhasil di pinjam.")
    else:
        print(f"Stock buku '{bookname} tidak tersedia")

while True:
    print("\n₊ ⊹₊ ⊹₊ ⊹  Selamat datang di perpus mini ꒰ᐢ. .ᐢ꒱₊˚⊹ ")
    print("1. Tampilkan Stok Buku")
    print("2. Pinjam Buku")
    print("3. Keluar")

    menu= int(input("\nMasukkan pilihan menu (1-3): "))

    if menu == 1:
        show_stock()
    elif menu == 2:
        book_rent()
    elif menu == 3:
        print("Terima kasih telah berkunjung!")
        break
    else:
        print("Menu tidak tersedia")
    
