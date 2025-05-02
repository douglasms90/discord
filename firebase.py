import requests
import json

# Post(Create)
link = "https://database-11bec-default-rtdb.firebaseio.com/"
#dados = {'nome':'Medeiros'}
#req = requests.post(f"{link}/discord/tests/.json", data=json.dumps(dados))

# Patch(Update)
dados = {'nome':'Douglas'}
id = '-OPHWlWesheJbcvFUuoN'
req = requests.patch(f"{link}/discord/tests/{id}/.json", data=json.dumps(dados))
