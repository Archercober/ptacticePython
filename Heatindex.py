import codecs
import csv
from meteocalc import heat_index, Temp

# main function for calculating the heat index


def CalcuateHeatindex(F=1.0, rh=1.0):
    Hindex = -42.379 + 2.04901523 * F + 10.14333127 * rh
    Hindex = Hindex - 0.22475541 * F * rh - 6.83783 * pow(10, -3) * F * F
    Hindex = Hindex - 5.481717 * pow(10, -2) * rh * rh
    Hindex = Hindex + 1.22874 * pow(10, -3) * F * F * rh
    Hindex = Hindex + 8.5282 * pow(10, -4) * F * rh * rh
    Hindex = Hindex - 1.99 * pow(10, -6) * F * F * rh * rh
    h = round(Hindex, 1)
    return h


def Cal2(T=1.0, rh=1.0):
    e = (6.112 * 10**(7.5 * T / (237.7 + T)) * rh / 100)
    H = T + (5 / 9) * (e - 10)
    return round(H, 1)

f1 = 'C:/Users/Archer/Desktop/新しいフォルダー/20171225.csv'
f2 = 'C:/Users/Archer/Desktop/新しいフォルダー/20171226.csv'
f3 = 'C:/Users/Archer/Desktop/新しいフォルダー/20171227.csv'


def DealCsv(name='hello'):
    r = open(name, "rt")
    w = open(name.replace('2017122', '1'), 'w', newline='')
    read = csv.reader(r)
    write = csv.writer(w)
    head_row = next(read)
    head_row.append('E_WGBT(F)')
    head_row.append('E_WGBT(C)')
    head_row.append('AE_WGBT(C)')
    head_row.append('AE_WGBT(F)')
    write.writerow(head_row)
    for line in read:
        at = Temp(float(line[1]), 'c')
        fa = float(line[1]) * 1.8 + 32
        hum = float(line[5])
        # print(fa,hum)
        e_H = CalcuateHeatindex(fa, hum)
        e_C = Cal2(float(line[1]), hum)
        e_A = heat_index(at, hum)
        line[0] = line[0][-8:]
        line.append(e_H)
        line.append(e_C)
        line.append(e_A.c)
        line.append(e_A.f)
        write.writerow(line)

    r.close()
    w.close()


DealCsv(f1)
DealCsv(f2)
DealCsv(f3)
# print(CalcuateHeatindex(80,40))

# t=Temp(26.67,'c')
#hh=heat_index(t, 36)
# print(hh.f,hh.c)
print(Cal2(26.67, 40))



