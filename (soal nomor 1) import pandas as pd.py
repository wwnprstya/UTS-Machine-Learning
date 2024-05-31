import pandas as pd

# Data mahasiswa dan biaya per kedatangan
data = {
    "Nama": ["Ani", "Budi", "Joni", "Jono", "Lono"],
    "Biaya_per_kedatangan": [30000, 35000, 20000, 25000, 15000],
    "Kedatangan": {
        "Senin": [2, 0, 0, 0, 0],
        "Selasa": [0, 3, 0, 0, 0],
        "Rabu": [0, 0, 0, 4, 0],
        "Kamis": [0, 0, 0, 0, 1],
        "Jumat": [0, 0, 2, 0, 0],
        "Sabtu": [5, 0, 0, 0, 0],
        "Minggu": [0, 2, 0, 0, 0]
    }
}

# Membuat DataFrame untuk kedatangan
df_kedatangan = pd.DataFrame(data["Kedatangan"], index=data["Nama"]).T

# Menghitung total kedatangan per mahasiswa
total_kedatangan_per_mahasiswa = df_kedatangan.sum()

# Menghitung total biaya per hari
total_biaya_per_hari = df_kedatangan.mul(data["Biaya_per_kedatangan"]).sum(axis=1)

# a) Rata-rata mahasiswa datang pada minggu ini
rata_rata_kedatangan = total_kedatangan_per_mahasiswa.mean()
print(f"Rata-rata mahasiswa datang pada minggu ini: {rata_rata_kedatangan}")

# b) Kapan biaya tertinggi terjadi?
hari_biaya_tertinggi = total_biaya_per_hari.idxmax()
print(f"Biaya tertinggi terjadi pada hari: {hari_biaya_tertinggi}")

# c) Hari apa biaya lebih dari 110,000?
hari_biaya_lewat_110k = total_biaya_per_hari[total_biaya_per_hari > 110000].index.tolist()
print(f"Hari dengan biaya lebih dari 110000: {hari_biaya_lewat_110k}")

# d) Siapa yang paling banyak datang ke kampus?
paling_banyak_datang = total_kedatangan_per_mahasiswa.idxmax()
print(f"Mahasiswa yang paling banyak datang ke kampus: {paling_banyak_datang}")

# e) Siapa yang datang pada hari Minggu?
datang_minggu = df_kedatangan.loc["Minggu"]
mahasiswa_datang_minggu = datang_minggu[datang_minggu > 0].index.tolist()
print(f"Mahasiswa yang datang pada hari Minggu: {mahasiswa_datang_minggu}")

# f) Berapa biaya tertinggi dan terendah?
biaya_tertinggi_per_kedatangan = max(data["Biaya_per_kedatangan"])
biaya_terendah_per_kedatangan = min(data["Biaya_per_kedatangan"])
print(f"Biaya tertinggi per kedatangan: {biaya_tertinggi_per_kedatangan}")
print(f"Biaya terendah per kedatangan: {biaya_terendah_per_kedatangan}")

# g) Berapa frekuensi datang tertinggi dan terendah?
frekuensi_tertinggi = total_kedatangan_per_mahasiswa.max()
frekuensi_terendah = total_kedatangan_per_mahasiswa.min()
print(f"Frekuensi datang tertinggi: {frekuensi_tertinggi}")
print(f"Frekuensi datang terendah: {frekuensi_terendah}")
