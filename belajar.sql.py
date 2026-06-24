import sqlite3

# koneksi ke database (otomatis bikin file db kalau belum ada)
conn = sqlite3.connect("belajar.db")
cursor = conn.cursor()

# bikin tabel
cursor.execute("""
    CREATE TABLE IF NOT EXISTS mahasiswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        umur INTEGER,
        kota TEXT
    )               
""")


conn.commit()
print("Database & tabel berhasil dibuat")

# insert data
cursor.execute("INSERT INTO mahasiswa (nama, umur, kota) VALUES (?, ?, ?)", ("Hafizh", 20, "Bekasi"))
cursor.execute("INSERT INTO mahasiswa (nama, umur, kota) VALUES (?, ?, ?)", ("Budi", 22, "Jakarta"))
cursor.execute("INSERT INTO mahasiswa (nama, umur, kota) VALUES (?, ?, ?)", ("Siti", 22, "Bandung"))

conn.commit()
print("Data berhasil ditambahkan")

# ambil semua data
cursor.execute("SELECT * FROM mahasiswa")
data = cursor.fetchall()

print ("\n=== DATA MAHASISWA ===")
for row in data:
    print(f"ID: {row[0]} | Nama: {row[1]} | Umur: {row[2]} | Kota: {row[3]}")
    
# update data
cursor.execute("UPDATE mahasiswa SET kota = ? WHERE nama = ?", ("Surabaya", "Budi"))
conn.commit()
print("Data berhasil diupdate")

# delete data
cursor.execute("DELETE FROM mahasiswa WHERE nama = ?", ("Siti",))  
conn.commit()
print("Data berhasil dihapus!")

# cek data sekarang
cursor.execute("SELECT * FROM mahasiswa")
data = cursor.fetchall()

print("\n=== DATA SEKARANG ===")
for row in data:
    print(f"ID: {row[0]} | Nama: {row[1]} | Umur: {row[2]} | Kota: {row[3]}")