import requests, re

url = 'https://econodata.com.br/consulta-empresa?filtro=60499310000124'

response = requests.get(url)

text = response.text

with open('empresas.html', 'w') as f: f.write(text)

cnpjs = re.findall(r'\d\d\.\d\d\d\.\d\d\d\/\d\d\d\d\-\d\d', text)

print(cnpjs)
