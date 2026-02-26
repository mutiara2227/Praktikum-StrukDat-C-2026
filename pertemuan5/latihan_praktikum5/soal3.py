#Terdapat dua data pendaftar UKM (Unit Kegiatan Mahasiswa):
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}
#Tampilkan mahasiswa yang hanya mendaftar di ukm_coding saja (tidak mendaftar di robotik).
Hanya_ukm_coding = ukm_coding - ukm_robotik
print(Hanya_ukm_coding)
#Tampilkan daftar seluruh mahasiswa unik yang mendaftar di salah satu atau kedua UKM tersebut.
Pendaftar_unik = ukm_coding.union(ukm_robotik)
print(Pendaftar_unik)
#Cek apakah "Andi" merupakan anggota dari ukm_robotik. Tampilkan hasil dalam bentuk boolean.
Cek_anggota = 'Andi' in ukm_robotik
print(Cek_anggota)