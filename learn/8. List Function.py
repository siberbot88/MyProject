Numbers=[1,6,9,3,8,2]
countries=["Italy","Germany","Spain","Spain","Spain","Spain","France","Portugal","Australia"]
countries2=countries.copy()
countries.sort()

#menggabungkan list
countries.extend(Numbers)

#menambahkan objek ke list
countries.append("South Africa")

#insert objek ke list sesuai index dipilih
countries.insert(3,"India")

#menghapus objek list
countries.remove("Germany")

#menghapus data list
# countries.clear()

#mengambil object paling akhir
countries.pop()

print(countries.index("Australia"))
print(countries.count("Spain"))
print(countries)
print(countries2)