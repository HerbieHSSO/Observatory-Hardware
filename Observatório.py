import requests
from bs4 import BeautifulSoup
import smtplib
import openpyxl
from openpyxl import Workbook
from datetime import date
excel = Workbook()
R51600AF = 'https://www.kabum.com.br/produto/107545/processador-amd-ryzen-5-1600-cache-19mb-3-2ghz-3-6ghz-max-turbo-am4-yd1600bbafbox'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}




page_R51600AF = requests.get(R51600AF, headers=headers)
soup_R51600AF = BeautifulSoup(page_R51600AF.content,'html.parser')


title_R51600AF = soup_R51600AF.find(itemprop='name').get_text()
price_R51600AF = soup_R51600AF.find('span', itemprop='offers').find('strong').get_text()
print(title_R51600AF)
print(price_R51600AF)




R32200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=94723'

page_R32200G = requests.get(R32200G, headers=headers)
soup_R32200G = BeautifulSoup(page_R32200G.content,'html.parser')

title_R32200G = soup_R32200G.find(itemprop='name').get_text()
price_R32200G = soup_R32200G.find('span', class_='preco_desconto_avista-cm').get_text()
print(title_R32200G)
print(price_R32200G)




R52600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=95557'
page_R52600 = requests.get(R52600, headers=headers)
soup_R52600 = BeautifulSoup(page_R52600.content,'html.parser')

title_R52600 = soup_R52600.find(itemprop='name').get_text()
price_R52600 = soup_R52600.find('span', class_='preco_desconto_avista-cm').get_text()
print(title_R52600)
print(price_R52600)


R53600 = 'https://www.kabum.com.br/produto/102438/processador-amd-ryzen-5-3600-cache-32mb-3-6ghz-4-2ghz-max-turbo-am4-sem-v-deo-100-100000031box'
page_R53600 = requests.get(R53600, headers=headers)
soup_R53600 = BeautifulSoup(page_R53600.content,'html.parser')

title_R53600 = soup_R53600.find(itemprop='name').get_text()
price_R53600 = soup_R53600.find('span', itemprop='offers').find('strong').get_text()

print(title_R53600)
print(price_R53600)




R72700 = 'https://www.kabum.com.br/produto/95564/processador-amd-ryzen-7-2700-cooler-wraith-spire-cache-20mb-3-2ghz-4-1ghz-max-turbo-am4-sem-v-deo-yd2700bbafbox'
page_R72700 = requests.get(R72700, headers=headers)
soup_R72700 = BeautifulSoup(page_R72700.content,'html.parser')

title_R72700 = soup_R72700.find(itemprop='name').get_text()
price_R72700 = soup_R72700.find('span', itemprop='offers').find('strong').get_text()
print(title_R72700)
print(price_R72700)

R73700X = 'https://www.kabum.com.br/produto/102436/processador-amd-ryzen-7-3700x-32mb-3-6ghz-4-4ghz-max-turbo-am4-sem-v-deo-100-100000071box'
page_R73700X = requests.get(R73700X, headers=headers)
soup_R73700X = BeautifulSoup(page_R73700X.content,'html.parser')

title_R73700X = soup_R73700X.find(itemprop='name').get_text()
price_R73700X = soup_R73700X.find('span', itemprop='offers').find('strong').get_text()
print(title_R73700X)
print(price_R73700X)

R73800X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102435'
page_R73800X = requests.get(R73800X, headers=headers)
soup_R73800X = BeautifulSoup(page_R73800X.content,'html.parser')

title_R73800X = soup_R73800X.find(itemprop='name').get_text()
price_R73800X = soup_R73800X.find('span', class_='preco_desconto_avista-cm').get_text()
print(title_R73800X)
print(price_R73800X)

R93900X = 'https://www.kabum.com.br/produto/102434/processador-amd-ryzen-9-3900x-cache-64mb-3-8ghz-4-6ghz-max-turbo-am4-sem-v-deo-100-100000023box'
page_R93900X = requests.get(R93900X, headers=headers)
soup_R93900X = BeautifulSoup(page_R93900X.content,'html.parser')
title_R93900X = soup_R93900X.find(itemprop='name').get_text()
price_R93900X = soup_R93900X.find('span', itemprop='offers').find('strong').get_text()
print(title_R93900X)
print(price_R93900X)

planilha = excel.active
planilha['A1'] = 'AMD:'
planilha['A2'] = 'CPU:'
planilha['B1'] = 'Nome:'
planilha['B2'] = 'R5 1600AF'
planilha['D1'] = 'Valor:'
planilha['C1'] = 'Data:'
planilha['C2'] = '{}'.format(date.today())
planilha['D2'] = '{}'.format(price_R51600AF)
planilha['A3'] = 'CPU:'
planilha['B3'] = 'R3 2200G'
planilha['D3'] = '{}'.format(price_R32200G)
planilha['C3'] = '{}'.format(date.today())
planilha['A4'] = 'CPU:'
planilha['B4'] = 'R5 2600'
planilha['D4'] = '{}'.format(price_R52600)
planilha['C4'] = '{}'.format(date.today())
planilha['A5'] = 'CPU:'
planilha['B5'] = 'R7 2700'
planilha['D5'] = '{}'.format(price_R72700)
planilha['C5'] = '{}'.format(date.today())
planilha['A6'] = 'CPU:'
planilha['B6'] = 'R5 3600'
planilha['D6'] = '{}'.format(price_R53600)
planilha['C6'] = '{}'.format(date.today())
planilha['A7'] = 'CPU:'
planilha['B7'] = 'R7 3700X'
planilha['D7'] = '{}'.format(price_R73700X)
planilha['C7'] = '{}'.format(date.today())
planilha['A8'] = 'CPU:'
planilha['B8'] = 'R7 3800X'
planilha['D8'] = '{}'.format(price_R73800X)
planilha['C8'] = '{}'.format(date.today())
planilha['A9'] = 'CPU:'
planilha['B9'] = 'R9 3900X'
planilha['D9'] = '{}'.format(price_R93900X)
planilha['C9'] = '{}'.format(date.today())
excel.save('{}.xlsx'.format(date.today()))



























