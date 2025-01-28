#seq = [1,2,3,4,5]
#for anggota in seq:
    #print(anggota*2)
from idlelib.debugobj_r import remote_object_tree_item

# for i in range(0,10,2):
#     print("hallo")

# a = 0
# while a < 10:
#     print(a)
#     if a == 5:
#         continue
#     else:
#         a += 1

# arr = [1,2,3,4,5]
# # arr_ans = []
# # for  anggota in arr:
# #     arr_ans.append(anggota**2)
# #
# # print(arr_ans)
#
# hasil = ["ganjil" if num%2 != 0 else "genap" for num in arr]
# print(hasil)

# list_arr = [[1,2,3],[2,3,4],[3,4,5]]
# hasil = []
# for sub in list_arr:
#     total= sum(sub)
#     hasil.append(total)
#
# print(hasil)

# input = [800,600,400,200]
# compare_input = [500,200,400]
#
# for i in range(len(input)):
#     if input[i] not in compare_input:
#         input[i] = 0
#     else:
#         input[i] = 1
#
# print(input)

# Input harga barang dari dua toko
input_prices = {
    "Indoramet": {
        "Ayam": 30000,
        "Sayur": 15000,
        "Buah": 20000,
        "Ikan": 22000
    },
    "Alfaramet": {
        "Ayam": 25000,
        "Sayur": 12000,
        "Buah": 30000,
        "Ikan": 25000
    }
}

# Input jumlah barang yang ingin dibeli
items_to_buy = {
    "Ayam": 2,
    "Sayur": 1,
    "Ikan": 1
}

# Program untuk menghitung total biaya
total_cost = 0

# Loop untuk setiap barang yang akan dibeli
for item, quantity in items_to_buy.items():
    # Cari harga termurah dari kedua toko untuk item tersebut
    price_indoramet = input_prices["Indoramet"].get(item, float('inf'))
    price_alfaramet = input_prices["Alfaramet"].get(item, float('inf'))
    cheapest_price = min(price_indoramet, price_alfaramet)

    # Hitung total untuk item tersebut
    total_cost += cheapest_price * quantity

# Output hasil perhitungan
print("Total biaya belanja:", total_cost)

def perkalian(a,b):
    return a*b

print(perkalian(10,3))

def salam(nama=" ", formal=True, Kondisi = " "):
    wordings = {
        (True, " "): "Halo {}!".format(nama),
        (False, " "): "Halo {}!".format(nama),
        (True, "Salam"): "Halo {}! Salam {}!".format(nama,Kondisi),
        (False, "Salam"): "Halo {}! Salam {}!".format(nama,Kondisi)
    }
    return wordings[(formal,Kondisi)]

def kalkulator(a,b,operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return a/b
    else:
        return

while True:
    a = float(input("Masukkan angka pertama:"))
    operasi = input("Masukkan operator: ")
    b = float(input("Masukkan angka kedua:"))

    print(kalkulator(a, b, operasi))


