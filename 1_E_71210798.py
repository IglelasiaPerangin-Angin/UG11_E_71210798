#judul
print ("Menu Program yang Tersedia")
print ("1. pangkatkan angka")
print ("2. akarkan bilangan")

#penyelesaian
#pil
pil = int(input ("Masukkan pilihan yang diinginkan : "))
def PangkatAngka():
    print ("Masukkan angka yang ingin dipangkatkan")
    bilangan = (float(input("Angka : ")))
    print ("ingin memodifikasi pangkat ?(yes/no)")
    b = input (": ")
    if b == "yes" :
        pangkat = float(input("Masukkan nilai pangkat : "))
        r = float(bilangan**pangkat)
        print ("Hasil dari {0}^{1} = ".format(bilangan,pangkat), r)
    else:
        r = (bilangan**2)
        print ("Hasil dari {0}^2 = ".format(bilangan), r)

def AkarBilangan():
    print ("Masukkan angka yang ingin di akar angka")
    bilangan = (float(input("Angka : ")))
    print ("ingin memodifikasi akar ?(yes/no)")
    b = input (": ")
    if b == "yes":
        akar = float(input("Masukkan nilai akar : "))
        r = float(bilangan**(1/akar))
        print ("Hasil akar pangkat {0} dari {1} = ".format(akar,bilangan), r)
    else:
        r = (bilangan**0.5)
        print ("Hasil akar pangkat 2 dari {0} = ".format(bilangan), round(r, 2))
        


if pil == 1:
    PangkatAngka()
elif pil ==2:
    AkarBilangan()
else:
    print("-")



