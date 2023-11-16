with open('./ct2020/thongkexau/THONGKEXAU.INP') as fin:
    s=fin.readline()
for i in s:
    a[i]=a.get(i,0)+1