#Data nilai mahasiswa disimpan dalam format berikut:
nilai_siswa = {
    "S01": {"nama": "Dina", "tugas": 80, "uts": 75, "uas": 85},
    "S02": {"nama": "Abdul Harris", "tugas": 90, "uts": 88, "uas": 92},
    "S03": {"nama": "Sheila", "tugas": 70, "uts": 65, "uas": 70}
}
#Tambahkan data siswa baru: "S04" dengan nama "Fafa", nilai tugas 85, UTS 80, dan UAS 90.
nilai_siswa['SO4'] = {    
    'nama': 'Fafa', 'tugas': 85, 'uts': 80, 'uas': 90
}
print(nilai_siswa)
#Hitunglah nilai akhir setiap siswa dengan bobot: (Tugas 20% + UTS 30% + UAS 50%) dan tampilkan hasilnya.
for x in nilai_siswa.values():
    nilai_akhir = (x['tugas']* 0.2) + (x['uts']* 0.3) + (x['uas']* 0.5)
    print(f'{x['nama']} : {nilai_akhir}')
#Tampilkan nama siswa yang memiliki nilai UAS di atas 80.
print('Siswa yang memiliki nilai uas diatas 80 :')
for y in nilai_siswa.values():
    if y['uas'] > 80:
        print(y['nama'])