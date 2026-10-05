for angka in range(1, 11): 
    print(f"ini adalah for_loop ke-{angka}") 

print("") 

print("ini adalah angka genap") 
for angka_genap in range(2, 21, 2): # Diubah ke 21 agar angka 20 ikut muncul
    print(angka_genap) 

print("") 

print("ini adalah angka ganjil") 
# PERBAIKAN DI SINI: Mulai dari 1, batas sampai 20, lompat 2
for angka_ganjil in range(1, 20, 2): 
    print(angka_ganjil)

print("")

nama = "bil"
for huruf in nama:
    print(huruf) 

print("")

siswa = {"nama ": "bil", "umur " : 16, "kelas " : "X DKV"}
for key, value in siswa.items():
    print(f"{key}: {value}")

print("")

for i in range (1, 11):
    if i == 10:
        break
    if i % 2 == 0:
        continue
    print(i)
else:
    print("selesai")

print("")

for baris in range(1, 6):
    for kolom in range(1, 6):
        print(f"{baris},{kolom}", end=" ")
    print()