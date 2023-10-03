# Gaji pokok untuk karyawan kontrak
gaji_pokok_karyawan_kontrak = 300000

# Dictionary untuk menentukan persentase tunjangan jabatan berdasarkan golongan
persentase_tunjangan_jabatan = {
    1: 0.05,
    2: 0.10,
    3: 0.15
}

# Dictionary untuk menentukan persentase tunjangan pendidikan berdasarkan pendidikan
persentase_tunjangan_pendidikan = {
    "SMA": 0.025,
    "D1": 0.05,
    "D3": 0.20,
    "S1": 0.30
}

# Tarif lembur per jam
tarif_lembur_per_jam = 3500

# Input nama karyawan, golongan jabatan, pendidikan, dan jumlah jam kerja
nama_karyawan = input("Nama karyawan: ")
golongan_jabatan = int(input("Golongan jabatan (1/2/3): "))
pendidikan = input("Pendidikan (SMA/D1/D3/S1): ")
jam_kerja = float(input("Jumlah jam kerja: "))

# Menghitung tunjangan jabatan
if golongan_jabatan in persentase_tunjangan_jabatan:
    persentase_jabatan = persentase_tunjangan_jabatan[golongan_jabatan]
    tunjangan_jabatan = gaji_pokok_karyawan_kontrak * persentase_jabatan
else:
    tunjangan_jabatan = 0

# Menghitung tunjangan pendidikan
if pendidikan in persentase_tunjangan_pendidikan:
    persentase_pendidikan = persentase_tunjangan_pendidikan[pendidikan]
    tunjangan_pendidikan = gaji_pokok_karyawan_kontrak * persentase_pendidikan
else:
    tunjangan_pendidikan = 0

# Menghitung honor lembur
if jam_kerja > 8:
    jam_lembur = jam_kerja - 8
    honor_lembur = jam_lembur * tarif_lembur_per_jam
else:
    honor_lembur = 0

# Menghitung total gaji
total_gaji = gaji_pokok_karyawan_kontrak + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

# Menampilkan hasil
print(f"Karyawan yang bernama {nama_karyawan}")
print(f"Honor yang diterima (Gaji Pokok): Rp {gaji_pokok_karyawan_kontrak:,.0f}")
print(f"Tunjangan Jabatan: Rp {tunjangan_jabatan:,.0f}")
print(f"Tunjangan Pendidikan: Rp {tunjangan_pendidikan:,.0f}")
print(f"Honor Lembur: Rp {honor_lembur:,.0f}")
print(f"Total Gaji: Rp {total_gaji:,.0f}")
