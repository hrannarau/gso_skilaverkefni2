import os
print("1. Bæta við")
print("2. Breyta upplýsingum")
print("3. Eyða upplýsingum")
print("4. Prenta út alla símaskránna")
print("5. Leita að ákveðnu nafni og prenta upplýsingar")
print("6. Hætta")
svar = input("Hvaða aðgerð viltu framkvæma? ")

while svar != "6":
    if svar == "1":
        val = input("Viltu bæta við nýjan aðila í símaskrána? j/n ")
        while val == "j":
            nafn = input("Hvað er nafnið? ")
            kennitala = input("Hvað er kennitalan? ")
            simi = input("Hvað er símanúmerið? ")

            skra = open("simaskra.txt", "a")
            skra.write(nafn)
            skra.write(",")
            skra.write(kennitala)
            skra.write(",")
            skra.write(simi)
            skra.write(";")
            skra.close()

            val = input("Viltu bæta við nýjan aðila í símaskrána? j/n ")

    elif svar == "2":
        skra = open("simaskra.txt", "r")
        simaskra = skra.read().split(";")
        skra.close()
        hvadaUppl = input("Hvaða upplýsingar viltu breyta? na/kt/nr ")
        if hvadaUppl == "na":
            hvadaNafn = input("Hjá hverjum viltu breyta upplýsingum? ")
            nyNafn = input("Hvað er nýja nafnið? ")
            teljari = 0
            for x in simaskra:
                faersla = x.split(",")
                if faersla[0] == hvadaNafn:
                    faersla[0] = nyNafn
                    strengur = faersla[0] + "," + faersla[1] + "," + faersla[2]
                    simaskra[teljari] = strengur
                else:
                    teljari = teljari + 1
        elif hvadaUppl == "kt":
            hvadaNafn = input("Hjá hverjum viltu breyta upplýsingum? ")
            nyKt = input("Hvað er nýja kennitalan? ")
            teljari = 0
            for x in simaskra:
                faersla = x.split(",")
                if faersla[0] == hvadaNafn:
                    faersla[1] = nyKt
                    strengur = faersla[0] + "," + faersla[1] + "," + faersla[2]
                    simaskra[teljari] = strengur
                else:
                    teljari = teljari + 1
        elif hvadaUppl == "nr":
            hvadaNafn = input("Hjá hverjum viltu breyta upplýsingum? ")
            nyNumer = input("Hvað er nýja númerið? ")
            teljari = 0
            for x in simaskra:
                faersla = x.split(",")
                if faersla[0] == hvadaNafn:
                    faersla[2] = nyNumer
                    strengur = faersla[0] + "," + faersla[1] + "," + faersla[2]
                    simaskra[teljari] = strengur
                else:
                    teljari = teljari + 1
        else:
            print("villa")
        skra = open("simaskra.txt", "w")
        for x in simaskra:
            texti = x + ";"
            skra.write(texti)
        skra.close()
        break

    elif svar == "3":
        skra = open("simaskra.txt", "r")
        simaskra = skra.read().split(";")
        skra.close()
        hvadaNafn = input("Hvern vilt þú eyða? ")
        teljari = 0
        for x in simaskra:
            faersla = x.split(",")
            if faersla[0] == hvadaNafn:
                simaskra.pop(teljari)
            else:
                teljari = teljari + 1
        skra = open("simaskra.txt", "w")
        for x in simaskra:
            texti = x + ";"
            skra.write(texti)
        skra.close()
        break

    elif svar == "4":
        skra = open("simaskra.txt", "r")
        simaskra = skra.read().split(" ")
        skra.close()
        for x in simaskra:
            print(x)
            print("\n")

    elif svar == "5":
        skra = open("simaskra.txt","r")
        simaskra = skra.read().split(";")
        skra.close()
        b = "já"
        if b == "já":
            hvadaNafn = input("Hvað heitir aðilin sem þú ert að leita að? ")
            for i in simaskra:
                if hvadaNafn in i:
                    print(i)
        break

    elif svar == "6":
        break


