from datetime import date, time, datetime, timedelta
from stores.models import Store

def parseField(field):
  file = field.read().decode('utf-8')
  fileList = file.split("\r\n")
  listData = []
  for i in fileList:
    data = { 
      "tipo": i[0:1],
      "data": i[1:9],
      "valor": (int(i[9:19]) / 100),
      "cpf": i[19:30],
      "cartao": i[30:42],
      "hora": date.fromtimestamp(int(i[42:48])),
      "dono_da_loja": i[48:62],
      "nome_loja": i[62:81]
    }
    # Store.objects.create(**data)
    listData.append(data)
  
  exitFiles = ["2","3","9"]
  
  storages = []
  for i in listData:
    if i["nome_loja"] not in storages:
      storages.append(i["nome_loja"])
  
  result = []
  for i in storages:
    totalValue = 0
    for value in listData:
      if i == value["nome_loja"]:
        if value["tipo"] in exitFiles:
          totalValue -= int(value["valor"])
        else:
          totalValue += int(value["valor"])
          
    result.append({i, totalValue})
  return result