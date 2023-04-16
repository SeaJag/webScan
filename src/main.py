from login import login
from vulnerability_checker import get_url_list, check_vulnerabilities
from fpdf import FPDF
import pandas as pd
import datetime

date = datetime.datetime.now()

host = 'http://172.17.0.1'

session = login(host)

toCheck = host + '/'
url_list = get_url_list(session, toCheck)

print("\n===========================   Liste des pages à tester   =======================================")
print(url_list)

print("\n================================   Rapport des failles détectées   ===========================================")
xss_count, sql_count, lfi_count = check_vulnerabilities(session, url_list, host)
print(f"\n\nBILAN : \nNombre de failles détectées : {xss_count + sql_count + lfi_count} \nXSS Injection = {xss_count}\nSQL Injection = {sql_count}\nLFI = {lfi_count}")

#print("\n=====================================       Recommendation Patch Vulnérabilités       ==============================================")
#if (xss_count > 0):
#    print("\n***************Voici nos recommendations pour les failles XSS***************\n")
#    f = open("/home/kali/projectpython/webScan/src/Recommendation/XSS_recommendation.txt", "r")
#    print(f.read())
#    f.close()
#if (sql_count > 0):
#    print("\n***************Voici nos recommendations pour les failles SQL***************\n")
#    f = open("/home/kali/projectpython/webScan/src/Recommendation/SQL_recommendation.txt", "r")
#    print(f.read())
#if (lfi_count > 0):
#    print("\n***************Voici nos recommendations pour les failles LFI***************\n")
#    f = open("/home/kali/projectpython/webScan/src/Recommendation/LFI_recommendation.txt", "r")
#    print(f.read())


print("\n=====================================       Fin du Rapport       ==============================================")

# cell height
ch = 8
class PDF(FPDF):
    def __init__(self):
        super().__init__()
    def header(self):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'WebScan', 0, 3, 'C')
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', '', 12)
        self.cell(0, 8, f'Page {self.page_no()}', 0, 0, 'C')

# Load or prepare pandas DataFrame
df = pd.DataFrame({'Vulnerabilities' : ['XSS', 'LFI', 'SQL'], 'Numbers' : [f"{xss_count}", f"{lfi_count}", f"{sql_count}"]})

#Generate PDF        
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 28)
pdf.cell(w=0, h=20, txt="Vulnerability report", ln=1)
pdf.set_font('Arial', '', 12)
pdf.cell(30, ch, f'Date of the report : {date}', 0)
pdf.ln(ch)
pdf.ln(ch)
pdf.multi_cell(w=0, h=5, txt="We have scanned the entire web application, here is a report summarizing all the vulnerabilities as well as the measures to take to correct these flaws.")

#list of pages to be tested
pdf.set_font('Arial', 'B', 20)
pdf.cell(w=0, h=20, txt="List of pages to be tested", ln=1)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 5, f"{url_list}", 0)

#Report of detected flaws
nbofflaws = {xss_count + sql_count + lfi_count}
pdf.set_font('Arial', 'B', 20)
pdf.cell(w=0, h=15, txt="Report of detected flaws", ln=1)
if (nbofflaws != 0) :
    pdf.set_font('Arial', 'I', 16)
    pdf.set_text_color(r= 255, g= 0, b = 0)
    pdf.multi_cell(0, 8, f"Warning ! We discovered a total of {xss_count + sql_count + lfi_count} flaws !", 0)
    pdf.set_text_color(r= 0, g= 0, b = 0)
else :
    pdf.set_font('Arial', 'I', 16)
    pdf.set_text_color(r= 0, g= 125, b = 0)
    pdf.multi_cell(0, 8, f"Your web application is well protected, we did not discover any vulnerabilities.", 0)
    pdf.set_text_color(r= 0, g= 0, b = 0)
# Table Header
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, ch, 'Vulnerabilities', 1, 0, 'C')
pdf.cell(40, ch, 'Numbers', 1, 1, 'C')
# Table contents
pdf.set_font('Arial', '', 16)
for i in range(0, len(df)):
    pdf.cell(40, ch, df['Vulnerabilities'].iloc[i], 1, 0, 'C')   
    pdf.cell(40, ch, df['Numbers'].iloc[i], 1, 1, 'C')



