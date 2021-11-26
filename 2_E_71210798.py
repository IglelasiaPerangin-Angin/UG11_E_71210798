#judul input

m4 = input("Masukkan kata : ")
awm = len(m4)

#penyelesaian

if (awm == 7):
    print("Huruf tengah pada kata",m4,"adalah",m4[2:5])
elif (awm == 3):
    print("Huruf tengah pada kata",m4,"adalah",m4[1])
elif (awm == 6):
    print("Huruf tengah pada kata",m4,"adalah",m4[2:4])
elif (awm == 8):
    print("Huruf tengah pada kata",m4,"adalah",m4[2:6])
elif (awm == 9):
    print("Huruf tengah pada kata",m4,"adalah",m4[3:6])
else:
    print("mejuahjuah")
