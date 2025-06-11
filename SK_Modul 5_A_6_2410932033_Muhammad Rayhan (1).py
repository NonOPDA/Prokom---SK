class Mahasiswa:
    def __init__(self, nim, nama, tugas, uts, uas):
        self.nim = nim
        self.nama = nama
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.rata2 = (tugas + uts + uas) / 3
        self.huruf = self.konversi_nilai()

    def konversi_nilai(self):
        if self.rata2 >= 85:
            return "A"
        elif self.rata2 >= 70:
            return "B"
        elif self.rata2 >= 60:
            return "C"
        elif self.rata2 >= 50:
            return "D"
        else:
            return "E"

    def tampilkan_data(self):
        print(f"NIM     : {self.nim}")
        print(f"Nama    : {self.nama}")
        print(f"Tugas   : {self.tugas}")
        print(f"UTS     : {self.uts}")
        print(f"UAS     : {self.uas}")
        print(f"Rata2   : {self.rata2:.2f}")
        print(f"Nilai   : {self.huruf}\n")

class RekapNilai:
    def __init__(self):
        self.data = {}

    def tambah_data(self):
        nim = input("Masukkan NIM mahasiswa: ")
        nama = input("Masukkan Nama mahasiswa: ")
        tugas = float(input("Masukkan nilai Tugas: "))
        uts = float(input("Masukkan nilai UTS: "))
        uas = float(input("Masukkan nilai UAS: "))
        mhs = Mahasiswa(nim, nama, tugas, uts, uas)
        self.data[nim] = mhs
        print("Data berhasil ditambahkan")

    def tampilkan_semua(self):
        if not self.data:
            print("Belum ada data.")
        else:
            for mhs in self.data.values():
                mhs.tampilkan_data()

    def ubah_data(self):
        nim = input("Masukkan NIM yang ingin diubah: ")
        if nim in self.data:
            self.tambah_data()  # Overwrite data lama
        else:
            print("Data tidak ditemukan.")

    def hapus_data(self):
        nim = input("Masukkan NIM yang ingin dihapus: ")
        if nim in self.data:
            del self.data[nim]
            print("Data berhasil dihapus.")
        else:
            print("Data tidak ditemukan.")


def main():
    rekap = RekapNilai()
    while True:
        print("=== LOGIN ===")
        print("1. Dosen")
        print("2. Mahasiswa")
        print("0. Keluar")
        user = input("Masukkan ID: ")

        if user == "1":
            while True:
                print("\n--- Menu Dosen ---")
                print("1. Tambah Nilai")
                print("2. Lihat Rekapan")
                print("3. Ubah Data")
                print("4. Hapus Data")
                print("0. Logout")
                pilihan = input("Pilih menu: ")

                if pilihan == "1":
                    rekap.tambah_data()
                elif pilihan == "2":
                    rekap.tampilkan_semua()
                elif pilihan == "3":
                    rekap.ubah_data()
                elif pilihan == "4":
                    rekap.hapus_data()
                elif pilihan == "0":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif user == "2":
            print("\n--- Rekapan Nilai ---")
            rekap.tampilkan_semua()

        elif user == "0":
            print("Program selesai.")
            break

        else:
            print("ID tidak dikenali.")


if __name__ == "__main__":
    main()
