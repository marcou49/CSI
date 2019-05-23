import sys

#ADN del ladrón

with open("dna.txt", "r") as adn:
    adn_culpable = adn.read()

#implementamos pelo
# Black: CCAGCAATCGC
# Brown: GCCAGTGCCG
# Blonde: TTAGCTATCGC

pelo = input("Teclea N si tienes el pelo negro, M si es marrón, R si es rubio ")

if pelo == "N":
    pelo = "CCAGCAATCGC"

elif pelo == "M":
    pelo = "GCCAGTGCCG"

elif pelo == "R":
    pelo = "TTAGCTATCGC"

if pelo not in adn_culpable:
  print("No es el culpable")
  sys.exit()

#implementamos cara
# Square: GCCACGG
# Round: ACCACAA
# Oval: AGGCCTCA

cara = input('Teclea C si tienes la cara cuadrada, R redonda, O ovalada ')

if cara == "C":
    cara = "GCCACGG"

elif cara == "R":
    cara = "ACCACAA"

elif cara == "O":
    cara = "AGGCCTCA"

if cara not in adn_culpable:
  print("No es el culpable")
  sys.exit()


#implementamos ojos
# Blue: TTGTGGTGGC
# Green: GGGAGGTGGC
# Brown: AAGTAGTGAC

ojos = input("Teclea A si tienes los azules, V verdes o M marrones ")

if ojos == "A":
    ojos = "TTGTGGTGGC"

elif ojos == "V":
    ojos = "GGGAGGTGGC"

elif ojos == "M":
    ojos = "AAGTAGTGAC"

if ojos not in adn_culpable:
  print("No es el culpable")
  sys.exit()


#implementamos raza
# White: AAAACCTCA
# Black: CGACTACAG
# Asian: CGCGGGCCG

raza = input("Teclea B si eres blanco, N de raza negra o A asiatico ")

if raza == "B":
    raza = "AAAACCTCA"

elif raza == "N":
    raza = "CGACTACAG"

elif raza == "A":
    raza = "AAGTAGTGAC"

if raza not in adn_culpable:
  print("No es el culpable")
  sys.exit()


#hombre o mujer
genero = input("Teclea M si es mujer o H si es hombre ")

if genero == "M":
    genero = "TGAAGGACCTTC"

elif genero == "H":
    genero = "TGCAGGAACTTC"


if genero in adn_culpable:
  print("Este es el culpable")