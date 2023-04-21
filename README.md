# webScan

# Context

- WebScan is a web application scanner searching for common security vulnerabilities (SQL injections, XSS injection and LFI injection).
- WebScan Generate automatically a PDF report showing the vulnerabilities detected and the input used to detetct. As well a recommendations for patching the vulnerabilities.

## demonstration video :
You can see a demo video on `Demo_Equipe_Cinq.mp4`

# Requirement
Before anythinge else you have to install docker at your machine. 
(Go check Dockerfile)

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
Login into web interface and at the end of page there are `Create / Reset Database`.
Click at this button and relogin at the web interface. You will see the challenges.

## 2. Install dependancies

```bash
pip3 install -r requirements.txt
```

## 3. Run script :

```bash
python3 src/main.py
```
This will generate : 
- A quick report on the terminal
- A detailed report in PDF

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

- [x] Mettre à jour le README

- [x] Développer les tests unitaires

- [x] Développer la version finale du rapport

- [x] Documentation de prise en main avec Doxygen

- [x] Faire une vidéo de démo

```

```
