# 1. Tabel Pembeli
tabel_pembeli = [
    ["ahmad@gmail.com", "Ahmad", "Jakarta"],
    ["budi@gmail.com", "Budi", "Bandung"]
]

# 2. Tabel Penjual
tabel_penjual = [
    ["tokoelektronik@gmail.com", "Pak Jaka"],
    ["tokobuku@gmail.com", "Ibu Sri"]
]

# 3. Tabel Barang (Ada Foreign Key Email Penjual di indeks ke-3)
tabel_barang = [
    ["LAP01", "Laptop ASUS", 7500000, "tokoelektronik@gmail.com"],
    ["BUK02", "Buku Pemrograman Python", 150000, "tokobuku@gmail.com"]
]

# 4. Tabel Transaksi Membeli (Many-to-Many: Menghubungkan Pembeli, Barang, dan Jumlah)
tabel_transaksi_membeli = [
    # [ID_Transaksi, Email_Pembeli, SKU_Barang, Jumlah_Beli]
    ["TRX001", "ahmad@gmail.com", "LAP01", 1],
    ["TRX002", "budi@gmail.com", "BUK02", 2]
]

# Cetak simulasi nota transaksi untuk pembuktian relasi
print("====================================================")
print("       HASIL HUBUNGAN RELASI TRANS-AKSI TOKO")
print("====================================================")

for trx in tabel_transaksi_membeli:
    id_trx, email_pemb, sku_brg, qty = trx
    
    # Cari nama pembeli
    nama_pembeli = next(p[1] for p in tabel_pembeli if p[0] == email_pemb)
    # Cari nama barang dan nama penjualnya
    detail_barang = next(b for b in tabel_barang if b[0] == sku_brg)
    nama_barang = detail_barang[1]
    email_penj = detail_barang[3]
    nama_penjual = next(pj[1] for pj in tabel_penjual if pj[0] == email_penj)
    
    print(f"ID Transaksi : {id_trx}")
    print(f"Pembeli      : {nama_pembeli} ({email_pemb})")
    print(f"Barang Dibeli: {nama_barang} (Jumlah: {qty})")
    print(f"Penjual/Toko : {nama_penjual}")
    print("-" * 52)