import json
from datetime import datetime

fileName = "./Resources/Data.json"

def TransformToJson(Aplicacion,Ping):
    now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    jsonObject = {
        "Fecha": now,
        "Aplicacion": Aplicacion,
        "Ping": Ping
    }

    print(jsonObject 
          )

    file = open(fileName, "w")
    json.dump(jsonObject, file)
    file.close()