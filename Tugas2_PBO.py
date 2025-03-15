class Mahasiswa:
    def __init__(self, nama, nim):
        self.__nama = nama
        self.__nim = nim
        self.__matakuliah = []  # List untuk menyimpan mata kuliah

    # Setter
    def set_nama(self, nama):
        self.__nama = nama
    
    def set_nim(self, nim):
        self.__nim = nim
    
    # Getter
    def get_nama(self):
        return self.__nama
    
    def get_nim(self):
        return self.__nim
    
    def tambah_nilai(self, matkul, uts, uas, tugas):
        nilai_akhir = (uts * 0.3) + (uas * 0.4) + (tugas * 0.3)
        self.__matakuliah.append({
            'Mata Kuliah': matkul,
            'UTS': uts,
            'UAS': uas,
            'Tugas': tugas,
            'Akhir': nilai_akhir,
            'Huruf': self.konversi_nilai(nilai_akhir)
        })
    
    def get_nilai(self):
        return self.__matakuliah
    
    def konversi_nilai(self, nilai):
        if nilai >= 85:
            return 'A'
        elif nilai >= 80:
            return 'A-'
        elif nilai >= 75:
            return 'B+'
        elif nilai >= 70:
            return 'B'
        elif nilai >= 65:
            return 'B-'
        elif nilai >= 60:
            return 'C+'
        elif nilai >= 55:
            return 'C'
        elif nilai >= 50:
            return 'D'
        else:
            return 'E'
    
    @staticmethod
    def hitung_ip(matakuliah):
        konversi = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                    'C+': 2.3, 'C': 2.0, 'D': 1.0, 'E': 0.0}
        total_nilai = sum(konversi[mk['Huruf']] for mk in matakuliah)
        return round(total_nilai / len(matakuliah), 2) if matakuliah else 0.0
    
    def tampilkan_nilai(self):
        print(f'Nama: {self.__nama}, NIM: {self.__nim}')
        print('Nilai Mata Kuliah:')
        for mk in self.__matakuliah:
            print(f"  {mk['Mata Kuliah']}: {mk['Akhir']:.2f} ({mk['Huruf']})")
        ip = self.hitung_ip(self.__matakuliah)
        print(f'IP: {ip}\n')

# Implementasi Objek
mahasiswa1 = Mahasiswa("Ahmat Prayoga", "123456789")
mahasiswa1.tambah_nilai("Matematika", 85, 90, 80)
mahasiswa1.tambah_nilai("Pemrograman", 75, 80, 78)
mahasiswa1.tampilkan_nilai()
