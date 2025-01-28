# numbers = [1,2,3,4,5]
# for num in numbers:
#     if num == 3:
#         continue ;
#     print(num)

# x = 5
# y = 10
# print(x > 3 and y < 15)
angka = [1,2,3,4,5]
hasil = 0
for x in angka:
    if x % 2 != 0:
        hasil += x
print(hasil)