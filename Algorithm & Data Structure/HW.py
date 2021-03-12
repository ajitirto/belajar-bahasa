def binSe(kumpulan, target):
#Mulaidariseluruhruntutanelemen
    low = 0
    high =len(kumpulan) - 1
#Secaraberulangbelahruntutanitumenjadiseparuhnya
#sampaitargetnyaditemukan
    while low <= high:
#Temukanpertengahanruntutitu
        mid = (high + low) // 2
#Apakahpertengahannyamemuattarget?
    if kumpulan[mid] == target:
        return True
#ataukahtargetnyadisebelahkirinya?
    elif target < kumpulan[mid]:
        high = mid - 1
#ataukahtargetnyadisebelahkanannya?
    else:
        low = mid + 1
#Jikaruntutnyatidakbisadibelahlagi,berartitargetnyatidakada
        return False
print("AAA")