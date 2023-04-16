from login import login
from vulnerability_checker import get_url_list, check_vulnerabilities

host = 'http://172.17.0.1'

session = login(host)

toCheck = host + '/'
url_list = get_url_list(session, toCheck)

print("\n===========================   Liste des pages à tester   =======================================")
print(url_list)

print("\n================================   Rapport des failles détectées   ===========================================")
xss_count, sql_count, lfi_count = check_vulnerabilities(session, url_list, host)
print(f"\n\nBILAN : \nNombre de failles détectées : {xss_count + sql_count + lfi_count} \nXSS Injection = {xss_count}\nSQL Injection = {sql_count}\nLFI = {lfi_count}")

print("\n=====================================       Recommendation Patch Vulnérabilités       ==============================================")
if (xss_count > 0):
    print("\n***************Voici nos recommendations pour les failles XSS***************\n")
    f = open("/home/kali/projectpython/webScan/src/Recommendation/XSS_recommendation.txt", "r")
    print(f.read())
    f.close()
if (sql_count > 0):
    print("\n***************Voici nos recommendations pour les failles SQL***************\n")
    f = open("/home/kali/projectpython/webScan/src/Recommendation/SQL_recommendation.txt", "r")
    print(f.read())
if (lfi_count > 0):
    print("\n***************Voici nos recommendations pour les failles LFI***************\n")
    f = open("/home/kali/projectpython/webScan/src/Recommendation/LFI_recommendation.txt", "r")
    print(f.read())


print("\n=====================================       Fin du Rapport       ==============================================")