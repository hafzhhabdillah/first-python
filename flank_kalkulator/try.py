while True:
    print("\n===== KALKULATOR =====")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    # Kode rahasia untuk masuk ke login
    if pilihan == "1234":
        print("\n===== LOGIN =====")

        username = input("Username: ")
        password = input("Password: ")

        if username == "bil" and password == "123":
            print("\nAnda berhasil login!")
            print("Anda masuk ke dashboard.")
            
            print("\n===== DASHBOARD =====")
            print("Selamat datang, bil!")

        else:
            print("\nUsername atau password salah.")
            print("Anda kembali ke kalkulator.")

    elif pilihan == "1":
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        hasil = angka1 + angka2

        print("Hasil:", hasil)

    elif pilihan == "2":
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        hasil = angka1 - angka2

        print("Hasil:", hasil)

    elif pilihan == "3":
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        hasil = angka1 * angka2

        print("Hasil:", hasil)

    elif pilihan == "4":
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        if angka2 == 0:
            print("Tidak bisa membagi dengan 0.")
        else:
            hasil = angka1 / angka2
            print("Hasil:", hasil)

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")