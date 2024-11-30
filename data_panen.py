# Data panen
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        },
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        },
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        },
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        },
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        },
    }
}

# Bagian 1: Menyelesaikan Tugas
for lokasi, info in data_panen.items():
    print(f"Nama Lokasi: {info['nama_lokasi']}")
    print(f"Hasil Panen: {info['hasil_panen']}")
    print("-" * 30)

total_jagung = sum(info['hasil_panen']['jagung'] for info in data_panen.values())
print(f"Total Hasil Panen Jagung: {total_jagung}")

nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama Lokasi3: {nama_lokasi3}")

hasil_padi = {lokasi: info['hasil_panen']['padi'] for lokasi, info in data_panen.items()}
hasil_kedelai = {lokasi: info['hasil_panen']['kedelai'] for lokasi, info in data_panen.items()}
print("Hasil Panen Padi:", hasil_padi)
print("Hasil Panen Kedelai:", hasil_kedelai)

for lokasi, info in data_panen.items():
    padi = info['hasil_panen']['padi']
    jagung = info['hasil_panen']['jagung']

    if padi > 1300 or jagung > 800:
        print(f"{info['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{info['nama_lokasi']} dalam kondisi baik.")
print("Perubahan di branch Baru")
