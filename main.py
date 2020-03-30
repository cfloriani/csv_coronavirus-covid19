import json,csv
from urllib.request import urlopen

arq = urlopen('https://api.covid19api.com/all').read().decode('utf8') #usa api como fonte de dados
#arq = open('db.txt', 'r').read() #usa o db.txt como fonte de dados
fulldata = json.loads(arq)
data = {} #{'País':(Deaths,Confirmed,Recovered)}

#cria os indices com os paises
for x in fulldata:
	if x['Country'] not in data:
		data[x['Country']] = [0,0,0]

#verifica país a país os casos
for x in fulldata:
	if x['Status'] == 'deaths':
		if x['Cases'] > data[x['Country']][0]:
			data[x['Country']][0] = x['Cases']
	if x['Status'] == 'confirmed':
		if x['Cases'] > data[x['Country']][1]:
			data[x['Country']][1] = x['Cases']
	if x['Status'] == 'recovered':
		if x['Cases'] > data[x['Country']][2]:
			data[x['Country']][2] = x['Cases']

#imprime no csv
with open('export.csv','w') as arquivo:
	writer = csv.writer(arquivo)
	writer.writerow(('País', 'Mortes', 'Infectados','Recuperados'))
	for i in data:
		writer.writerow((i,data[i][0],data[i][1],data[i][2]))

#imprime na tela
'''
for i in data:
	print('Pais:' ,i)
	print('Mortes: ',data[i][0])
	print('Infectados: ',data[i][1])
	print('Recuperados: ',data[i][2])
	print('-------------------------------')
'''