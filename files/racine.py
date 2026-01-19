def decoupe_en_tranche(n):
    res = []
    while n > 0:
        res = [n % 10] + res
        n   = n // 10
    return res

def extraire_racine(nb, decimales):
    tranches = decoupe_en_tranche(nb) + decimales*[0]
    nb_abaisse = tranches.pop(0)
    
    x = 0
    while (x+1)**2 <= nb_abaisse:
        x = x + 1
        
    racine = x
    reste  = nb_abaisse - x**2
    
    while tranches != []:
        nb_abaisse = 100*reste + tranches.pop(0)
        
        chiffre = 0
        while (20*racine + (chiffre+1))*(chiffre+1) <= nb_abaisse:
            chiffre = chiffre + 1
        
        reste = nb_abaisse - (20*racine+chiffre)*chiffre
        racine = 10*racine + chiffre
        
    return racine/10**decimales