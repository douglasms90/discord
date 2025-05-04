import requests
import json

# Post(Create)
link = "https://database-11bec-default-rtdb.firebaseio.com/"
dados = {
    "Act":[
        {
            "rf":[
                {
                    "id":101,
                    "nm":"vsback",
                    "pr":0,
                    "pm":0,
                    "qt":0
                },
                {
                    "id":102,
                    "nm":"selic",
                    "pr":0,
                    "pm":0,
                    "qt":0
                },
                {
                    "id":103,
                    "nm":"lci-26",
                    "pr":0,
                    "pm":0,
                    "qt":0
                },
                {
                    "id":104,
                    "nm":"ipca26",
                    "pr":0,
                    "pm":0,
                    "qt":0
                },
                {
                    "id":105,
                    "nm":"lci-26",
                    "pr":0,
                    "pm":0,
                    "qt":0
                },
            ]
        }
    ]
}
req = requests.post(f"{link}/discord/.json", data=json.dumps(dados))

# Patch(Update)
#dados = {'nome':'Douglas'}
#id = '-OPHWlWesheJbcvFUuoN'
#req = requests.patch(f"{link}/discord/tests/{id}/.json", data=json.dumps(dados))

# Get(Read)
req = requests.get(f'{link}/.json')
print(req.text)

