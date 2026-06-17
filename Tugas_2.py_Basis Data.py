data_mahasiswa = [
    ["Ahmad", 85],
    ["Budi", 78],
    ["Citra", 90]
]

while True:
    # Menampilkan Menu Utama Aplikasi
    print("\n====================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("====================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Urutkan Data Berdasarkan Nilai")
    print("7. Hitung Rata-rata Nilai")
    print("8. Keluar")
    print("====================================")
    
    pilihan = input("Pilih menu 1-8: ")
    print("------------------------------------")
    
    # 1. Tampilkan Data
    if pilihan == "1":
        if not data_mahasiswa:
            print("Data mahasiswa masih kosong!")
        else:
            print("Daftar Data Mahasiswa:")
            for i, mhs in enumerate(data_mahasiswa, 1):
                print(f"{i}. Nama: {mhs[0]} | Nilai: {mhs[1]}")
                
    # 2. Tambah Data
    elif pilihan == "2":
        nama = input("Masukkan nama mahasiswa baru: ")
        nilai = int(input("Masukkan nilai mahasiswa: "))
        data_mahasiswa.append([nama, nilai])
        print(f"Data {nama} berhasil ditambahkan!")
        
    # 3. Ubah Data
    elif pilihan == "3":
        nama_cari = input("Masukkan nama mahasiswa yang ingin diubah nilainya: ")
        ditemukan = False
        for mhs in data_mahasiswa:
            if mhs[0].lower() == nama_cari.lower():
                nilai_baru = int(input(f"Masukkan nilai baru untuk {mhs[0]}: "))
                mhs[1] = nilai_baru
                print(f"Data nilai {mhs[0]} berhasil diubah menjadi {nilai_baru}!")
                ditemukan = True
                break
        if not ditemukan:
            print(f"Mahasiswa dengan nama '{nama_cari}' tidak ditemukan.")
            
    # 4. Hapus Data
    elif pilihan == "4":
        nama_hapus = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        ditemukan = False
        for mhs in data_mahasiswa:
            if mhs[0].lower() == nama_hapus.lower():
                data_mahasiswa.remove(mhs)
                print(f"Data {mhs[0]} berhasil dihapus!")
                ditemukan = True
                break
        if not ditemukan:
            print(f"Mahasiswa dengan nama '{nama_hapus}' tidak ditemukan.")
            
    # 5. Cari Data
    elif pilihan == "5":
        nama_cari = input("Masukkan nama mahasiswa yang dicari: ")
        ditemukan = False
        for mhs in data_mahasiswa:
            if mhs[0].lower() == nama_cari.lower():
                print(f"Data Ditemukan -> Nama: {mhs[0]} | Nilai: {mhs[1]}")
                ditemukan = True
                break
        if not ditemukan:
            print(f"Mahasiswa dengan nama '{nama_cari}' tidak ditemukan.")
            
    # 6. Urutkan Data Berdasarkan Nilai Tertinggi
    elif pilihan == "6":
        if not data_mahasiswa:
            print("Data kosong, tidak bisa diurutkan!")
        else:
            # Mengurutkan list berdasarkan elemen indeks ke-1 (Nilai) secara descending (tertinggi ke terendah)
            data_mahasiswa.sort(key=lambda x: x[1], reverse=True)
            print("Data berhasil diurutkan berdasarkan nilai tertinggi!")
            # Menampilkan langsung hasil urutan
            for i, mhs in enumerate(data_mahasiswa, 1):
                print(f"{i}. Nama: {mhs[0]} | Nilai: {mhs[1]}")
                
    # 7. Hitung Rata-rata Nilai
    elif pilihan == "7":
        if not data_mahasiswa:
            print("Data kosong, rata-rata nilai adalah 0")
        else:
            total_nilai = sum(mhs[1] for mhs in data_mahasiswa)
            rata_rata = total_nilai / len(data_mahasiswa)
            print(f"Jumlah Mahasiswa : {len(data_mahasiswa)}")
            print(f"Total Nilai      : {total_nilai}")
            print(f"Rata-rata Nilai  : {rata_rata:.2f}")
            
    # 8. Keluar dari Program
    elif pilihan == "8":
        print("Terima kasih! Program selesai.")
        break
        
    # Validasi jika user salah memasukkan input selain angka 1-8
    else:
        print("Pilihan tidak valid! Silakan masukkan angka 1 sampai 8.")