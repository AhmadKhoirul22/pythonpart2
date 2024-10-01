def grade_nilai(nilai):
    if (nilai >= 0 and nilai < 60):
        print("E")
    elif (nilai >= 60 and nilai < 70):
        print("D")
    elif (nilai >= 70 and nilai < 80):
        print("C")
    elif (nilai >= 80 and nilai < 90):
        print("B")
    elif (nilai >= 90 and nilai <= 100):
        print("A")
    else:
        print("ga nyambung")
nilai = float(input("masukan nilai yang anda dapat :"))
grade_nilai(nilai)