# stars
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

# bilangan ganjil 
 
maximum = int(input(" Please Enter the Maximum Value : "))
Oddtotal = 0
number = 1
 
while number <= maximum:
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number
    number = number + 1

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(maximum, Oddtotal))

# ketupat
size = 7
i = 0

while i < size:

    j = 0

    while j < size:
        if abs(i - size // 2) + abs(j - size // 2) <= size // 2:
            print("",end="")
        else:
            print("",end="")

            j += 1
            print()
            i += 1

# total harga 
print("\n𓆝 𓆟 𓆞 𓆝 TRANSAKSI PENJUALAN𓆝 𓆟 𓆞 𓆝")

product = int(input("\n Jumlah produk  :"))
total = 0

for i in range(product):
    price = int(input("Harga Barang {}:".format(i + 1)))
    total = total + price


print("Total pembayaran : " , total)
    
# pw

print("anda memiliki 3x kesempatan untuk menebak")

percobaan = 0
while True:
    pw = input("Masukkan keyword {}: ".format( percobaan + 1))
    if pw == 'dasprokece' :
        print("\n₊ ⊹₊ ⊹₊ ⊹ PIN is valid ꒰ᐢ. .ᐢ꒱₊˚⊹ ")
        break
    elif percobaan == 2 :
      print("\n₊ ⊹₊ ⊹₊ ⊹ YOU FAIL!!! (◞ ‸ ◟ㆀ) ")
      break
    print("\n₊ ⊹₊ ⊹₊ ⊹ Invalid PIN. (◞ ‸ ◟ㆀ) ")
    percobaan += 1




    




