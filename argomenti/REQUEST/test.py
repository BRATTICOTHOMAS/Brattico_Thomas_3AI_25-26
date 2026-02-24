import requests
import json
#url a nostra scelta
url = "https://emojihub.yurace.pro/api/search?q="
nom=input("nome emoji: ")
response = requests.get(url+nom)
if response.status_code!=200:
    print("Errore nel contattare il servizio online!")
else:

    da=json.loads(response.json())
        
    print(da)
    