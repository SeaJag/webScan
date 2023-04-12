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

## Premier jalon :  

* [x] Création dépôt Git 

* [x] Définition du scope et répartition des taches pour les différents membres de l’équipe 

* [x] Choix des outils utilisés

* [x] Déployer DVWA sur une VM

* [x] Dev le scrapper des toutes les pages du site Web

## Second jalon :  

* [x] Initier le programme pour scrapper l'application DVWA

* [ ] Avoir un PoC sur une injection 


## Troisième jalon : 

* [ ] Tester les inputs de toutes les pages avec plusieurs injections

* [ ] Rédiger une Doc / Readme

* [ ] Générer un rapport pour chaque faille détectée

* [ ] Rédaction de docuementation sur les outils utilisées 
