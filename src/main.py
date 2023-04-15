from login import login
from vulnerability_checker import get_url_list, check_vulnerabilities

session = login()

toCheck = 'http://172.17.0.1' + '/'
url_list = get_url_list(session, toCheck)

print("\n===========================   Liste des pages à tester   =======================================")
print(url_list)

print("\n===========================   Rapport des failles détectées   =======================================")
check_vulnerabilities(session, url_list)
print("================================       Fin du Rapport       =========================================")