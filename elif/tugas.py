# and
id = int(input("masukan id : "))
nama = input("masukan nama : ")

if id == 23 and nama == "bil":
    print("selamat datang")
else :
    print("salah bray")

# or
cuaca = input("masukan cuaca saat ini : ")

if cuaca == "gerimis" or cuaca == "hujan":
    print("enaknya makan mie dan jeruk hangat") 
elif cuaca == "panas":
    print("enaknya beli eskrim")
else :
    print("enaknya makan steak omlet")

# and dan or 
bulan = input("masukan bulan : ")
status = input("masukan status : ")

if bulan == "januari" and status == "mahasiswa":
    print("saatnya kuliah!!")
elif bulan == "juli" or status == "pekerja":
    print("saatnya bekerja")
else :
    print("mending turu")