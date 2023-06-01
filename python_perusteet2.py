
# 2.1
# Kirjoita ohjelma, jossa on muuttuja ja se tulostetaan. Sitten muuta muuttujan arvoa niin, että sen arvo
# kasvaa kaksin kertaiseksi. Tulosta muuttuja.
keppi = 33
print (keppi)
keppi*= 2
print (keppi)

# 2.2
# Kirjoita ohjelma, jossa on kaksi muuttujaa. Kasvata ensimmäistä muuttujaa toisen muuttujan arvolla.
# Tulosta kasvatettu muuttuja.
muuttuja = 12
ruuti = 13
muuttuja += ruuti
print (muuttuja)

# 2.3
# Kirjoita ohjelma, jossa on kaksi muuttujaa, joiden arvoina on itse valitsemasi numerot. Laske ensimmäisen
# muuttujan arvoa kahdella ja sitten laske ensimmäisen muuttujan arvoa toisen muuttujan arvolla.
ristikko =  40
ranta = 55
ristikko -= 2
ristikko -= ranta
print(ristikko)

# 2.4
# Kirjoita ohjelma, jossa on kaksi muuttujaa, joiden arvoina on itse valitsemasi numerot. Kasvata molempia
# lukuja niiden summalla. Kokeile esimerkin arvoilla, jolloin sinun tulisi saada esimerkin mukainen lopputulos.
# Esimerkki:
# muuttuja1 = 5
# muuttuja2 = 10
# muuttuja1 -> 20
# muuttuja2 -> 25

aalto = 10
vesi = 20
hiekka = aalto + vesi
aalto += hiekka
vesi += hiekka
print(vesi, aalto)
