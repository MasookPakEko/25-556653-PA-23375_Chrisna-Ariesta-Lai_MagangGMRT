import numpy as np

sudut_satu = float(input("Masukkan sudut lengan pertama: "))
sudut_dua = float(input("Masukkan sudut lengan kedua: "))
sudut_tiga = float(input("Masukkan sudut lengan ketiga: "))
lengan_satu = float(input("Masukkan panjang lengan 1: "))
lengan_dua = float(input("Masukkan panjang lengan 2: "))
lengan_tiga = float(input("Masukkan panjang lengan 3: "))

x = np.radians(sudut_satu)
y = np.radians(sudut_dua)
z = np.radians(sudut_tiga)

H01 = np.array([[np.cos(x), -np.sin(x), 0], [np.sin(x), np.cos(x), 0], [0, 0, 1]])
H12 = np.array([[1, 0, lengan_satu], [0, 1, 0], [0, 0, 1]])
H23 = np.array([[np.cos(y), -np.sin(y), 0], [np.sin(y), np.cos(y), 0], [0, 0, 1]])
H34 = np.array([[1, 0, lengan_dua], [0, 1, 0], [0, 0, 1]])
H45 = np.array([[np.cos(z), -np.sin(z), 0], [np.sin(z), np.cos(z), 0], [0, 0, 1]])
H56 = np.array([[1, 0, lengan_tiga], [0, 1, 0], [0, 0, 1]])

H06 = H01 @ H12 @ H23 @ H34 @ H45 @ H56

print(f"Koordinat x terhadap basis (Px): {H06[0, 2]}")
print(f"Koordinat y terhadap basis (Py): {H06[1, 2]}")