import sys
import os
import json
import csv

# Inisialisasi dictionary untuk menyimpan data mahasiswa
mahasiswa = {}

# Fungsi untuk membaca data dari file JSON
def baca_dari_file_json(nama_file="mahasiswa.json"):
    global mahasiswa
    try:
        if os.path.exists(nama_file):
            with open(nama_file, 'r') as file:
                mahasiswa = json.load(file)
            print(f"Data berhasil dimuat dari file '{nama_file}'")
        else:
            print(f"File '{nama_file}' tidak ditemukan. Memulai dengan database kosong.")
    except Exception as e:
        print(f"Error saat membaca file JSON: {e}")

# Fungsi untuk membaca data dari file CSV
def baca_dari_file_csv(nama_file="mahasiswa.csv"):
    global mahasiswa
    try:
        if os.path.exists(nama_file):
            with open(nama_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    nim = row['NIM']
                    mahasiswa[nim] = {"nama": row['Nama'], "nilai": int(row['Nilai'])}
            print(f"Data berhasil dimuat dari file '{nama_file}'")
        else:
            print(f"File '{nama_file}' tidak ditemukan. Memulai dengan database kosong.")
    except Exception as e:
        print(f"Error saat membaca file CSV: {e}")

# Fungsi untuk menyimpan data ke file JSON
def simpan_ke_file_json(nama_file="mahasiswa.json"):
    try:
        with open(nama_file, 'w') as file:
            json.dump(mahasiswa, file, indent=4)
        print(f"Data mahasiswa telah disimpan dalam file '{nama_file}'")
    except Exception as e:
        print(f"Error saat menyimpan file JSON: {e}")

# Fungsi untuk menyimpan data ke file CSV
def simpan_ke_file_csv(nama_file="mahasiswa.csv"):
    try:
        with open(nama_file, 'w', newline='') as file:
            fieldnames = ['NIM', 'Nama', 'Nilai']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for nim, data in mahasiswa.items():
                writer.writerow({'NIM': nim, 'Nama': data['nama'], 'Nilai': data['nilai']})
        print(f"Data mahasiswa telah disimpan dalam file '{nama_file}'")
    except Exception as e:
        print(f"Error saat menyimpan file CSV: {e}")

# Fungsi untuk menambah mahasiswa
def tambah_mahasiswa():
    try:
        nim = input("Masukkan NIM: ")
        if nim in mahasiswa:
            print(f"Mahasiswa dengan NIM {nim} sudah ada dalam database!")
            return
        
        nama = input("Masukkan Nama: ")
        nilai_input = input("Masukkan Nilai: ")
        
        # Validasi nilai
        try:
            nilai = int(nilai_input)
            if nilai < 0 or nilai > 100:
                print("Nilai harus di antara 0-100!")
                return
        except ValueError:
            print("Nilai harus berupa angka!")
            return
        
        # Tambahkan ke dictionary
        mahasiswa[nim] = {"nama": nama, "nilai": nilai}
        print("Mahasiswa berhasil ditambahkan!")
    except Exception as e:
        print(f"Error: {e}")

# Fungsi untuk menampilkan semua mahasiswa
def tampilkan_semua_mahasiswa():
    if not mahasiswa:
        print("Database mahasiswa kosong!")
        return
    
    print("\n==== DATA MAHASISWA ====")
    print("NIM      | Nama                | Nilai")
    print("-" * 40)
    
    for nim, data in mahasiswa.items():
        print(f"{nim:<9}| {data['nama']:<20}| {data['nilai']}")
    print()

# Fungsi untuk mencari mahasiswa berdasarkan NIM
def cari_mahasiswa():
    nim = input("Masukkan NIM yang ingin dicari: ")
    if nim in mahasiswa:
        print("Data Mahasiswa:")
        print(f"NIM: {nim}")
        print(f"Nama: {mahasiswa[nim]['nama']}")
        print(f"Nilai: {mahasiswa[nim]['nilai']}")
    else:
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan!")

# Fungsi untuk mengedit data mahasiswa
def edit_mahasiswa():
    nim = input("Masukkan NIM yang ingin diedit: ")
    if nim in mahasiswa:
        nama_baru = input("Nama baru (kosongkan jika tidak ingin mengubah): ")
        nilai_baru = input("Nilai baru (kosongkan jika tidak ingin mengubah): ")
        
        if nama_baru:
            mahasiswa[nim]["nama"] = nama_baru
        
        if nilai_baru:
            try:
                nilai = int(nilai_baru)
                if nilai < 0 or nilai > 100:
                    print("Nilai harus di antara 0-100!")
                    return
                mahasiswa[nim]["nilai"] = nilai
            except ValueError:
                print("Nilai harus berupa angka!")
                return
        
        print("Data berhasil diperbarui!")
    else:
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan!")

# Fungsi untuk menghapus data mahasiswa
def hapus_mahasiswa():
    nim = input("Masukkan NIM yang ingin dihapus: ")
    if nim in mahasiswa:
        del mahasiswa[nim]
        print("Data mahasiswa berhasil dihapus.")
    else:
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan!")

# Fungsi untuk mengurutkan data mahasiswa
def urutkan_mahasiswa():
    if not mahasiswa:
        print("Database mahasiswa kosong!")
        return
    
    print("\nUrutkan berdasarkan:")
    print("1. NIM")
    print("2. Nilai Tertinggi")
    try:
        pilihan = int(input("Pilihan: "))
        
        if pilihan == 1:
            tampilkan_mahasiswa_urut_nim()
        elif pilihan == 2:
            tampilkan_mahasiswa_urut_nilai()
        else:
            print("Pilihan tidak valid!")
    except ValueError:
        print("Masukkan pilihan yang benar (angka)!")

# Fungsi untuk menampilkan mahasiswa urut berdasarkan NIM
def tampilkan_mahasiswa_urut_nim():
    print("\n==== DATA MAHASISWA (URUT BERDASARKAN NIM) ====")
    print("NIM      | Nama                | Nilai")
    print("-" * 40)
    
    for nim in sorted(mahasiswa.keys()):
        data = mahasiswa[nim]
        print(f"{nim:<9}| {data['nama']:<20}| {data['nilai']}")
    print()

# Fungsi untuk menampilkan mahasiswa urut berdasarkan nilai
def tampilkan_mahasiswa_urut_nilai():
    print("\n==== DATA MAHASISWA (URUT BERDASARKAN NILAI) ====")
    print("NIM      | Nama                | Nilai")
    print("-" * 40)
    
    # Urutkan berdasarkan nilai (tertinggi ke terendah)
    nim_terurut = sorted(mahasiswa.keys(), key=lambda x: mahasiswa[x]['nilai'], reverse=True)
    
    for nim in nim_terurut:
        data = mahasiswa[nim]
        print(f"{nim:<9}| {data['nama']:<20}| {data['nilai']}")
    print()

# Fungsi utama untuk menampilkan menu
def tampilkan_menu():
    print("\n==== SISTEM PENGELOLAAN DATA MAHASISWA ====")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Semua Mahasiswa")
    print("3. Cari Mahasiswa Berdasarkan NIM")
    print("4. Edit Data Mahasiswa")
    print("5. Hapus Data Mahasiswa")
    print("6. Simpan ke File JSON")
    print("7. Simpan ke File CSV")
    print("8. Urutkan Data Mahasiswa")
    print("9. Keluar")
    return input("Pilihan: ")

# Program utama
def main():
    # Cek apakah file data ada, jika ada, muat datanya
    baca_dari_file_json()
    baca_dari_file_csv()
    
    while True:
        pilihan = tampilkan_menu()
        
        if pilihan == '1':
            tambah_mahasiswa()
        elif pilihan == '2':
            tampilkan_semua_mahasiswa()
        elif pilihan == '3':
            cari_mahasiswa()
        elif pilihan == '4':
            edit_mahasiswa()
        elif pilihan == '5':
            hapus_mahasiswa()
        elif pilihan == '6':
            simpan_ke_file_json()
        elif pilihan == '7':
            simpan_ke_file_csv()
        elif pilihan == '8':
            urutkan_mahasiswa()
        elif pilihan == '9':
            simpan_ke_file_json()  # Simpan data sebelum keluar
            simpan_ke_file_csv()   # Simpan data sebelum keluar
            print("Terima kasih telah menggunakan sistem ini!")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

# Jika program dijalankan dengan command-line arguments
if __name__ == "__main__":
    # Jika ada argumen command line
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        # Muat data terlebih dahulu
        baca_dari_file_json()
        baca_dari_file_csv()
        
        if command == "tampil" or command == "show":
            tampilkan_semua_mahasiswa()
        elif command == "cari" or command == "search" and len(sys.argv) > 2:
            # Cari berdasarkan NIM dari argumen
            nim = sys.argv[2]
            if nim in mahasiswa:
                print("Data Mahasiswa:")
                print(f"NIM: {nim}")
                print(f"Nama: {mahasiswa[nim]['nama']}")
                print(f"Nilai: {mahasiswa[nim]['nilai']}")
            else:
                print(f"Mahasiswa dengan NIM {nim} tidak ditemukan!")
        elif command == "tambah" or command == "add" and len(sys.argv) > 4:
            # Tambah mahasiswa: python program.py tambah 2023005 "Nama Mahasiswa" 85
            nim = sys.argv[2]
            nama = sys.argv[3]
            try:
                nilai = int(sys.argv[4])
                if nilai < 0 or nilai > 100:
                    print("Nilai harus di antara 0-100!")
                else:
                    mahasiswa[nim] = {"nama": nama, "nilai": nilai}
                    print("Mahasiswa berhasil ditambahkan!")
                    simpan_ke_file_json()
                    simpan_ke_file_csv()
            except ValueError:
                print("Nilai harus berupa angka!")
        elif command == "hapus" or command == "delete" and len(sys.argv) > 2:
            # Hapus mahasiswa: python program.py hapus 2023005
            nim = sys.argv[2]
            if nim in mahasiswa:
                del mahasiswa[nim]
                print("Data mahasiswa berhasil dihapus.")
                simpan_ke_file_json()
                simpan_ke_file_csv()
            else:
                print(f"Mahasiswa dengan NIM {nim} tidak ditemukan!")
        else:
            print("Perintah tidak dikenali. Memulai program dalam mode interaktif...")
            main()
    else:
        main()