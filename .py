try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasilnya:", hasil)
except ValueError:
    print("Itu bukan angka!")
except ZeroDivisionError:
    print("Ga bisa bagi dengan 0!")
    