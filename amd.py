import requests
from bs4 import BeautifulSoup
import smtplib
import openpyxl
from openpyxl import Workbook
from datetime import date


try:
    

    R51600AF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=107545'

except:
    R51600AF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=107545'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}




page_R51600AF = requests.get(R51600AF, headers=headers)
soup_R51600AF = BeautifulSoup(page_R51600AF.content,'html.parser')


title_R51600AF = soup_R51600AF.find(itemprop='name').get_text()
price_R51600AF = soup_R51600AF.find(itemprop='price').get('content')
print(title_R51600AF)
print(price_R51600AF)



try:
    
    R32200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=94723'
except:
    R32200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=94723'

page_R32200G = requests.get(R32200G, headers=headers)
soup_R32200G = BeautifulSoup(page_R32200G.content,'html.parser')

title_R32200G = soup_R32200G.find(itemprop='name').get_text()
price_R32200G = soup_R32200G.find(itemprop='price').get('content')
print(title_R32200G)
print(price_R32200G)



try:
    
    R52600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=95557'
except:
    R52600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=95557'
page_R52600 = requests.get(R52600, headers=headers)
soup_R52600 = BeautifulSoup(page_R52600.content,'html.parser')

title_R52600 = soup_R52600.find(itemprop='name').get_text()
price_R52600 = soup_R52600.find(itemprop='price').get('content')
print(title_R52600)
print(price_R52600)

try:
    

    R53600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102438'
except:
    R53600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102438'
    
page_R53600 = requests.get(R53600, headers=headers)
soup_R53600 = BeautifulSoup(page_R53600.content,'html.parser')

title_R53600 = soup_R53600.find(itemprop='name').get_text()
price_R53600 = soup_R53600.find(itemprop='price').get('content')

print(title_R53600)
print(price_R53600)



try:
    
    R72700 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=95564'
except:
    R72700 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=95564'
    
page_R72700 = requests.get(R72700, headers=headers)
soup_R72700 = BeautifulSoup(page_R72700.content,'html.parser')

title_R72700 = soup_R72700.find(itemprop='name').get_text()
price_R72700 = soup_R72700.find(itemprop='price').get('content')
print(title_R72700)
print(price_R72700)

try:
    
    R73700X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102436'
except:
    R73700X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102436'
page_R73700X = requests.get(R73700X, headers=headers)
soup_R73700X = BeautifulSoup(page_R73700X.content,'html.parser')

title_R73700X = soup_R73700X.find(itemprop='name').get_text()
price_R73700X = soup_R73700X.find(itemprop='price').get('content')
print(title_R73700X)
print(price_R73700X)
try:
    
    R73800X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102435'
except:
    R73800X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102435'
page_R73800X = requests.get(R73800X, headers=headers)
soup_R73800X = BeautifulSoup(page_R73800X.content,'html.parser')

title_R73800X = soup_R73800X.find(itemprop='name').get_text()
price_R73800X = soup_R73800X.find(itemprop='price').get('content')
print(title_R73800X)
print(price_R73800X)
try:
    R93900X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102434'
except:
    R93900X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102434'
page_R93900X = requests.get(R93900X, headers=headers)
soup_R93900X = BeautifulSoup(page_R93900X.content,'html.parser')
title_R93900X = soup_R93900X.find(itemprop='name').get_text()
price_R93900X = soup_R93900X.find(itemprop='price').get('content')
print(title_R93900X)
print(price_R93900X)


try:
    R33300X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=113391'
except:
    R33300X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=113391'

page_R33300X = requests.get(R33300X, headers=headers)
soup_R33300X = BeautifulSoup(page_R33300X.content,'html.parser')
title_R33300X = soup_R33300X.find(itemprop='name').get_text()
price_R33300X = soup_R33300X.find(itemprop='price').get('content')
print(title_R33300X)
print(price_R33300X)

try:
    R33200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102248'
except:
    R33200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102248'


page_R33200G = requests.get(R33200G, headers=headers)
soup_R33200G = BeautifulSoup(page_R33200G.content,'html.parser')
title_R33200G = soup_R33200G.find(itemprop='name').get_text()
price_R33200G = soup_R33200G.find(itemprop='price').get('content')
print(title_R33200G)
print(price_R33200G)



try:
    R53600X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102437'
except:
    R53600X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102437'



page_R53600X = requests.get(R53600X, headers=headers)
soup_R53600X = BeautifulSoup(page_R53600X.content,'html.parser')

title_R53600X = soup_R53600X.find(itemprop='name').get_text()
price_R53600X = soup_R53600X.find(itemprop='price').get('content')

print(title_R53600X)
print(price_R53600X)















    
