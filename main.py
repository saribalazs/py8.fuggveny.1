'''
1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza! 
A program tartalmazza a függvény hívását is!
'''
def osszegzo():
    p = sum(lista)
    return p

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(osszegzo())