#Recommendation
pdf.set_font('Arial', 'B', 20)
pdf.cell(w=0, h=20, txt="Recommendation", ln=1)
pdf.set_font('Arial', 'B', 16)
pdf.cell(w=0, h=13, txt="XSS exploit", ln=1)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(w=0, h=5, txt="XSS injections belong to the category of code injection vulnerabilities in the same way as SQL injections. However, to discover and exploit an XSS vulnerability, an attacker must inject malicious code via the client-side input parameters.")
pdf.ln(2)
pdf.set_font('Arial', 'I', 12)
pdf.multi_cell(w=0, h=5, txt="How to defend against it ?")
pdf.set_font('Arial', '', 12)
pdf.multi_cell(w=0, h=5, txt="At the PHP code level :")
pdf.multi_cell(w=0, h=5, txt="- The XSS attack is due to input coming from the outside (thus untrusted). The solution is therefore to filter the user's input by applying functions such as addslashes() or strip_tags() which remove all tags contained in the input string.")
pdf.multi_cell(w=0, h=5, txt="- Only a certain maximum length should be allowed for entries by checking it with the strlen() function or by systematically truncating it with the substr() function.")
pdf.multi_cell(w=0, h=5, txt="At the PHP code level :")
pdf.multi_cell(w=0, h=5, txt="- Set the magic_quotes_gpc directive in php.ini. This will automatically escape all special characters (including single and double quotes) in strings from outside the system. -> magic_quotes_gpc = On")
pdf.multi_cell(w=0, h=5, txt="CSP :")
pdf.multi_cell(w=0, h=5, txt="- Apply the Content Security Policy mechanism. CSP (Content Security Policy) script rules must be defined. These allow you to authorise content according to a list that you decide and thus prohibit the loading of specific types of content. You can thus define whether external scripts can be loaded, whether inline scripts can be executed, whether resources can be loaded from the same origin as the main page, etc..")

pdf.set_font('Arial', 'B', 16)
pdf.cell(w=0, h=13, txt="LFI exploit", ln=1)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(w=0, h=5, txt="An LFI vulnerability aims to include external files at code execution time. The vulnerability is created because there is not enough checking of the website entries.")
pdf.ln(2)
pdf.set_font('Arial', 'I', 12)
pdf.multi_cell(w=0, h=5, txt="How to defend against it ?")
pdf.set_font('Arial', '', 12)
pdf.multi_cell(w=0, h=5, txt="At the PHP code level :")
pdf.multi_cell(w=0, h=5, txt="- Filtering user input. Similar to the other attacks, the best way in php to prevent this is to filter the inputs. Since the GET parameter passed by the hacker is often too long, you should start by limiting the allowed length.")
pdf.multi_cell(w=0, h=5, txt="At the server configuration level :")
pdf.multi_cell(w=0, h=5, txt="- By modifying the php engine configuration file called php.ini. This is a text file that contains a set of directives that allow you to customise certain aspects of the PHP engine's behaviour. magic_quotes_gp can be used to automatically escape special characters from incoming strings (which come from forms, URL bars and cookies). It actually acts like the addslashes function but in an automated way. -> magic_quotes_gpc = On")
pdf.multi_cell(w=0, h=5, txt="- There is a directive that allows you to specify whether or not to allow external files to be retrieved for inclusion at runtime. On the php.ini file, you need to disable the following directive -> allow_url_fopen = Off")

pdf.set_font('Arial', 'B', 16)
pdf.cell(w=0, h=13, txt="SQL exploit", ln=1)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(w=0, h=5, txt="SQL injections belong to the category of code injection vulnerabilities in the same way as XSS injections. It involves adding an unintended query to an SQL query to interact with the database. An SQL flaw allows data to be stolen or modified, or even remote code to be executed.")
pdf.ln(2)
pdf.set_font('Arial', 'I', 12)
pdf.multi_cell(w=0, h=5, txt="How to defend against it ?")
pdf.set_font('Arial', '', 12)
pdf.multi_cell(w=0, h=5, txt="At the PHP code level :")
pdf.multi_cell(w=0, h=5, txt="- Filtering user input. Anything the user may submit to the server is considered foreign and potentially hostile content. Therefore, before allowing input to pass, it must be filtered.One can simply escape special characters from submitted strings using PHP functions like addslashes() or mysql_real_escape_string(). One can also apply regular expressions to check if the string represents such a pattern as with the preg_match() function and also check the length of the string with the strlen() function.")
pdf.multi_cell(w=0, h=5, txt="- Use the PDO object. It provides full immunity to SQL injections if you separate the data from the processing (the queries prepared with the query markers or named parameters).")
pdf.multi_cell(w=0, h=5, txt="- Do a two-step authentication. Instead of checking the login and the password in the same request, we split this treatment in two. First we ask for the login, and if this is correct we then ask for the password.")
pdf.multi_cell(w=0, h=5, txt="At the server configuration level :")
pdf.multi_cell(w=0, h=5, txt="- By modifying the php engine configuration file called php.ini. This is a text file that contains a set of directives that allow you to customise certain aspects of the PHP engine's behaviour. The magic_quotes_gpc directive can be used to automatically escape special characters in incoming strings (which come from forms, URL bars and cookies). It actually acts like the addslashes() function but in an automated way. -> magic_quotes_gpc = On")


pdf.output(f'./Vulnerability report.pdf')
