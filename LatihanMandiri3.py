import re

a = input("Masukkan nama file : ")
with open(a, "r") as handle:
    j = dict()

    for i in handle:
        if "from" in str(i.lower()):
            cari = re.search(r"from (.+@\w+\.\w+\.?\w*)", i.lower())

            if cari != None:
                b = cari.group(1)

                if b not in j:
                    j[b] = 1
                else:
                    j[b] += 1
print(j)