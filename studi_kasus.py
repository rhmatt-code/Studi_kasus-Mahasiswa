mata_kuliah = ['Kalkulus','Statistik','Algoritma','PTI','Bahasa Inggris']

def hitung_nilai_akhir():
    nilai_akhir = (nilai_tugas * 20/100) + (nilai_uts * 30/100) + (nilai_uas * 35/100)
    
    return nilai_akhir

data_mahasiswa =(input("Masukan Nama mahasiswa: ")) 

for matkul in mata_kuliah :
    print("Masukka nilai untuk mata kuliah " +matkul +":")
    nilai_tugas =int(input("Nilai Tugas: "))
    nilai_uts =int(input("Nilai UTS: "))
    nilai_uas =int(input("Nilai UAS: "))

if hitung_nilai_akhir() > 85:
   huruf_nilai = "A"
elif hitung_nilai_akhir() > 80 and hitung_nilai_akhir() < 85:
    huruf_nilai = "B"
elif hitung_nilai_akhir() > 75 and hitung_nilai_akhir() < 80:
    huruf_nilai = "C"
elif hitung_nilai_akhir() > 70 and hitung_nilai_akhir() < 75:
    huruf_nilai = "D"
else:
    huruf_nilai = "E"

print("\n")

print("Hasil Nilai dari Mahasiswa Semestr 1 :\n")

print("Nama Mahasiswa: " + data_mahasiswa)

for matkul in mata_kuliah :
    print(str(matkul) + ", Nilai Akhir: " + str(hitung_nilai_akhir()) + ", Huruf Nilai: " + huruf_nilai)

    
    