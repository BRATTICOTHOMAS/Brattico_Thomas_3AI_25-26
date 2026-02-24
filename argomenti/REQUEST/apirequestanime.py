import requests
import json
#url a nostra scelta
url = "https://emojihub.yurace.pro/api/all"
response = requests.get(url)
if response.status_code!=200:
    print("Errore nel contattare il servizio online!")
else:
    data = response.json()
    print("--- Ecco i primi 5 risultati ---")
    test=json.loads(response.text)
    for emoji in data[:5]:
        nome = emoji.get('name')
        categoria = emoji.get('category')
        codice_html = emoji.get('htmlCode')[0] 
        print(f"Nome: {nome}")
        print(f"Categoria: {categoria}")
        print(f"Codice HTML: {codice_html}")
        print("-" * 20)
        
    print(test)
    for emoji in data[:90]:

        emoji_dict = {emoji['name'].lower(): emoji['category']}
        print(emoji_dict)
        print(emoji_dict[2])
    nom=input("inserisci il nome della emoji per trovare la sua corrispettiva categoria: ").islower()
    
   # print(f"La categoria di questa emoji è: {emoji_dict[]}")
   