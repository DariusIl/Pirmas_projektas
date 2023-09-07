# import random
# #vardas = "Modestas"
# # # print(vardas)
# # skaicius = 25
# #
# # print("Mano sugalvotas skaicius " + str(skaicius))
# # skaicius1 = '32'
# #
# # true_or_false = False
# # fruits = ['apple', 'orange', 'kiwi', 'banana']
# # print(fruits[2])
# # print(type(fruits))
# lietuvos_pilietis = {
#     'id': 1,
#     'Vardas': 'Antantas',
#     'Amzius': 34,
#     'Miestas': 'Klaipeda'
# }
#
# print(lietuvos_pilietis)
# print("Pries:")
# print("Vardas: ", lietuvos_pilietis["Vardas"])
# print("Po: ")
# lietuvos_pilietis['Vardas'] = "Giedrius"
# print("Vardas: ", lietuvos_pilietis["Vardas"])
#
# # Temperaturos = [20, 25,  22, 18, 12]
# #
# # suma = sum(Temperaturos)
# #
# # kiekis = len(Temperaturos)
# #
# # vidutine_temp = suma / kiekis
# # print(vidutine_temp)
#
# # # 1. Sukurkite kintamąjį vardas ir priskirkite jam savo vardą. Tada parašykite programą,
# # # kuri išspausdina sveikinimo žinutę su jūsų vardu;
# #
# # Vardas = "Darius"
# # sveikinimas = "Sveikas_prisijunges"
# # print(sveikinimas + Vardas)
#
# # 2. Sukurkite kintamuosius skaicius1 ir skaicius2,
# # ir priskirkite jiems du skaičius. Parašykite programą,
# # kuri juos sudeda ir išspausdina sumą.
#
# # skaicius1 = 5
# # skaicius2 = 1
# # suma = skaicius2 + skaicius1
# # print(suma)
#
# # 3.Parašykite programą, kuri prašo vartotojo įvesti skaičių ir nustato,
# # ar tai yra lyginis ar nelyginis skaičius.
#
#
#
# #4. Sukurkite žodyną pavadinimu telefonu_knygute,
# # kuriam raktai yra žmonių vardai, o reikšmės - jų telefono numeriai. Parašykite programą,
# # kuri leidžia vartotojui ieškoti telefono numerio pagal žmogaus vardą.
#
# # telefonu_knygute = {
# #     'Antanas': 85200000,
# #     'Simas': 85200001,
# #     'Vanagas': 85200002,
# #     'Goga': 85200003
# #     }
#
# #5 Sukurkite žodyną pavadinimu produktai, kuriame saugosite prekių pavadinimus
# # ir jų kainas. Parašykite programą,
# # kuri suranda pigiausią produktą ir išspausdina jo pavadinimą ir kainą.
# # produktai = {
# #     'id': 1,
# #     'pavadinimas': 'pirma',
# #     'kaina': 2,
# # 'id': 2,
# #     'pavadinimas': 'antra',
# #     'kaina': 3,
# # 'id': 3,
# #     'pavadinimas': 'trecia',
# #     'kaina': 4,}
# # print(produktai)
# # print(f"{min} found in 'kaina'")
#
#
# # skaicius = 42
# # if skaicius == 42:
# #     print("lygus")
# # elif skaicius ==42:
# #
# # else:
# #     print("Nelygus")
#
# # sarasas = [1,2,3,4,5,]
# # for elementas in sarasas:
# #     print("elementas: ", elementas)
# #
# #     for i in range(5):
# #         print(i)
# #
# #
# #         # kur turi pradeti ir kur turi pabaigti ( paskutinio skaiciaus nerodo (-1))
# #  for i in range(2,7):
# #         print(i)
# # stepai - paskutinis parodo per kiek zingsniu eina
# #         for i in range(2, 10, 2):
# #             print(i)
# #
# #             revers nuo kito galo
# # for i in range(5, 0 -1):
# #     print(i)
#
#
# # # koks didziausias skaicius sarase
# # skaiciai = [24,11,72,34,7,84]
# #
# # didziausias_skaicius = skaiciai[0]
# #
# # for skaicius in skaiciai:
# #     if skaicius > didziausias_skaicius:
# #      didziausias_skaicius = skaicius
# # print("didziausias skaicius yra: ", didziausias_skaicius)
#
# # skaicius = input("Koks tavo vardas:")
#
# # skaicius = int(input("Iveskite skaiciu: "))
# # suma = 0
# #
# # for i in range(1,skaicius + 1):
# #     suma += i
# # print("Skaicius suma nuo 1 iki", skaicius, "yra", suma)
#
# # is saraso isfiltruoti lyginius skaicius
#
# # sarasas = [2,5,12,25,9]
# # lyginiai_skiciai = []
# #
# # for skaicius in sarasas:
# #     if skaicius %2 == 0:
# #         lyginiai_skiciai.append(skaicius)
# # print("lyginiai_skaiciai ", lyginiai_skiciai)
#
# # eiluciu_skaicius = int(input("iveskite sveika skaiciu"))
# # for eilute in range(1, eiluciu_skaicius+1):
# #     tarpas = eiluciu_skaicius - eilute
# #     zvaigzdes = 2 * eilute -1
# #     print(" " * tarpas + "*"*zvaigzdes)
#
# # rasti pirminius skaicius intervale tarp 10 ir 50
# # pradzia =10
# # pabaiga = 50
# #
# # print(f"pirminiai skaiciai tarp {pradzia} ir {pabaiga } yra:")
# # for skaicius in range(pradzia, pabaiga+1):
# #     if skaicius >1:
# #         for daliklis in range(2, skaicius):
# #             if (skaicius % daliklis)==0:
# #                 break
# #         else:
# #             print(skaicius)
#
# # patikritni zaodiu is saraso rasti ir atspausdinti zodzius kurie prasideda raide "A"
# # zadziai_is_a = ["as", "tu","jis","asta", "marius"]
# # raide = "a"
# # for zodis in zadziai_is_a:
# #     if zodis[0]. lower()==raide. lower():
# #         print(zodis)
# #
# # # sudaryti ir isvesti daygybos lentele
# # print("Daugybos lnetele nuo 1 iki 10")
# # for i in range(1,11):
# #     for j in range (1,11):
# #         rezultatas = i*j
# #         print(f"{i} x {j} = {rezultatas}")
# #     print()
#
# # patikrinti vartotojo ivestas skaicius teigiamas neigiamas ar nulis
# # skaicius = int(input("iveskite skaiciu: "))
# # if skaicius > 0:
# #     print("teigiamas")
# # elif skaicius <0:
# #     print("neigiamas")
# # else:
# #     print("nulis")
#
# # isveda FIZZ - is 3 dalinasi, BUZZ - is 5 ir FIZZBUZZ is abieju. 1-100
#
# # for skaicius in range(1,101):
# #     if skaicius % 3 ==0 and skaicius % 5 ==0:
# #         print("FIZZBUZZ")
# #     elif skaicius % 3 ==0:
# #         print("FIZZ")
# #     elif skaicius % 5 ==0:
# #         print("BUZZ")
# #     else:
# #         print(skaicius)
#
# # sukurkite skaiciu atspejimo programa
# pasleptas_skaicius = random.randint( 1, 100)
# bandymai =0
# maksimalus_bandymu_skaicius =10
# while bandymai<maksimalus_bandymu_skaicius:
#     spejimas = int(input("atspekite paslepta skaiciu nuo 1 iki 100"))
#     bandymai +=1
#     if spejimas  == pasleptas_skaicius:
#         print(f"sveikinam!!!atspejote skaiciu per {bandymai}bandymus")
#         break
#     elif spejimas < pasleptas_skaicius:
#         print("badykite didesni skaiciu")
#     else:
#         print("bandykite mazesni skaiciu")
# if bandymai >= maksimalus_bandymu_skaicius:
#     print(f"jus pasieket maksimalu bandymu skaiciu. pasleptas skaicius buvo {pasleptas_skaicius}")

