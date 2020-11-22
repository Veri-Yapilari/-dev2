rFile = open('source.c', 'r') # okunacak kaynak dosya
wFile = open('target.c', 'w') # hedef dosyaya yazma, yoksa oluşturup yazma

recess = 0 # girintileme adedi

while True:
    line = rFile.readline()
    if not line:
        break
    if line[0] == '{': # acik süslü parantez var mi kontrolü
        newLine = int(recess) * '\t' + line # recess miktarınca tab boyutunda girintileme yapılır.
        recess += 1 # Girinti sayısını artır
    elif line[0] == '}': # kapalı süslü parantez kontrolü
        newLine = int(recess-1) * '\t' + line # recess'den bir az olacak miktarda tab boyutunda girintileme yap.
        recess -= 1 # Girinti sayısını azalt
    else:
        newLine = int(recess) * '\t' + line # acik ya da kapali süslü parantezz yoksa satırı olduğu gibi bırakır
    wFile.write(newLine) # yazdırma