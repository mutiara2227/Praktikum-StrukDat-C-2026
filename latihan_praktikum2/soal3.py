#Terdapat dua set yang berisi daftar keahlian (skill) dari dua tim pengembang:
tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL","NodeJS"}
#Tentukan keahlian yang dimiliki oleh kedua tim (irisan).
Keahlian_kedua_tim = tim_frontend & tim_backend
print(Keahlian_kedua_tim)
#Tentukan keahlian yang hanya dimiliki oleh tim_backend.
Keahlian_tim_backend = tim_backend.difference(tim_frontend)
print(Keahlian_tim_backend)
#Gabungkan kedua set tersebut untuk melihat daftar total keahlian unik yang tersedia di perusahaan.
KeahlianTotal = tim_frontend.union(tim_backend)
print(KeahlianTotal)