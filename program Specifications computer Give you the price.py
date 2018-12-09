
from tkinter import messagebox

#Program for the price of computers only Enter the specifications Note computers for the year 2018 new
print ("Program specifications computer ")
SP=input ("Special computer enter 0 or General computer enter 1 :")
#by hussain alsamr
while int(SP)==1:
    print(' specifications Computer ')
    c = input('CPU :')  # cpu cor 2, i3 , i5 , i7 ,i9-> input writ Just int EX ( 2 ,3 ,5 ,7 ,9)
    r = input('RAM :')  # ram the computer int (2-16) GB
    h = input('HARD :')  # hard the computer int 50 into 2000 GB
    k = input("APPROX :")  # GPU Graphics Wizard input cor i5 or more
    if int(c) == 2 and int(r) >= 2 and int(r) <= 4 and int(h) >= 20 and int(h) <= 250:
        print('125$-225$ Type( HP and DELL)')
    elif int(c) == 3 and int(r) >= 2 and int(r) <= 4 and int(h) >= 20 and int(h) <= 320:
        print("190$-300$ Type( HP or DELL or lenovo )")
    elif (c) == 5 and int(r) >= 2 and int(r) <= 6 and int(h) >= 20 and int(h) <= 500:
        print("250$-350$ Type (HP or DELL or lenovo or backgdell)")

    elif int(c) == 5 and int(r) >= 2 and int(r) <= 6 and int(h) >= 20 and int(h) <= 500 and int(h) <= 720 and int(
            k) == 1 and int(k) == 2:
        print("250$-350$ Type( HP or DELL or lenovo or backgdell)")
    elif int(c) == 7 and int(r) >= 6 and int(r) <= 10 and int(h) >= 20 and int(h) <= 1000 and int(k) == 1 and int(
            k) <= 2:
        print("380$-550$ Type( HP or DELL or lenovo or backgdell or ACER)")
    elif int(c) == 7 and int(r) >= 6 and int(r) <= 12 and int(h) >= 20 and int(h) <= 1000 and int(k) >= 2 and int(
            k) <= 4:
        print("700$-850$ Type( HP or DELL or lenovo or backgdell or ACER)")
    elif int(c) == 7 and int(r) >= 6 and int(r) <= 16 and int(h) >= 20 and int(h) <= 1000 and int(k) >= 2 and int(
            k) <= 6:
        print("900$-1300$ Type( HP or DELL or lenovo or backgdell or ACER or ) Super Computer more 2000$ Type ")
    else :
        messagebox.showinfo( message="Please Sponsor Terms of Entry")
        continue