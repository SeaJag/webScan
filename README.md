# webScan

# Context

Web application scanner searching for common security vulnerabilities such as SQL injections, XSS flaws, and CSRF flaws (checking for the presence of a token, for example). Generate a report showing the vulnerability (the input) as well as recommendations for patching the flaws.

# Fonctionnement du programme : 
- Input : Prend en paramètre un lien
- Output : Reporting avec les failles ainsi que des recommandations 

# Dockerfile

## Build image :
```bash
    docker build -t webscan .
```

# Lancer le programme : 
## Run DVWA : 
## Run le script : 


# Planning : 

## Premier jalon (07/04/2023) :  

* [x] Création dépôt Git 

* [x] Définition du scope et répartition des taches pour les différents membres de l’équipe 

* [x] Choix des outils utilisés

* [x] Déployer DVWA sur une VM

* [x] Dev le scrapper des toutes les pages du site Web

## Second jalon (15/04/2023) :  

* [x] Initier le programme pour scrapper l'application DVWA

* [x] Avoir un PoC sur une injection 

* [x] Tester les inputs de toutes les pages avec plusieurs injections (injection XSS, SQL et LFI)

* [x] Développer une V1 du rapport : Type de faille - Page vulnérable - Payload utilisée

## Troisième jalon (21/04/2023) : 

* [ ] Rédiger une Doc / Mettre à jour le README

* [x] Doxygen

* [ ] Développer les tests unitaires

* [ ] Développer la version finale du rapport

* [ ] Documentation de prise en main

* [ ] Faire une vidéo de démo
