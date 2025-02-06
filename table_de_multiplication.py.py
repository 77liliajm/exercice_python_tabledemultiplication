#exo d'algorithmique : table de multiplication


#but : affichage d'une table de multiplication

#saisie de la valeur dont la table de multplication va être affiché
val = input("Entrez un nombre entier = ")
if not (1 <= int(val) <= 10):
    print("Veuillez saisir une valeur comprise entre 1 et 10")

#initialisation du coefficient multiplicateur de la table
k = 1
for k in range(1, 11):
    print(int(val), "*", k, "=", int(val)*k)