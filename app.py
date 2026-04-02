import requests, re

url = 'https://econodata.com.br/consulta-empresa?filtro=60499310000124'

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'})

text = response.text

with open('empresas.html', 'w') as f: f.write(text)

cnpjs = re.findall(r'\d\d\.\d\d\d\.\d\d\d\/\d\d\d\d\-\d\d', text)

print(cnpjs)
