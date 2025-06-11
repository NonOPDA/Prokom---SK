#Username dan Password yang benar
username_benar = "RayhanTI"
password_benar = "TI1234"

attempts = 3 #Banyak kesempatan

while attempts > 0: 
    username = input("\nSilakan Masukkan Username Anda: ")
    password = input("Silakan Masukkan Password Anda: ")

    if username == username_benar and password == password_benar:
        print("\nUsername dan Passowrd Anda benar!")
        break
    else:
        attempts -= 1
        print("\nUsername atau Password tidak terdaftar.")

if attempts == 0:
    print("\nAkses Login ditolak. Silakan coba lagi.") 
else:
    print("\nSelamat Datang!")
    #SK Modul 2
    while True:
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
            konfirmasi = input("\nAnda memilih rute penerbangan: \n" + rute + "\nDengan harga: Rp" + harga + ".\nKonfirmasi? (y/n): ")
            if konfirmasi == "y" or konfirmasi == "Y":
                print("\nPemesanan Berhasil!")
                print("Nama Penumpang: ", nama)
                print("Rute Penerbangan: ", rute)
                print("Total Harga: Rp ", harga)
            elif konfirmasi == "n" or konfirmasi == "N":
                print("\nPemesanan Dibatalkan")
            else:
                print("Input Anda tidak sesuai")
            #Penambahan data
            tiket_tambah = input("Apakah Anda ingin memesan tiket lagi? (y/n): ")
            if tiket_tambah == "y" or tiket_tambah == "Y":
                print("\nSilakan masukkan data penumpang berikutnya!")
                continue
            elif tiket_tambah == "n" or tiket_tambah == "N":
                print("\nTerima kasih telah menggunakan layanan kami!")
                break
            else:
                print("Mohon masukkan jawaban yang valid! (y/n)")