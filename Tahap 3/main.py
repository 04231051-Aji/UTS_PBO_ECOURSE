
class Peserta:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim


class Instruktur:
    def __init__(self, nama):
        self.nama = nama


class KelasKursus:
    def __init__(self, nama_kelas, instruktur, kapasitas=5):
        self.nama_kelas = nama_kelas
        self.instruktur = instruktur
        self.__kapasitas = kapasitas
        self.__peserta_list = []

    def daftar(self, peserta):
        if len(self.__peserta_list) >= self.__kapasitas:
            print("[GAGAL] Kelas penuh!")
        else:
            self.__peserta_list.append(peserta)
            print(f"[SUKSES] {peserta.nama} ({peserta.nim}) berhasil daftar")

    def tampilkan_peserta(self):
        print("\n=== DAFTAR PESERTA ===")
        if not self.__peserta_list:
            print("Belum ada peserta.")
        else:
            for i, p in enumerate(self.__peserta_list, start=1):
                print(f"{i}. {p.nama} ({p.nim})")


# VALIDASI
def validasi_nama(nama):
    return nama.isalpha()


def validasi_nim(nim):
    return nim.isdigit() and len(nim) == 8


# MAIN
if __name__ == "__main__":
    instruktur = Instruktur("Pak Budi")
    kelas = KelasKursus("E-Course ITK", instruktur)

    while True:
        print("Kelas Tambahan Program Berorientasi Objek")
        print("\n=== MENU ===")
        print("1. Daftar Peserta")
        print("2. Tampilkan Peserta")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            # 🔹 INPUT NAMA (loop sampai benar)
            while True:
                nama = input("Masukkan Nama: ")
                if validasi_nama(nama):
                    break
                else:
                    print("Masukkan nama anda dengan benar")

            # 🔹 INPUT NIM (loop sampai benar)
            while True:
                nim = input("Masukkan NIM (8 angka): ")
                if validasi_nim(nim):
                    break
                else:
                    print("Masukkan nomor induk mahasiswa anda dengan benar")

            peserta = Peserta(nama, nim)
            kelas.daftar(peserta)

        elif pilihan == "2":
            kelas.tampilkan_peserta()

        elif pilihan == "3":
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid!")