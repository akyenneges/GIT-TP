import csv

# Ouvrir le fichier csv
with open('data.csv', 'r') as f:
    # Créer un objet csv à partir du fichier
    obj = csv.reader(f)
    a = 0

    for ligne in obj:
        print(ligne)
        a+=1

    print ('Il y a ',a,' lignes dans le fichier')
