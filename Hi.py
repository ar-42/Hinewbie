import os
# warna
P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
N = "\033[0m"    # Warna Mati

def main():
  os.system("clear")
  print(f'\t{P} Siapa nama Anda? {N}')
  nama=input(f'\t{K} Nama: {P} ')
  print (f'\n\t{H} Hallo {nama} {N}') 

def logo():
  print ("""
 …………(0 0)
.—oOO–(_)—–.
╔═════════════════╗
║    Hi newbie    ║
╚═════════════════╝
‘———————-oOO
……...|__|__|
……….. || ||
…….. ooO Ooo
""")

def op():
  print(f'\n {K}Terimakasih sudah menggunakan script hinewbie{N}')
  print('\n Jalankan lagi atau exit?')
  print("""
1. jalankan ulang
2. exit
""")
  lagi=input('pilihan: ')
  if lagi=="1":
    main()
    logo()
    op()
  else:
    print('\n ')
    os.system("clear")
    print(' Byeeee')

main()
logo()
op()