# zodziu sarasas kur saugomi zodziai ir isvesti zodzius kuriu ilgis ilgesnis nei 6 simboliai
# zadziu_sarasas = ["as", "jis", "mano", "namas", "daiktas", "kinas", "kojines"]
# zodynas = {}
# for zodis in zadziu_sarasas:
#     zodynas[zodis]=len(zodis)
# for zodis, ilgis in zodynas.items():
#     if ilgis > 6:
#         print(f"{zodis}:{ilgis} simboliai")

# 1. Sukurkite žodyną ir trumpą tekstą. Atspasudinkite žodžius, kurie pasikartojo daugiau nei 3 kartus.

# tekstas = "zodis kuris karotjasi tris kartu buna zodis nes cia svarbu zodis zodis"
# zodynas = {}
# zodziai = tekstas.split()
# for zodis in zodziai:
#     zodynas[zodis]= zodynas.get(zodis, 0)+1
# for zodis, pasikartojimai in zodynas.items():
#     if pasikartojimai >=3:
#         print(f"pasikartojantis zodis yra: {zodis}, pasikartoja {pasikartojimai} kartu")

# 2 .Sukurti sąrašą žodžių ir išvesti unikalius žodžius bei jų pasikartojimo dažnumą;
# zodziu_sarasas = ["as", "jis", "mano", "namas", "daiktas", "kinas", "jis", "mano","namas","namas"]

