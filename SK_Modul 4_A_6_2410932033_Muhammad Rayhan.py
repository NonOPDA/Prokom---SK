print("Selamat Datang di Arsip Mahasiswa")

#Data Nama, NIM, dan Tahun Masuk
mahasiswa = [
    ["Andi", "2101128046", "2021"],
    ["Budi", "2410931001", "2024"],
    ["Cika", "1910932022", "2019"],
    ["Dodi", "2311132011", "2023"],
    ["Ella", "2310114088", "2023"]
]

while True:
    print("\nMenu Opsi")
    print("1. Data Mahasiswa")
    print("2. Tambah Mahasiswa")
    print("3. Hapus Mahasiswa")
    print("4. Ubah Data Mahasiswa")
    print("5. Keluar")
    pilihan = input("Pilihan menu (1-5): ")

    if pilihan == "1":
        print("\nData Mahasiswa")
        for mhs in mahasiswa:
            print("Nama", mhs[0], "NIM", mhs[1], "Tahun Masuk", mhs[2])
    
    elif pilihan == "2":
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM: ")
        tmasuk = int(input("Masukkan Tahun Masuk: "))
        mahasiswa.append([nama, nim, tmasuk])
        print("Data Ditambahkan")

    elif pilihan == "3":
        hapus = input("Masukkan NIM mahasiswa yang akan dihapus: ")
        for mhs in mahasiswa:
            if mhs[1] == hapus:
                mahasiswa.remove(mhs)
                print("Data berhasil dihapus")
            else:
                print("Data tidak ditemukan")
                break
    
    elif pilihan == "4":
        ubah = input("Masukkan NIM mahasiswa yang akan diubah: ")
        for mhs in mahasiswa:
            if mhs[1] == ubah:
                nama_baru = input("Masukkan Nama baru: ")
                nim_baru = input("Masukkan NIM baru: ")
                tahun_baru = int(input("Masukkan Tahun Masuk baru: "))
                mhs[0] = nama_baru
                mhs[1] = nim_baru
                mhs[2] = tahun_baru
                print("Data mahasiswa berhasil diubah.")
            else:
                print("Data tidak ditemukan")
                break
            
    elif pilihan == "5":
        print("Program Selesai")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1 sampai 5")
    while True:
        lanjut = str(input("Apakah masih ingin melanjutkan program? (y/n): "))
        if lanjut == "y" or lanjut == "Y":
            break
        elif lanjut == "n" or lanjut == "N":
            print("Program Selesai")
            exit()
        else:
            print("Pilihan tidak valid")