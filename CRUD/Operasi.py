from . import Database
from .Util import random_string
import time

def delete(index):
    with open(Database.DB_NAME, 'r', encoding='utf-8') as file:
        file_data = file.readlines()
        for i, data in enumerate(file_data):
            if i == index-1:
                file_data.remove(data)
            
    with open(Database.DB_NAME, 'w') as file:
        file.writelines(file_data)

def update(index):
    penulis = input("Penulis\t:")
    judul = input("Judul\t:")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            break
        except:
            print("tahun harus angka dan 4 digit, silakan masukkan rahun lagi 'yyyy'")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE['judul'][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"

    with open(Database.DB_NAME, 'r', encoding='utf-8') as file:
        file_data = file.readlines()
        for i, data in enumerate(file_data):
            if i == index-1:
                file_data[index-1] = data_str
            
    with open(Database.DB_NAME, 'w') as file:
        file.writelines(file_data)

                
def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE['judul'][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
   
    try:
        with open(Database.DB_NAME, 'a', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print("Gagal")

def create_first_data():

    penulis = input("Penulis : ")
    judul = input("Judul : ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            break
        except:
            print("tahun harus angka dan 4 digit, silakan masukkan rahun lagi 'yyyy'")
    
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE['judul'][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    print(data_str)
    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print("Gagal")

def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("membaca database error")
        return False


    
