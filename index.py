# Master str
#lower 1
#text = input("Entre yon chen karakte: ")
#text.lower()
#print(text.lower())
import random

#split() 2
#text1 = input("Entre yon chen karakte: ")
#x = text1.rsplit(" ")
#print(x)

#3
#text2 = input("Entre yon chen karakte: ")
#majis = text2.title()
#print(majis)

#4
#text3 = input("Entre yon chen karakte: ")
#inisyal = ""
#for i in text3.split():
    #inisyal += i[0]
#print(inisyal)

#5
#text4 = input("Entre yon chen karakte: ")
#i = text4.replace("a","@")
#print(i)

#6
#text5 = input("Entre yon chen karakte: ")
#invers= reversed(text5)
#for i in invers:
 #   print(i)

#7
#text6 = input("Entre yon chen karakte: ")
#x = text6.find("a")
#print(x)

#8
#text7 = input("entrer une phrase: ")
#index = text7.find("a")
#sum=0
#while index != -1:
 #   sum+= index
  #  index = text7.find("a",index+1)
#print(sum)

#9
#text8 = input("entrer une phrase: ")
#index = text8.find("a")
#i = []
#while index != -1:
 #   i.append(index)
  #  index = text8.find("a",index+1)

#print(i)

#10
#text9 = input("entrer une phrase: ")
#x = text9.replace(" ","")
#print(x)

#Master list
#1
#number = int(input("Entrez un nombre divisible par 2: "))
#if number % 2 == 0:
 #   my_list = [number]
  #  for i in range(10):
   #     if my_list[-1] + 2 <= number + 20:
    #        my_list.append(my_list[-1] + 2)
    #print(my_list)
#else:
 #   print("Le nombre n'est pas divisible par 2.")

#2
#list_pam = []
#for i in range(5):
    #number = int(input("antre yon chif:"))
    #list_pam.append(number)
#print(list_pam)
#text = ','.join(str(eleman)for eleman in list_pam )
#print(text)

#3
#chen_pam = []
#for i in range(5):
 #   a =(input("antre yon chif:"))
  #  chen_pam.append(a)
#print(chen_pam)
#b = [eleman.upper() for eleman in chen_pam]
#print(b)

#4
#lis = []
#for i in range(10):
 #   number = int(input("Entrez un nombre: "))
  #  lis.append(number)
   # if i % 3 == 0:
    #    lis2 = []
     #   lis2.append(lis[i])
      #  print(lis2, end=" ")

#print(lis)

#5
#lis_orijinal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#nouvo_lis = [lis_orijinal[i:i+3] for i in range(0, len(lis_orijinal), 3)]
#print(nouvo_lis)

#6
#list1 = [1, 2, 3, 4, 5, 6, 7, 3, 2, 4, 7]
#list2 = list(set(list1))
#print(list2)

#7
#lista = [1, 2, 3, 4, 5, 6]
#listb=[8, 3, 2, 4, 7]
#listc = []
#for i in lista:
 #   for x in listb:
  #      if i == x:
   #         listc.append(i)

#print(listc)

#8
#lista = [1, 2, 3, 4, 5, 6]
#listb=[8, 3, 2, 4, 7]
#listc = list(set(lista)-set(listb))
#listd = list(set(listb)-set(lista))
#liste = listc + listd
#print(liste)

#9
#lisa = []
#lisb = []
#dic = {
   # "nom": "Saintil",
  #  "prenom":"ralph",
 #   "age": 22
#}
#lisa = list(dic.keys())
#print(lisa)
#lisb = list(dic.values())
#print(lisb)

#10
#lisx = [1, 2, 4, 3, 5, 4, 3, 7]
#lisy = [2, 3, 8, 9, 6, 4, 3, 2]
#lisz = [9, 8, 5, 3, 2, 6, 1, 6]
#lisi = list(set(lisx))
#lisj = list(set(lisy))
#lisk = list(set(lisz))
#lisw = lisi+lisj+lisk
#lisq = set(lisw)
#print(lisq)

#master dictionnaire
#1
#dica = {
    #"nif": 1456,
    #"nom": "aliano",
   # "prenom":"charles",
  #  "niveau":"licence",
 #   "etat":"enbesil"
#}
#lis_vale = list(dica.values())
#print(lis_vale)

#2
#while True:
 # vale = input("antre yon vale ak akolad: ")
  #if vale.startswith("{") and vale.endswith("}"):
   # break
  #else:
   # print("vale a pa gen akolad ni devan ni deye")

#3
#dicb = {
 #  "nif": 1456,
  # "nom": "aliano",
   # "prenom":"charles",
    #"niveau":"licence",
    #"etat":"enbesil"}
#for kle in dicb:
 #   print(kle)

#4
#dicd = {
#   "nif": 1456,
 #  "nom": "aliano",
  #  "prenom":"charles",
   # "niveau":"licence",
    #"etat":"enbesil"}
#for vale in dicd.values():
 #   print(vale)

#5
#diksyone = {"ane1":2020, "ane2":2021, "ane3":2022, "ane4": 2023}
#kopi = {k:v for k, v in diksyone.items()}
#kopi["ane1"]=2021
#print("oji ", diksyone)
#print("fake ", kopi)

