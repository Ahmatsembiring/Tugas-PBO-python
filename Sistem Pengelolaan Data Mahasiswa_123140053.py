import sys  # mengakses argumen command-line
import os  # Memeriksa keberadaaan file
import csv  # Digunakan untuk membaca dan menulis data dalam format CSV.
import json  # Digunakan untuk membaca dan menulis data dalam format JSON.

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n==== SISTEM PENGELOLAAN DATA MAHASISWA ====")
    print("-" * 40)
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Semua Mahasiswa")
    print("3. Cari Mahasiswa Berdasarkan NIM")
    print("4. Edit Data Mahasiswa")
    print("5. Hapus Data Mahasiswa")
    print("6. Simpan ke File")
    print("7. Sorting Data Mahasiswa")
    print("8. Keluar")
    print("-" * 40)

# Fungsi untuk menambahkan mahasiswa
def tambah_mahasiswa(mahasiswa):
    try:
        nim = input("Masukkan NIM: ")
        if nim in mahasiswa:
            print("NIM sudah ada!")
            return
        nama = input("Masukkan Nama: ")
        nilai = float(input("Masukkan Nilai: "))
        mahasiswa[nim] = {"nama": nama, "nilai": nilai}
        print("Mahasiswa berhasil ditambahkan!")
    except ValueError:
        print("Input nilai tidak valid. Harap masukkan angka.")

# Fungsi untuk menampilkan semua mahasiswa
def tampilkan_semua_mahasiswa(mahasiswa):
    if not mahasiswa:
        print("Tidak ada data mahasiswa.")
        return
    print("\n==== DATA MAHASISWA ====")
    print("NIM      | Nama                | Nilai")
    print("-" * 40)
    for nim, data in mahasiswa.items():
        print(f"{nim}  | {data['nama']}   | {data['nilai']}")
    print("-" * 40)

# Fungsi untuk mencari mahasiswa berdasarkan NIM
def cari_mahasiswa(mahasiswa):
    nim = input("Masukkan NIM yang ingin dicari: ")
    if nim in mahasiswa:
        print("\n==== DATA MAHASISWA ====")
        print("-" * 40)
        print(f"NIM: {nim}")
        print(f"Nama: {mahasiswa[nim]['nama']}")
        print(f"Nilai: {mahasiswa[nim]['nilai']}")
        print("-" * 40)
    else:
        print("Mahasiswa tidak ditemukan!")

# Fungsi untuk mengedit data mahasiswa
def edit_mahasiswa(mahasiswa):
    nim = input("Masukkan NIM yang ingin diedit: ")
    if nim in mahasiswa:
        try:
            nama_baru = input("Nama baru (kosongkan jika tidak ingin mengubah): ")
            nilai_baru = input("Nilai baru (kosongkan jika tidak ingin mengubah): ")
            if nama_baru:
                mahasiswa[nim]['nama'] = nama_baru
            if nilai_baru:
                mahasiswa[nim]['nilai'] = float(nilai_baru)
            print("Data berhasil diperbarui!")
        except ValueError:
            print("Input nilai tidak valid. Harap masukkan angka.")
    else:
        print("Mahasiswa tidak ditemukan!")

# Fungsi untuk menghapus mahasiswa
def hapus_mahasiswa(mahasiswa):
    nim = input("Masukkan NIM yang ingin dihapus: ")
    if nim in mahasiswa:
        del mahasiswa[nim]
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("Mahasiswa tidak ditemukan!")

# Fungsi untuk menyimpan data ke file
def simpan_ke_file(mahasiswa, filename="mahasiswa"):
    try:
        # Menulis data dari dictionary mahasiswa ke file CSV menggunakan csv.DictWriter
        format_file = input("Pilih format file (csv/json): ").lower()
        if format_file == 'csv':
            with open(f"{filename}.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["NIM", "Nama", "Nilai"])
                for nim, data in mahasiswa.items():
                    writer.writerow([nim, data['nama'], data['nilai']])
            print(f"Data mahasiswa telah disimpan dalam file '{filename}.csv'")
        elif format_file == 'json':
            with open(f"{filename}.json", 'w') as file:
                json.dump(mahasiswa, file, indent=4)
            print(f"Data mahasiswa telah disimpan dalam file '{filename}.json'")
        else:
            print("Format file tidak valid.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan file: {e}")

# Fungsi untuk membaca data dari file
def baca_dari_file(filename="mahasiswa"):
    mahasiswa = {}  #
    try:
        format_file = input("Pilih format file (csv/json): ").lower()
        if format_file == 'csv':
            if os.path.exists(f"{filename}.csv"):
                with open(f"{filename}.csv", 'r') as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip header
                    for row in reader:
                        nim, nama, nilai = row
                        mahasiswa[nim] = {"nama": nama, "nilai": float(nilai)}  # nenambahkan file ke dictonory
        elif format_file == 'json':
            if os.path.exists(f"{filename}.json"):
                with open(f"{filename}.json", 'r') as file:
                    mahasiswa = json.load(file)
        else:
            print("Format file tidak valid.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")
    return mahasiswa

# Fungsi untuk sorting data mahasiswa
def sorting_mahasiswa(mahasiswa):
    try:
        print("\n==== SORTING DATA MAHASISWA ====")
        print("-" * 40)
        print("1. Sorting berdasarkan NIM")
        print("2. Sorting berdasarkan Nilai Tertinggi")
        print("-" * 40)
        pilihan = input("Pilihan: ")
        if pilihan == '1':
            sorted_mahasiswa = dict(sorted(mahasiswa.items()))
        elif pilihan == '2':
            sorted_mahasiswa = dict(sorted(mahasiswa.items(), key=lambda item: item[1]['nilai'], reverse=True))
        else:
            print("Pilihan tidak valid.")
            return
        tampilkan_semua_mahasiswa(sorted_mahasiswa)
    except Exception as e:
        print(f"Terjadi kesalahan saat sorting data: {e}")

# Fungsi utama
def main():
    mahasiswa = baca_dari_file()

    while True:
        tampilkan_menu()
        pilihan = input("Pilihan: ")

        if pilihan == '1':
            tambah_mahasiswa(mahasiswa)
        elif pilihan == '2':
            tampilkan_semua_mahasiswa(mahasiswa)
        elif pilihan == '3':
            cari_mahasiswa(mahasiswa)
        elif pilihan == '4':
            edit_mahasiswa(mahasiswa)
        elif pilihan == '5':
            hapus_mahasiswa(mahasiswa)
        elif pilihan == '6':
            simpan_ke_file(mahasiswa)
        elif pilihan == '7':
            sorting_mahasiswa(mahasiswa)
        elif pilihan == '8':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()