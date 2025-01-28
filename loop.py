#percobaan membuat pesan login
username = "admin"
password = "xqhumftmzy2112"

while True:
    uname = input("Masukkan Username : ")
    if uname == username:
        while True :
            pword = input("Masukkan Password : ")
            if pword == password:
                print("Selamat anda berhasil login")
                break
        break


animals = ['cat', 'dog', 'rabbit']
for animal in animals:
    print(animal)
    if animal == 'dog':
        continue


