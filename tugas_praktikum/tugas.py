# Fungsi untuk menghasilkan deret bilangan genap
def deret_genap(jumlah):
    genap = []
    for i in range(1, jumlah + 1):
        if i % 2 == 0:
            genap.append(i)
    return genap

# Input jumlah deret
jumlah_deret = int(input("Masukkan jumlah deret: "))

# Menghasilkan dan menampilkan deret bilangan genap
bilangan_genap = deret_genap(jumlah_deret)
print("Outputnya:", ', '.join(map(str, bilangan_genap)))