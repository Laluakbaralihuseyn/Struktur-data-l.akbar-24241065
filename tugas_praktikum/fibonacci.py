# Deret awal
initial_values = [1, 2, 2, 5, 8]

# Input jumlah deret
deret = int(input("Jumlah deret angka: "))

# Menampilkan deret Fibonacci
for i in range(deret):
    if i < len(initial_values):
        print(initial_values[i], end=", ")
    else:
        next_value = initial_values[-1] + initial_values[-2]
        initial_values.append(next_value)
        print(next_value, end=", ")