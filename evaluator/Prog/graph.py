import matplotlib.pyplot as plt
import json

def lire_json(chemin):
    with open (chemin) as json_data:
        dist = json.load(json_data)
    return dist

donnees = lire_json("../result/resultat.json")
print(donnees)

trad_name = []
liste_jaccard = []
liste_cosine = []

for key, value in donnees.items():
    #print(key)
    print(value)
    fichier = key.split('--')[0]
    trad = fichier.split('_')[-1]
    trad_name.append(trad)
    for cle, valeur in value.items():
        if cle == 'cosine':
            liste_cosine.append(valeur[0])
        else:
            liste_jaccard.append(valeur[0])

plt.scatter(trad_name, liste_cosine, label='cosine', s=10, marker="s")
plt.scatter(trad_name, liste_jaccard, label='cosine', s=10, marker="s")
plt.ylabel('Distances')
plt.xlabel('Vesion génerer')
plt.axis([-1,6,0,1])
plt.legend(loc="lower left", ncol=2, bbox_to_anchor=(0.1,1))
plt.tight_layout()

plt.show()