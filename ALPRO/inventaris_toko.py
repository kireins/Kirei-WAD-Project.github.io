data_toko= [
    {"nama_produk": "Salmon Belly", "harga": 14000000, "stok": 20},
    {"nama_produk": "Glass Noodle", "harga": 300000, "stok": 30},
    {"nama_produk": "Brisket", "harga": 500000, "stok": 15}
]

total_penjualan = 0

while True:
    print("====== Sistem Inventaris Toko ======")
    print("\nInventaris Awal:")
    for i, product in enumerate(data_toko, 1):
        print(f"{i}. {product['nama_produk']} - Harga: Rp.{product['harga']:,.2f} - Stok: {product['stok']}")


    print("\n====== Transaksi Penjualan ======")
    choice = int(input("\nPilih nomor produk yang akan dijual: "))
    if 1 <= choice <= len(data_toko):
        product = data_toko[choice - 1]
        quantity = int(input(f"Masukkan jumlah {product['nama_produk']} yang akan dijual: "))
        if quantity <= product['stok']:
            product['stok'] -= quantity
            total_harga = quantity * product['harga']
        print(f"\n====== Struk Pembelian====== \nProduk: {product['nama_produk']}\nHarga: Rp.{product['harga']:,.2f}\nJumlah: {quantity}\nTotal Harga: Rp.{total_harga:,.2f}")
        total_penjualan += total_harga
        print(f"\nTotal Penjualan: Rp.{total_penjualan:,.2f}")
    if total_penjualan > 1000000:
        diskon = 0.15
    elif total_penjualan > 500000:
        diskon = 0.1
    else:
        diskon = 0

    if diskon > 0:
     total_diskon = total_penjualan * diskon
     total_penjualan -= total_diskon
    print(f"\nDiskon {diskon * 100}% diberikan. Total Pembayaran setelah Diskon: Rp.{total_penjualan:,.2f}")


    lanjut = input("Apakah Anda ingin melanjutkan penjualan? (yes/no): ")
    if lanjut.lower() != 'yes':
        print("Terima kasih! Program selesai")
        break


        
