korongok = []

while True:
    koordinata = ""
    sori = str(input(f"Adja meg a korong sorának számát: "))
    if sori == "":
        break
    else:
        oszlopi = str(input(f"Adja meg a korong oszlopának számát: "))
    koordinata = sori+"K"+oszlopi
    if koordinata in korongok:
        korongok.remove(koordinata)
    elif int(koordinata.split("K")[0])>=1 and int(koordinata.split("K")[0])<=8 and int(koordinata.split("K")[1])>=1 and int(koordinata.split("K")[1])<=8 and koordinata not in korongok:
        korongok.append(koordinata)
    else:
        print(f"Ezt a korongot nem lehet lerakni")
print(korongok)