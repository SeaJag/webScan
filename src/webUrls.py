import requests
import re
from bs4 import BeautifulSoup

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
    url_list.append(link.get("href"))

# Imprimer la liste des URLs
print(url_list)