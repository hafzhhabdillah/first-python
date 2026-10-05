# type data

# == : Sama dengan (Contoh : 5 == 5 → Benar)
# != : Tidak sama dengan (Contoh : 5 != 3 → Benar)
# < : Kurang dari (Contoh : 3 < 5 → Benar)
# > : Lebih dari (Contoh : 5 > 3 → Benar)
# <= : Kurang dari atau sama dengan (Contoh : 5 <= 5 → Benar)
# >= : Lebih dari atau sama dengan (Contoh : 5 >= 5 → Benar)

nilai = 75

if nilai <= 70: 
    print("anda tidak lulus")
else:
    print("anda lulus")

password = input("masukan password :")

if password == "admin123":
    print("login berhasil")
else:
    print("login gagal")
    