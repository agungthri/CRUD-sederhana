from . import Operasi

def delete_console():
    read_console()
    while True:
        try:
            index = int(input("Masukkan Indeks Yang Akan Dihapus : "))
            break
        except:
            print("Masukkan Angka")
    Operasi.delete(index)
    read_console()

def update_console():
    read_console()
    while True:
        try:
            index = int(input("Masukkan Indeks Yang Akan DiUpdate : "))
            break
        except:
            print("Masukkan Angka")
    Operasi.update(index)
    read_console()

def create_console():
    print("\n\n"+"="*100)
    print("Silahkan Tambah Data Buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
        except:
            print("tahun harus angka dan 4 digit, silakan masukkan rahun lagi 'yyyy'")
    Operasi.create(tahun, judul, penulis)
    print("berikut ini adalah data baru anda")
    read_console()

def read_console():
    data_file = Operasi.read()
    index = "NO"
    judul = "JUDUL"
    penulis = "PENULIS"
    tahun = "TAHUN"

    #header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

    #data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun  = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}", end="")
        

    #footer
    print("="*100+"\n")
