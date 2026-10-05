# and adalah kode untuk memberikan akses apabila pada kedua hal sama benar

username = input("masukan nama : ")
password = input("masukan password : ")

if username == "admin" and password == "admin123":
    print("login berhasil")
else :
    print("login gagal")


# or adalah kode untuk memberikan akses apabila salah satu atau kedua hal bernilai benar

hari = input("masukan hari : ")

if hari == "senin" or hari == "selasa":
    print("belajar ptyhon") 
elif hari == "minggu" or hari == "jumat":
    print("libur")
else :
    print("belajar laravel")


# kombinasi and dan or

umur = int(input("masukan umur : "))
punya_kartu_member = True

if punya_kartu_member == True and (umur < 14 or umur > 20):
    print("bisa masuk")
else :
    print("tidak bisa masuk")


