# portScan
A l'image de Nmap, ce script permet de scanner des ports.
Ce code est un programme de scan de ports en Python. Il utilise le module argparse pour analyser les arguments de ligne de commande et le module socket pour la communication réseau.

Le programme permet de spécifier une adresse IP ou un nom de domaine cible avec l'option -H et une plage de ports à scanner avec l'option -p. Le programme crée ensuite un thread pour
chaque port dans la plage spécifiée et essaie de se connecter à l'adresse cible sur ce port. Si la connexion réussit, le programme affiche un message indiquant que le port est ouvert.
Sinon, le programme affiche un message indiquant que le port est fermé.
