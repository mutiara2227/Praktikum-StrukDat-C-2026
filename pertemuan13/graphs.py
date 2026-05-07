class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_kota(self, kota):
        if kota not in self.graph:
            self.graph[kota] = []

    def tambah_jalan(self, kota1, kota2, jarak):
        self.tambah_kota(kota1)
        self.tambah_kota(kota2)

        self.graph[kota1].append((kota2, jarak))
        self.graph[kota2].append((kota1, jarak))

        print(f"[INPUT] Menambahkan jalan {kota1} - {kota2} ({jarak} km)")

    def tampilkan_graph(self):
        print("\n[INFO] Struktur Jaringan Distribusi :")

        for kota in self.graph:
            print(f"-{kota} terhubung ke: ", end="")

            for tetangga, jarak in self.graph[kota]:
                print(f"{tetangga} ({jarak})", end="  ")

            print()

    def dijkstra(self, asal):

        jarak = {}

        for kota in self.graph:
            jarak[kota] = float('inf')

        jarak[asal] = 0

        dikunjungi = []

        while len(dikunjungi) < len(self.graph):

            kota_terdekat = None
            jarak_min = float('inf')

            for kota in self.graph:
                if kota not in dikunjungi and jarak[kota] < jarak_min:
                    jarak_min = jarak[kota]
                    kota_terdekat = kota

            if kota_terdekat is None:
                break

            dikunjungi.append(kota_terdekat)

            for tetangga, bobot in self.graph[kota_terdekat]:

                jarak_baru = jarak[kota_terdekat] + bobot

                if jarak_baru < jarak[tetangga]:
                    jarak[tetangga] = jarak_baru

        return jarak

print('SISTEM NAVIGASI LOGISTIK "KILAT MAJU"')
print('=========================')

g = Graph()

g.tambah_jalan("Jakarta", "Bandung", 150)
g.tambah_jalan("Jakarta", "Cirebon", 200)
g.tambah_jalan("Bandung", "Tasikmalaya", 100)
g.tambah_jalan("Bandung", "Cirebon", 130)
g.tambah_jalan("Cirebon", "Semarang", 250)
g.tambah_jalan("Tasikmalaya", "Semarang", 200)

g.tampilkan_graph()

print("\n[PROSES] Menghitung jarak dari : Jakarta...\n")

hasil = g.dijkstra("Jakarta")

print("[HASIL] Jarak Terpendek dari jakarta:")

for kota in hasil:
    if kota != "Jakarta":
        print(f"Ke {kota} : {hasil[kota]} km")
