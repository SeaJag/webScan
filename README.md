# webScan

# Contexte

Scanneur d'application web à la recherche de failles de sécurité courantes telles que les injections SQL, les failles XSS, les failles CSRF (check présence d’un token ou non par exemple ,..). Faire un reporting montrant la faille (l’input) ainsi que des recommandations pour patcher les failles.

# Fonctionnement du programme : 
- Input : Prend en paramètre un lien
- Output : Reporting avec les failles ainsi que des recommandations 


# Planning : 

## Premier jalon :  

|X| Création dépôt Git 

|X| Définition du scope et répartition des taches pour les différents membres de l’équipe 

|X| Choix des outils utilisés

|X| Déployer DVWA sur une VM

|X| Dev le scrapper des toutes les pages du site Web

## Second jalon :  

| . | Initier le programme pour scrapper l'application DVWA

| . | Scrapper l'ensemble des inputs de l'application 

| . | Tester les inputs avec différentes injections (sql, csrf...)


## Troisième jalon : 

| . | Générer un rapport pour chaque faille détectée

| . | Rédaction de docuementation sur les outils utilisées 