# 3. Sukurkite žodyną su studentų duomenimis ir
# atspausdinkite studentus, kurių vidurkis yra aukščiau 8.0;

# studentas = {
#     'id': 1,
#     'Vardas': 'Antantas',
#     'Vidurkis': 7,}
#     {'id': 2,
#     'Vardas': 'Antants',
#     'Vidurkis': 8,}
# 20230906
#1.  Parašykite programą, kuri suskaičiuoja visų sveikujų skaičių
# nuo 1 iki n ėjimo sumą, kur n yra vartotojo įvestas skaičius. Panaudokite
# "for" ciklą ir "if" sąlygos sakinį, kad tikrintumėte, ar įvestas skaičius yra sveikasis;

# n = int(input("iveskite sveika skaiciu: "))
# if n <= 0:
#     print("ivestas skaicius turi buti teigiamas bandykite dar:")
# else:
#     suma = 0
#     for skaicius in range(1,n +1):
#         suma += skaicius
#     print(f"suma nuo 1 iki {n} yra {suma}")

# 2. Sukurkite programą, kurioje vartotojas gali įvesti mokinio pažymį
# (nuo 1 iki 10). Programa turi grąžinti mokinio vertinimą
# (pvz., "Neužtektinai", "Silpnai", "Vidutiniškai", "Gerai", "Puikiai"). Naudokite "if" sąlygos sakinį;

# pazimys = int(input("iveskite vertinima: "))
# if pazimys <= 0 or pazimys >10:
#     print("ivestas vertinimas neteisingas:")
# elif pazimys >= 1 and pazimys <=4:
#     print("Neužtektinai")
# elif pazimys >= 5 and pazimys <= 6:
#     print("Silpnai")
# elif pazimys >= 7 and pazimys <= 8:
#     print("Vidutiniškai")
# elif pazimys==9:
#     print("Gerai")
# elif pazimys==10:
#     print("Puikiai")

# 3. Sukurkite programą, kuri leidžia vartotojui įvesti metus. Programa turi patikrinti,
# ar įvesti metai yra keliamieji (dalijasi iš 4) ir atspausdinti atitinkamą pranešimą;
# metai = int(input("Iveskite metus: "))
# if metai <= 0:
#     print("metai negali buti neigiami iveskite teigiama skaiciu: ")
# elif metai % 4 == 0:
#     print(f"{metai} metai yra keliamieji")
# else:
#     print(f"{metai} metai yra nekeliamieji")

# 4. Turite žodyną, kuriame yra vardai ir amžius. Parašykite programą,
# kuri peržiūri žodyną ir išrenka tik tas poras,
# kuriose amžius yra didesnis arba lygus 18. Rezultatus patalpinkite naujame žodyne;
# zodynas = {
#     'Jonas': 18,
#     'simas': 9,
#     'ona' : 20,
#     'anyt':5
#     }
# zodynas2 = {}
# for vardas, amzius in zodynas.items():
#     if amzius >=18:
#         zodynas2[vardas] = amzius
# print(zodynas2)

# 5. Leiskite vartotojui įvesti kelias prekes ir jų kainas.
# Sukurkite sąrašą, kuriame prekės yra žodynai,
# kuriuose yra prekės pavadinimas ir kaina.
# Taip pat paskaičiuokite bendrą visų prekių kainą;

# prekiu_krepselis = []
# while True:
#     preke = input("Nurodyte prekę arba įrašykite žodį baigti")
#     if not preke:
#         break
#     kaina = float(input("Įveskite prekės kainą: "))
#     prekes_info = {'pavadinimas': preke, 'kaina': kaina}
#     prekiu_krepselis.append(prekes_info)
#
# Krepselio_suma = sum((prekes_info['kaina'] for prekes_info in prekiu_krepselis))
# print("prekiu sarasas: ")
# for prekes_info in prekiu_krepselis:
#     print(f"Pavadinimas: {prekes_info['pavadinimas']}, Kaina: {prekes_info['kaina']}")
# print(f"Bendra kaina: {Krepselio_suma}")
#
# 6. Turite sąrašą žmonių vardų. Sukurkite programą,
# kuri leidžia vartotojui įvesti vardą ir patikrina,
# ar jis yra sąraše. Jei vardas yra sąraše,
# programa turi išvesti pranešimą
# "Vardas yra sąraše," kitu atveju - "Vardo nėra sąraše."
