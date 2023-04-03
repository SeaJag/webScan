from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# l'exécutable Chrome 
# To Do : Remplacer par DVWA
chrome_options = Options()
chrome_options.binary_location = '/chemin/vers/le/fichier/chrome'

# Init Nav
driver = webdriver.Chrome(options=chrome_options)

# Open page
driver.get("https://www.example.com")

# Find all links
links = driver.find_elements_by_tag_name("a")

# Parcours des liens et récupération des URLs associées
urls = []
for link in links:
    url = link.get_attribute("href")
    if url is not None and url not in urls:
        urls.append(url)
        # Clique on link
        link.click()
        # Retour en arrière
        driver.back()

# Fermeture du navigateur
driver.quit()

# URLs récupérées
print(urls)
