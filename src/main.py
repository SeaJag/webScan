from login import login
from vulnerability_checker import get_url_list, check_vulnerabilities

host = 'http://172.17.0.1'

session = login(host)

toCheck = host + '/'
url_list = get_url_list(session, toCheck)

print("\n===========================   Liste des pages à tester   =======================================")
print(url_list)

print("\n================================   Rapport des failles détectées   ===========================================")
check_vulnerabilities(session, url_list, host)
print("====================================       Fin du Rapport       ==============================================")