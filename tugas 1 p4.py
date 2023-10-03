# Dictionary untuk menentukan gaji pokok berdasarkan golongan jabatan
gaji_pokok_per_golongan = {
    "Golongan 1": 5000000,
    "Golongan 2": 6000000,
    "Golongan 3": 7000000,
    "Golongan 4": 8000000
}

# Dictionary untuk menentukan tunjangan jabatan
tunjangan_jabatan = {
    "Golongan 1": 1000000,
    "Golongan 2": 1500000,
    "Golongan 3": 2000000,
    "Golongan 4": 2500000
}

# Dictionary untuk menentukan tunjangan pendidikan
tunjangan_pendidikan = {
    "SMA": 500000,
    "Diploma": 1000000,
    "Sarjana": 1500000,
    "Magister": 2000000,
    "Doktor": 2500000
}

# Tarif lembur per jam
tarif_lembur_per_jam = 50000

# Input nama karyawan, golongan jabatan, pendidikan, dan jumlah jam kerja
nama_karyawan = input("Nama karyawan: ")
golongan_jabatan = input("Golongan jabatan (Golongan 1/Golongan 2/Golongan 3/Golongan 4): ")
pendidikan = input("Pendidikan (SMA/Diploma/Sarjana/Magister/Doktor): ")
jam_kerja = float(input("Jumlah jam kerja: "))

# Memeriksa apakah golongan jabatan dan pendidikan valid
if golongan_jabatan in gaji_pokok_per_golongan and pendidikan in tunjangan_pendidikan:
    gaji_pokok = gaji_pokok_per_golongan[golongan_jabatan]
    tunjangan_jabatan = tunjangan_jabatan[golongan_jabatan]
    tunjangan_pendidikan = tunjangan_pendidikan[pendidikan]
    
    # Menghitung honor lembur
    if jam_kerja > 40:
        lembur = (jam_kerja - 40) * tarif_lembur_per_jam
    else:
        lembur = 0

    # Menghitung total gaji
    total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + lembur

    # Menampilkan hasil
    print(f"Karyawan yang bernama {nama_karyawan}")
    print(f"Honor yang diterima (Gaji Pokok): Rp {gaji_pokok:,.0f}")
    print(f"Tunjangan Jabatan: Rp {tunjangan_jabatan:,.0f}")
    print(f"Tunjangan Pendidikan: Rp {tunjangan_pendidikan:,.0f}")
    print(f"Honor Lembur: Rp {lembur:,.0f}")
    print(f"Total Gaji: Rp {total_gaji:,.0f}")
else:
    print("Golongan jabatan atau pendidikan tidak valid.")