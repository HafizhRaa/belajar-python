import sqlite3

# koneksi database
conn = sqlite3.connect("todolist.db")
cursor = conn.cursor()

# bikin tabel
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tugas ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tugas TEXT,
        status TEXT DEFAULT 'belum'
     )   
""")
conn.commit()

def tambah_tugas(tugas_baru):
    cursor.execute("INSERT INTO tugas (tugas) VALUES (?)", (tugas_baru,))
    conn.commit()
    print(f"Tugas '{tugas_baru}' berhasil ditambahkan!")
    
def lihat_tugas():
    cursor.execute("SELECT * FROM tugas")
    data = cursor.fetchall()
    if len(data) == 0:
        print("Belum ada tugas!")
    else:
        print("\n=== DAFTAR TUGAS ===")
        for row in data:
            print(f"{row[0]}. [{row[2]}] {row[1]}")
             
def hapus_tugas(nomor):
    cursor.execute("DELETE FROM tugas WHERE id = ?", (nomor,))
    conn.commit()
    print("Tugas berhasil dihapus!")
   
def selesai_tugas(nomor):
    cursor.execute("UPDATE tugas SET status = 'selesai' WHERE id = ?", (nomor,))
    conn.commit()
    print("Tugas ditandai selesai!") 
    
# function
while True:
    print("\n=== TO-DO LIST ===")
    print("1. Tambah tugas")
    print("2. Lihat tugas")
    print("3. Tandai selesai")
    print("4. Hapus tugas")
    print("5. Keluar")
    
    pilihan = input ("Pilih menu (1/2/3/4/5): ")
    
    if pilihan == "1":
        tugas_baru= input("Masukan tugas: ")
        tambah_tugas(tugas_baru)
    elif pilihan == "2":
        lihat_tugas()
    elif pilihan == "3":
        lihat_tugas()
        nomor = int(input("Masukan nomor tugas yang selesai: "))
        selesai_tugas(nomor)
    elif pilihan =="4":
        lihat_tugas()
        nomor = int(input("Masukan nomor tugas yang mau dihapus: "))
        hapus_tugas(nomor)    
    elif pilihan == "5":
        print("Sampai jumpa!")
        conn.close()
        break
    else:
        print("Pilihan didak valid!")    
        