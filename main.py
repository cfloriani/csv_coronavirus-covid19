import json,csv
from urllib.request import urlopen

arq = urlopen('https://api.covid19api.com/all').read().decode('utf8') #usa api como fonte de dados
fulldata = json.loads(arq)
dados = {} #{'País':(Deaths,Confirmed,Recovered)}

#cria os indices com os paises
for dado in fulldata:
	if dado['Country'] not in dados:
		dados[x['Country']] = [0,0,0]

#verifica país a país os casos
for dado in fulldata:
	if dado['Status'] == 'deaths':
		if dado['Cases'] > dados[dado['Country']][0]:
			dados[dado['Country']][0] = dado['Cases']
	if dado['Status'] == 'confirmed':
		if dado['Cases'] > dados[dado['Country']][1]:
			dados[dado['Country']][1] = dado['Cases']
	if dado['Status'] == 'recovered':
		if dado['Cases'] > dados[dado['Country']][2]:
			dados[dado['Country']][2] = dado['Cases']

#imprime no csv
with open('export.csv','w') as arquivo:
	writer = csv.writer(arquivo)
	writer.writerow(('País', 'Mortes', 'Infectados','Recuperados'))
	for i in dados:
		writer.writerow((i,dados[i][0],dados[i][1],dados[i][2]))
