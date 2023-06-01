# 3.1
# Kirjoita ohjelma, jossa käyttäjä kirjoittaa oman nimensä ja ohjelma tervehtii käyttäjää muodossa:
# "Terve Aarni"
nimi = input("Kirjoita Nimesi: ")
print("Terve "+ nimi)

# 3.2
# Kirjoita ohjelma, johon käyttäjä syöttää luvun. Ohjelma tulostaa luvusta kaksin kertaisen arvon.
numeraali = input("anna luku: ")
numeraali = int(numeraali)
print(numeraali*2)

# 3.3
# Kirjoita ohjelma, joka laskee käyttäjän syöttämän arvon vähennyksen sadasta. Ohjelma tulostaa:
# ”Sadasta vähennettynä jää xxx”, korvaa xxx vähennyksellä.

ferrari = input ("anna luku: ")
ferrari = int (ferrari)

print ("sadasta vähennettynä jää: " + str (100 - ferrari))

# 3.4
# Kirjoita ohjelma, joka muuttaa luvun 12.53 kokonaisluvuksi. Tulosta muutettu luku

print (int(12.53))
