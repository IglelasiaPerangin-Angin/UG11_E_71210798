#JUDUL

print("=======Program Manipulasi String=======")
print("Pilihan Menu : ")
print ("1. Hitung kata ")
print ("2. Cek kata ")
print ("3. Ubah kata ")
x = input("Pilihan anda : ")

#TASK 1
def hitungKata():
    kalimat = input(" Masukan sebuah kalimat/kata : ")
    inginditung = input("Masukan kata yang ingin dihitung : ")
    lower1 = kalimat.lower()
    lower2 = inginditung.lower()
    if lower2 in lower1:
        x = lower1.count(lower2)
        print("Terdapat sebanyak",x,"kata",inginditung,"di dalam string")
#TASK 2
def cekkata():
    kalimat2= input("Masukan sebuah kalimat/kata : ")
    ingincek= input("Masukan kata yang ingin di cek : ")
    if ingincek in kalimat2:
        print("kata",ingincek,"terdapat di dalam string")
        print("String diubah menjadi : ")
        x = kalimat2.replace(ingincek,ingincek.upper())
        print(x)
    
    else:
        print("Kata",ingincek,"tidak terdapat di dalam string ")
        print("String diubah menjadi : ")
        print(kalimat2,ingincek)
#TASK 3
def ubahKata():
    kalimat3= input("Masukan sebuah kalimat/kata : ")
    ingincek2= input("Masukan kata yang ingin di ubah : ")
    inginganti= input("Masukan kata pengganti :")
    print("Anda akan mengubah kata",ingincek2,"Menjadi",inginganti,"Sebanyak 1x")
    cek= input("Apakah anda ingin mengubah jumlah total penggantian kata ? (yes/no) : ")
    if cek=="no":
        print("String berhasil diubah menjadi : ")
        print(kalimat3.replace(ingincek2,inginganti,1))

    elif cek== "yes":
        jumlahtotal= int(input("Masukan jumlah total penggantian : "))
        print("String berhasil diubah menjadi : ")
        print(kalimat3.replace(ingincek2,inginganti,jumlahtotal))

#PENYELESAIAN
if x == "1":
    hitungKata()

elif x == "2" :
    cekkata()

elif x == "3" : 
    ubahKata()

else:
    print("Pilihlah yang ada dimenu!")
