#HASAN KILICKAYA
#1. Soru

with open('text1.txt') as f:
    list1 = []
    list2 = []
    for line in f:
        line = line.split()
        if line:
            line = [int(i) for i in line]
            list1.append(line)


    for x in range(len(list1)):
        a = list1[x][1]
        list2.append(a)


list2.sort()
print list2

#2. sorunun baslangici(Tam değil)

for list in range(len(list2)):

    a = []
    b = list2[-1]
    a = [list2[-1]]
    if (b <= 600):
        b = b + list2[0]
        a.append(list2[0])
        del list2[0]
        if (b <= 600):
            b = b + list2[0]
            a.append(list2[1])
            del list2[0]
            print a
            if (b <= 600):
                b = b + list2[0]
                a.append(list2[2])
                del list2[0]
                print a

