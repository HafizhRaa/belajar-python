tugas = []

def tambah_tugas(tugas_baru):
    tugas.append(tugas_baru)
    print(f"Tugas '{tugas_baru}' berhasil ditambahkan")

def lihat_tugas():
        if len(tugas) == 0:
            print("Belum ada tugas!")
        else:
            print("\n=== DAFTAR TUGAS ===")
            for i, t in enumerate(tugas, 1):
                print(f"{i}. {t}")

def hapus_tugas(nomor):
    if nomor < 1 or nomor > len (tugas):
        print("Nomor tugas tidak valid!")
    else:
        dihapus = tugas.pop(nomor - 1)
        print(f"Tugas '{dihapus}' berhasil dihapus!")

#PAGE2

while True:
    print("\n=== TO-DO-LIST ===")            
    print("1. Tambah tugas")            
    print("2. Lihat tugas")       
    print("3. Hapus tugas")         
    print("4. Keluar")


    pilihan = input ("pilih menu (1/2/3/4): ")

    if pilihan == "1":
        tugas_baru = input("Masukan tugas: ")
        tambah_tugas(tugas_baru)
    elif pilihan == "2":
        lihat_tugas()
    elif pilihan == "3":
        lihat_tugas()
        nomor = int(input("Masukkan nomor tugas yang mau dihapus: "))
        hapus_tugas(nomor)
    elif pilihan == "4":
        print("Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid!")