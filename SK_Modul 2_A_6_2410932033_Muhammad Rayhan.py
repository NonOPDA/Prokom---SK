#Nama Penumpang dan Penerbangan
nama = input("Silakan Masukkan Nama Penumpang: ")
print("Silakan pilihan rute penerbangan Anda:")
print("1. Padang → Denpasar (Rp 2.500.000)")
print("2. Padang → Jakarta (Transit Batam) (Rp 3.100.000)")
print("3. Padang → Palangkaraya (Rp 2.700.000)")

#Memilih Rute
pilihan = input("Masukkan nomor rute pilihan Anda (1/2/3): ")

if pilihan == "1":
    rute = "Padang → Denpasar"
    harga = "2.500.000"
elif pilihan == "2":
    rute = "Padang → Jakarta (Transit Batam)"
    harga = "3.100.000"
elif pilihan == "3":
    rute = "Padang → Palangkaraya"
    harga = "2.700.000"
else:
    print("Maaf, rute penerbangan Anda tidak tersedia")
    rute = "n/a"
    harga = "n/a"
    exit()

#Konfirmasi
if rute:
    konfirmasi = input(f"\nAnda memilih rute penerbangan: \n{rute} \nDengan harga Rp {harga}. \nKonfirmasi? (y/n): ")
    if konfirmasi == "y" or konfirmasi == "Y":
        print("\nPemesanan Berhasil!")
        print(f"Nama Penumpang: {nama}")
        print(f"Rute Penerbangan: {rute}")
        print(f"Total Harga: Rp {harga}")
    else:
        print("\nPemesanan Dibatalkan")
