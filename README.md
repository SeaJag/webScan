# webScan

# Context

WebScan is a web application scanner searching for common security vulnerabilities as SQL injections, XSS flaws, and LFI injection.
WebScan Generate a PDF report showing the vulnerability (the input) as well and the recommendations for patching the vulnerabilities.

# Fonctionnement du programme :

- Input : Takes as parameter a link
- Output : Reporting with vulnerabilities and recommendations

# Requirement
Before anythinge else we will install docker at your machine.

[Install docker desktop on Ubuntu](https://docs.docker.com/desktop/install/ubuntu)

# Lunch program : 

## 1. Run DVWA :

```bash
docker run --rm -it -d -p 80:80 vulnerables/web-dvwa
```

Go to browser connect to DVWA with 127.0.0.1 host:
```bash
admin:password
```
Login into web interface and at the end of page there are Create / Reset Database
click at this button and relogin at the web interface. We will see the different challenge now.

## 2. Install dependancy

```bash
pip3 install -r requirements.txt
```

## 3. Run script :

```bash
python3 src/main.py
```

## 4. Run test :
```bash
python3 src/py_test.py
```

# Build Doc:

```bash
doxygen Doxyfile
```

# Planning :

## Premier jalon (07/04/2023) :

- [x] Création dépôt Git

- [x] Définition du scope et répartition des taches pour les différents membres de l’équipe

- [x] Choix des outils utilisés

- [x] Déployer DVWA sur une VM

- [x] Dev le scrapper des toutes les pages du site Web

## Second jalon (15/04/2023) :

- [x] Initier le programme pour scrapper l'application DVWA

- [x] Avoir un PoC sur une injection

- [x] Tester les inputs de toutes les pages avec plusieurs injections (injection XSS, SQL et LFI)

- [x] Développer une V1 du rapport : Type de faille - Page vulnérable - Payload utilisée

## Troisième jalon (21/04/2023) :

- [x] Rédiger une Doc / Mettre à jour le README

- [x] Doxygen

- [x] Développer les tests unitaires

- [x] Développer la version finale du rapport

- [x] Documentation de prise en main

- [x] Faire une vidéo de démo

```

```
