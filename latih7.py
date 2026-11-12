#============================================
#PROGRAM FUNGSI DAN MODULARISASI PYTHON
#Pertemuan 6 - Pemrograman Python
#Studi Kasus: Perhitungan Nilai Mahasiswa
#============================================

# FUNGSI 1: Input data mahasiswa
def input data():
    print(==="INPUT DATA MAHASISWA"===)
    nama = input("Masukan nilai tugas:")
    tugas = float(input("Masuki nilai tugas:"))
    uts = float(input("Masukan nilai UTS:"))
    uas = float(input("Masukan nilai UAS:"))

    return nama,tugas,uts,uas

# FUNGSI 2: Menghitung nilai akhir
def hitung nilai(tugas,uts,uas):
    nilai akhir =(tugas*0.30)+(uts*0.30)+(uas*0.40)
    return nilai akhir

# FUNGSI 3: Menentukan grade
def tentukan grade(nilai):
    if nilai>= 85:
        return"A"
    elif nilai>= 75:
        return"B" 
    elif nilai>= 65:
        return"C"
    elif nilai>= 50:
        return"D"
    else:
        return"E"
#FUNGSI 4: Menentukan status kelulusan
def status kelulusan(nilai):
    if nilai>= 60:
        return"LULUS"
    else:
        return"TIDAK LULUS"
#FUNGSI 5: Menampilkan hasil
def tampilkan hasil(nama,nilai grade,status):
    print("\n==================================")
    print("  HASIL NILAI MAHASISWA  ")
    print("==================================")
    print("Nama mahasiswa   :",nama)
    print("Nilai akhir      :",round(nilai,2))
    print("Grade            :",grade)
    print("Status           :"status)
    print("==================================")

# PROGRAM UTAMA
def main():
    nama,tugas,uts,uas=input data()

    nilai= hitung nilai(tugas,uts,uas)
    grade= tentukan grade(nilai)
    status= status kelulusan(nilai)
    tampilkan hasil(nama,nilai,grade,status)

# Menjalankan program utama
main()
