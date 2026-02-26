#Diberikan list berisi tuple data mahasiswa dan poin keaktifan: data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
#Lakukan perulangan pada list tersebut. Jika poin > 80, tampilkan: "[Nama] mendapatkan predikat Gold". Jika poin 50-80, tampilkan: "[Nama] mendapatkan predikat Silver". Di bawah itu, tampilkan: "[Nama] mendapatkan predikat Bronze"
for nama, nilai in data_aktivitas:
    if nilai > 80:
        print(f'{nama} mendapatkan predikat Gold')
    elif 50 < nilai < 80:
        print(f'{nama} mendapatkan predikat Silver')
    else:
        print(f'{nama} mendapatkan predikat Bronze')


