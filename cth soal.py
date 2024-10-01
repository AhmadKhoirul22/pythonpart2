def cek_kelulusan(nilai):
    if (nilai < 70 and  nilai >=0):
        print(("anda remidi"))
    elif (nilai >= 70 and nilai <= 100):
        print("anda lulus")
    else :
        print("nilai tidak valid")
nilai = int(input("masukan nilai yang anda dapat : "))
cek_kelulusan(nilai)