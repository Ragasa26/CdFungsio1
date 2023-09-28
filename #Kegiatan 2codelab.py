#Kegiatan 2
random_list = [105, 3.1, "Hello", 737, "Phyton", 2.7, "World", 412, 5.5, "AI"]

huruf = []
angka = []
koma = []
ratusan = []
puluhan = []
satuan = []
dicti = {'ratusan': 1,'puluhan' : 2,'satuan' : 3}


for x in random_list:
    if(type(x) == str) :
        huruf.append(x)
    elif(type(x) == float) :
        koma.append(x)
    else :
        angka.append(x)

for x in angka:
    if((x/100) > -1 ) :
        ratusan.append(int(x/100))
        dicti['ratusan'] = ratusan
 

for x in angka:
    if((x%10) > -1) :
        puluhan.append(int(((x%100)/10)))
        dicti['puluhan'] = puluhan

for x in angka:
    if((x%1) > -1) :
        satuan.append(int(((x%10))))
        dicti['satuan'] = satuan



print(huruf)
koma = tuple(koma)
print(koma)
print(angka)
print("dict ratusan", dicti['ratusan'])
print("dict puluhan", dicti['puluhan'])
print("dict satuan", dicti['satuan'])

