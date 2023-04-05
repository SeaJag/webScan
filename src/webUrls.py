import requests
from bs4 import BeautifulSoup

# URL DVWA
url = "http://192.168.1.27/dvwa/"

# requête GET
response = requests.get(url)

# Parsez le contenu HTML de la repp
soup = BeautifulSoup(response.content, "html.parser")

# Chercher les liens
links = soup.find_all("a")

# Lister les liens
for link in links:
    print(link.get("href"))
