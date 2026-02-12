class   Sepeda:
    def __init__(self, brand, jenis, year):
        self.brand = brand
        self.jenis = jenis
        self.year = year
    
    def nama_brand(self):
        print('Brand ini adalah', self.brand)
    
    def jenis_sepeda(self):
        print(self.jenis, 'adalah jenis sepedanya')
    
    def year_sepeda(self):
        print(f'Keluaran tahun {self.year}')

    def ubah_year(self, new_year):
        self.year = new_year

sepeda1 = Sepeda('Viar','Listrik',2020)
sepeda2 =Sepeda('Polygon','Biasa', 2019)
sepeda3 = Sepeda('Genio', 'Listrik', 2018)
print(sepeda1.brand)
print(sepeda1.jenis)
print(sepeda1.year)
sepeda1.nama_brand()
sepeda1.jenis_sepeda()
sepeda1.year_sepeda()
sepeda1.ubah_year(2022)   
sepeda1.year_sepeda()

print(sepeda2.brand)
print(sepeda2.jenis)
print(sepeda2.year)
sepeda2.nama_brand()
sepeda2.jenis_sepeda()
sepeda2.year_sepeda()
sepeda2.ubah_year(2022)   
sepeda2.year_sepeda()

print(sepeda3.brand)
print(sepeda3.jenis)
print(sepeda3.year)
sepeda3.nama_brand()
sepeda3.jenis_sepeda()
sepeda3.year_sepeda()
sepeda3.ubah_year(2022)   
sepeda3.year_sepeda()
