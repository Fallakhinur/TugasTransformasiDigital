karyawan=input("Nama Karyawan                : ")
jabatan=input("Golongan Jabatan 1/2/3       : ")
pendidikan=input("Pendidikan SMA/D1/D3/S1      : ")
jumlah_jamkerja=int(input("Jumlah Jam Kerja             : "))
gaji=300000
if jabatan=="1":
   presentase="5%"
   tunjangan_jab=5/100* gaji
elif jabatan=="2":
   Presentase="10%"
   tunjangan_jab=10/100* gaji
elif jabatan=="3":
   presentase="15%"
   tunjangan_jab=15/100* gaji
else: 
   print("Anda salah Input!")

#tunjangan pendidikan
if pendidikan=="SMA" or pendidikan=="sma":
   presentase="2.5%"
   tunjangan_pen=2.5/100* gaji
elif pendidikan=="D1" or pendidikan=="d1":
   presentase="5%"
   tunjangan_pen=5/100* gaji
elif pendidikan=="D3" or pendidikan=="d3":
   presentase="20%"
   tunjangan_pen=20/100* gaji
elif pendidikan=="S1" or pendidikan=="s1":
   presentase="30%"
   tunjangan_pen=30/100* gaji
else:
   print("Anda Salah Input!")

jamlembur=3500
if jumlah_jamkerja>=8:
   jumlah_jam=(jumlah_jamkerja-8) * jamlembur
else:
   jumlah_jam=0

#output
print("--------------------------------------------------------")
print("Karyawan yang bernama :",karyawan)
print("Gaji yang diterima    ")
print("Tunjangan Jabatan     : Rp.",tunjangan_jab)
print("Tunjangan Pendidikan  : Rp.",tunjangan_pen)
print("Honor lembur          : Rp.",jumlah_jam)
print("Gaji pokok            : Rp.",gaji)
print("-------------------------------------------------------+")
total_gaji=int(tunjangan_jab)+int(tunjangan_pen)+int(jumlah_jam)+int(gaji)
print("Total gaji            : Rp.",total_gaji)