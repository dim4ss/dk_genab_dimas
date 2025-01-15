#program menghitung nilai akhir
print("PROGRAM MENGHITUNG NILAI AKHIR")
tugas=float(input("masukan nilai tugas:"))
uas=float(input("masukan nilai uas:"))
uts=float(input("masukan nilai uts:"))

#mengecek
nilai_akhir=(0.3 * uts) + (0.5*uas )+( 0.2*tugas)
#hasil
print("NILAI AKHIR",nilai_akhir)