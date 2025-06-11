class rekap_nilai:
    def __init__(self):
        self.data_nilai = {}
    
    def input_nilai(self):
        nim = input("Masukkan NIM Mahasiswa: ")
        if nim not in self.data_nilai:
            self.data_nilai[nim] = {}

        jumlah_nilai = int(input("Jumlah komponen nilai (min 3): "))
        total = 0
        for i in range(jumlah_nilai):
            nama = input(f"Nama komponen {i+1}: ")
            nilai = float(input(f"Nilai {nama}: "))
            self.data_nilai[nim][nama] = nilai
            total += nilai

        mean = total / jumlah_nilai
        self.data_nilai[nim]["rata-rata"] = mean
        self.data_nilai[nim]["huruf"] = self.konversi_nilai(mean)

    def konversi_nilai(self, mean):
        if mean >= 85:
            return "A"
        elif mean >= 70:
            return "B"
        elif mean >= 60:
            return "C"
        elif mean >= 50:
            return "D"
        else:
            return "E"
        
    def rekap_data(self):
        if not self.data_nilai:
            print("Data tidak tersedia")
            return
        print("\nRekap Nilai Mahasiswa")
        for nim, nilai in self.data_nilai.items():
            print(f"\nNIM: {nim}")
            for k,v in nilai.items():
                print(f" {k}: {v}")

    def nilai_edit(self):
        nim = input("Masukkan NIM yang akan diedit: ")
        if nim in self.data_nilai:
            self.input_nilai()
        else:
            print("NIM tidak valid")

    def nilai_hapus(self):
        nim = input("Masukkan NIM yang akan dihapus: ")
        if nim in self.data_nilai:
            del self.data_nilai[nim]
            print("Data nilai dihapus")
        else:
            print("NIM tidak valid")

def main():
    rekap = rekap_nilai()
    while True:
        print("Dashboard Login Data Nilai Mahasiswa")
        user_id = input("Masukkan ID (1 = Dosen, 2 = Mahasiswa): ")
        if user_id == "1":
            while True:
                print("\n1. Input Nilai\n2. Lihat Rekap\n3. Edit Nilai\n4. Hapus Nilai\n5. Logout")
                pilih = input("Pilih menu: ")
                if pilih == '1':
                    rekap.input_nilai()
                elif pilih == '2':
                    rekap.rekap_data()
                elif pilih == '3':
                    rekap.nilai_edit()
                elif pilih == '4':
                    rekap.nilai_hapus()
                elif pilih == '5':
                    break
                else:
                    print("Pilihan tidak valid.")
        elif user_id == "2":
            rekap.rekap_data()
        else:
            print("ID tidak valid")
        
        lanjut = input("\nIngin melanjutkan program? (y/n): ")
        if lanjut.lower() != "y":
            break

if __name__ == "__main__":
    main()