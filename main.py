#input nilai matematika
matematika = float(input("masukkan nilai matematika : "))

#input nilai bahasa indonesia
indonesia = float(input("masukkan nilai bahasa indonesia : "))

#input nilai kewarganegaraan
kewarganegaraan = float(input("masukkan nilai kewarganegaraan : "))

#input nilai bahasa inggris
inggris = float(input("masukkan nilai bahasa inggris : "))

#input nilai praktikum
praktikum = float(input("masukkan nilai praktikum : "))

#perhitungan nilai rata rata
rata_rata = (matematika + indonesia + kewarganegaraan + inggris + praktikum) / 5

#perhitungan IPK
ipk = ""
if rata_rata >= 85:
    ipk = "A"
elif rata_rata >= 70 and rata_rata < 85:
    ipk = "B"
elif rata_rata >= 55 and rata_rata < 70:
    ipk = "C"
else:
    ipk = "D"

# #perhitungan index
# index = 0
#
# if matematika > 85 or indonesia > 85 or kewarganegaraan > 85 or inggris > 85 or praktikum > 85:
#     index += 4
# elif (matematika > 70 and matematika <85) or (kewarganegaraan >70 and kewarganegaraan <85) or (indonesia >70 and indonesia <85) or (inggris >70 and inggris <85) or (praktikum >70 and praktikum <85):
#     index += 3
# else:
#     index += 2
#
# #perhitungan index
# index_akhir = index/5


#hasil penilaian
print("Nilai rapot mahasiswa")
print("====================================")
print("nilai matematika : ",matematika)
print("nilai bahasa indonesia : ",indonesia)
print("nilai kewarganegaraan : ",kewarganegaraan)
print("nilai bahasa inggris : ",inggris)
print("nilai praktikum : ",praktikum)
print("-----------------------------------")
print("rata rata : ",rata_rata)
print("IPK : ",ipk)




