produk = {
    "nama" : "Handphone Samsung",
    "harga" : 1500000,
    "stok" : 20
}

while True:
    print("== MENU PENGELOLAAN DATA PRODUK ==")
    print("1. Tampilkan Data")
    print("2. Tambah Kategori")
    print("3. Ubah Harga")
    print("4. Hapus Kategotri")
    print("5. Keluar")

    pilihan = input("Pilih Menu (1-5): ")

    if pilihan == "1":
        print("Data Produk")

        for key, value in produk.items():
            print(key, ":", value)
        
    elif pilihan == "2":
        produk["Kategori"] = "Elektronik" 

        print("Setelah ditambahkan:")

        for key, value in produk.items():
            print(key, ":", value)

    elif pilihan == "3":
        produk.update({"harga": 2000000})

        print("Setelah diubah:")

        for key, value in produk.items():
            print(key, ":", value)

    elif pilihan == "4":
        produk.pop("Kategori")

        print("Setelah dihapus:")
        for key, value in produk.items():
            print(key, ":", value)

    elif pilihan == "5":
        print("Anda telah keluar dari Program")
        print("Data produk setelah perubahan: ")

        for key, value in produk.items():
            print(key, ":", value)
        break

    else:
        print("Pilihan tidak tersedia.")