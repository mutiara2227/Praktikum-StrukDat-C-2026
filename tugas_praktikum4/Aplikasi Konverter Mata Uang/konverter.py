from kurs import kurs

def konversi(dari, ke, jumlah):
    if dari == 'IDR' and ke in kurs:
        return jumlah / kurs[ke]
    elif dari in kurs and ke == 'IDR':
        return jumlah * kurs[dari]
    elif dari in kurs and ke in kurs:
        idr = jumlah * kurs[dari]
        return idr / kurs[ke]
    else:
        return None