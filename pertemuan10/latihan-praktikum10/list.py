riwayat = []

riwayat.append('https://www.w3schools.com/python/python_dsa_stacks.asp')
riwayat.append('https://www.youtube.com/')
riwayat.append('https://ft.unri.ac.id/')
print('Riwayat: ', riwayat)

topElement = riwayat[-1]
print('URL Teratas: ', topElement)

poppedElement = riwayat.pop()
print('Hapus URL: ', poppedElement)

print('Riwayat setelah dihapus: ',riwayat)

isEmpty = not bool(riwayat)
print('Riwayat kosong(True)/tidak(False): ', isEmpty)

print('Total URL: ', len(riwayat))