# biodata seseorang 
# data nilai unjiannya
# kalau nilainya bagus dia mendapatkan beasiswa
# kalau nilainya tidak bagus dia tidak mendapatkan beasiswa

nama = "bil"
umur = 16

nilai_matematika = 84
nilai_inggris = 89
nilai_rpl = 88
rata_rata = (nilai_matematika + nilai_inggris + nilai_rpl) / 3

print(f"Nama : {nama}")
print(f"Umur : {umur} tahun")
print(f"Rata-rata Nilai: {rata_rata:.2f}")

if rata_rata >= 80:
    print("Selamat! Anda Mendapatkan Beasiswa")
else:
    print("Maaf, Anda Tidak Mendapatkan Beasiswa")
