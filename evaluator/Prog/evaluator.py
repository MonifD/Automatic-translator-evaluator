import glob
import json
import os
import sklearn
from sklearn.metrics import DistanceMetric
from sklearn.feature_extraction.text import CountVectorizer

def lire_corpus(chemin):
    with open(chemin, 'r') as f:
        texte = f.read()
    return texte

def lire_json(chemin):
    with open (chemin) as json_data:
        dist = json.load(json_data)
    return dist

def stocker(chemin, contenu):
    w = open(chemin, 'w')
    w.write(json.dumps(contenu, indent=2))
    w.close()

def distances(texte1, texte2, metric_names):
    V = CountVectorizer(analyzer="word")
    X = V.fit_transform([texte1, texte2]).toarray()
    if metric != "cosine":
        dist = DistanceMetric.get_metric(metric_names)
        distance_tab1 = dist.pairwise(X)
        liste_resultat_dist2 = []
        liste_resultat_dist2.append(distance_tab1[0][1])
    else:
        distance_tab1 = sklearn.metrics.pairwise.cosine_distances(X)
        liste_resultat_dist2 = []
        liste_resultat_dist2.append(distance_tab1[0][1])
    return liste_resultat_dist2


liste_metric = ["jaccard", "cosine"]
chemin = "../DATA/*"
stocke_result="../result/"
liste_trad = []
liste_ref = []

i = 0
for path in glob.glob(chemin):
    print(path)
    for path_texte in glob.glob("%s/*.txt"%path):
        print(path_texte)
        nom_fichier,_=os.path.splitext(os.path.basename(path_texte))
        #print(path_texte)
        texte = lire_corpus(path_texte)
        if "ref" in path_texte:
            liste_ref.append(nom_fichier)
            liste_ref.append(texte)
        elif "VO" in path_texte:
            continue
        else:
            liste_trad.append([nom_fichier, texte])
            #print(liste_trad)

dico_dist = {}

for tt in liste_trad:
    trad = tt[1]
    ref = liste_ref[1]
    dico_dist[f"{liste_ref[0]} -- {tt[0]}"] = {}
    for metric in liste_metric:
        dico_dist[f"{liste_ref[0]} -- {tt[0]}"][metric] = distances(ref, trad, metric)
#print(dico_dist)

        # V = CountVectorizer(analyzer="word")
        # X= V.fit_transform([ref, trad]).toarray()
        # if metric != "cosine":
        #     dist = DistanceMetric.get_metric(metric)
        #     distance_tab1=dist.pairwise(X)
        #     liste_resultat_dist2 = []
        #     liste_resultat_dist2.append(distance_tab1[0][1])
        #     dico_dist[tt[0], liste_ref[0]][metric]=liste_resultat_dist2
        # else:
        #     distance_tab1=sklearn.metrics.pairwise.cosine_distances(X)
        #     liste_resultat_dist2 = []
        #     liste_resultat_dist2.append(distance_tab1[0][1])
        #     dico_dist[tt[0], liste_ref[0]][metric] = liste_resultat_dist2

#print(dico_dist)

stocker("%sresultat.json"%stocke_result , dico_dist)

