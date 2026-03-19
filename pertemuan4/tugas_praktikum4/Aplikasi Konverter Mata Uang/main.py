from tabulate import tabulate
from kurs import kurs
from konverter import konversi

def tampilkan_tabel_kurs():
    tabel = []
    for kode, nilai in kurs.items():
        tabel.append([kode, f'{nilai :,}'.replace(',','.')])
    print('\n=== KONVERTER MATA UANG===')
    print(tabulate(tabel, headers =['Kode', 'Kurs'], tablefmt = 'grid'))

def main():
    tampilkan_tabel_kurs()
    dari = input('\nDari (IDR/USD/EUR/SGD/JPY): ').upper()
    ke = input('Ke (IDR/USD/EUR/SGD/JPY): ').upper()
    jumlah = float(input('Jumlah: '))

    hasil = konversi(dari, ke, jumlah)
    if hasil is None:
        print('Kode mata uang tidak valid!')
    else:
        format_jumlah = f'{jumlah:,.0f}'.replace(',','.')
        format_hasil = f'{hasil:,.2f}'.replace(',','.')
        print(f'\nHasil: {format_jumlah} {dari} = {format_hasil} {ke}')

if __name__ == '__main__':
    main()