#6
#diksyone1 = {"lisans1":2020, "lisans2":2021, "lisans3":2022, "lisans4":2023, "nom":"saintil", "prenom":"ralph"}
#for k, v in diksyone1.items():
 #   if type(v) is str:
  #      diksyone1[k] = "_"+v+"_"
#print(diksyone1)

#7
#diksyone1 = {"lisans1":2020, "lisans2":2021, "lisans3":2022, "lisans4":2023, "nom":"saintil", "prenom":"ralph"}
#diksyone2 = {}
#for k, v in diksyone1.items():
 #   if type(v) is int:
  #      diksyone2[k] = v
#print(diksyone2)

#8
#diksyone1 = {"lisans1":2020, "lisans2":2021, "lisans3":2022, "lisans4":2023, "nom":"saintil", "prenom":"ralph"}
#lis_dik = list(diksyone1.items())
#print(lis_dik)

#9
#diksyone1 = {"lisans1":2020, "lisans2":2021, "lisans3":2022, "lisans4":2023, "nom":"saintil", "prenom":"ralph"}
#lis_dik = list(diksyone1.items())
#diksyone = dict(lis_dik)
#print(diksyone)

#10
#diksy1 = {
 #   "nom":"saintil",
  # "classe":"licence",
   # "age":22
#}

#diksy2 = {
 #   "nom": "Charles",
  #  "prenom": "aliano",
   # "classe": "licence",
    #"age": 25
#}

#diksy3 = {}

#for k in diksy1.keys() & diksy2.keys():
 #   if type(diksy1[k]) == type(diksy2[k]):
  #      diksy3[k] = diksy1[k] + diksy2[k]
   # else:
    #    diksy3[k] = str(diksy1[k]) + str(diksy2[k])

#for k in diksy1.keys() - diksy2.keys():
 #   diksy3[k] = diksy1[k]

#for k in diksy2.keys() - diksy1.keys():
 #   diksy3[k] = diksy2[k]

#print(diksy3)

import  random
import  string
import re
#master function
#1
#def enves(mo):
#    a =''.join(reversed(mo))
#    return a
#on_mo = input("antre yon mo svp: ")
#print(enves(on_mo))

#2
#def kod_aleyatwa(n):
 #   karakte_alfabet = string.ascii_letters
  #  kod = ''.join(random.choice(karakte_alfabet) for _ in range(n))
   # return kod
#kod = kod_aleyatwa(10)
#print("kod aleyatwa: ",kod)

#3
#def jenere(n):
#    karakte = string.ascii_letters
#    karakte_leyatwa = random.sample(karakte, n)
#    kod = ''.join(karakte_leyatwa)
#    return  kod

#kod = jenere(12)
#print("kod la: ", kod)

#4
#def jenere(n):
 #   karakte = string.ascii_letters+string.digits
  #  karakte_leyatwa = random.sample(karakte, n)
   # kod = ''.join(karakte_leyatwa)
   # return  kod
#kod = jenere(10)
#print(kod)

#5
#def jenere_slug(chenn):
    #chenn_san_espas = re.sub(r'\s', '-', chenn)
   # chenn_slug = re.sub(r'[^a-zA-Z0-9-]', '', chenn_san_espas)
  #  chenn_final = chenn_slug.lower()
 #   return chenn_final

#chenn = "ayiti pap peri tan ke soley la ap kontinye leve deye mon nou yo"
#slug = jenere_slug(chenn)
#print("SLUG:", slug)

#6
#def separe_yo(mo):
 #   for i in mo:
  #    mo_separe = ','.join(mo)
   # return mo_separe
#tex = input("antre yon pawol: ")
#print(separe_yo(tex))

#7
#def kripte(mo):
 #   alfabè = string.ascii_lowercase
  #  f_c = '_'.join([str(alfabè.index(k)+1)for k in mo.lower()])
   # return f_c
#a = input("antre yon pawol: ")
#print(kripte(a))

#8
#def dekripte_avek_endèks(mo_kripte):
#    alfabè = string.ascii_lowercase
#    endèks = mo_kripte.split('-')
#    mo_dekripte = ''.join([alfabè[int(endèk) - 1] for endèk in endèks])
#    return mo_dekripte

#mo_kripte = input("antre endeks let alfabet yo separe pa yire -: ")
#mo_dekripte = dekripte_avek_endèks(mo_kripte)
#print("Mo dekripte:", mo_dekripte)

#9
#def tupl(n,m):
 #   a = n
  #  b = m
   # c =n
    #a = m
    #b = c
    #tipl = (a,b)
    #return tipl
#print(tupl("travay","bon"))

#10
def inisyal_non(non):
    non = non.strip()  # Retire espas nan kòman ak fen non an
    non_konpoze = non.split()  # Separe non yo
    inisyal = ''

    for non in non_konpoze:
      if "-" not in non:
        inisyal += non[0].upper()  # Pran inisyal la epi mete li nan fòm majiskil
    return inisyal

non = "Jean Dupont"
inisyal = inisyal_non(non)
print(inisyal)
