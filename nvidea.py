import requests
from bs4 import BeautifulSoup
import smtplib
import openpyxl
from openpyxl import Workbook
from datetime import date


#GPUs:
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
try:
    kabum_GTX1650Super_XCBlackGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=113183'
except:
    kabum_GTX1650Super_XCBlackGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=113183'

page_kabum_GTX1650Super_XCBlackGaming = requests.get(kabum_GTX1650Super_XCBlackGaming, headers=headers)
soup_kabum_GTX1650Super_XCBlackGaming = BeautifulSoup(page_kabum_GTX1650Super_XCBlackGaming.content,'html.parser')


title_kabum_GTX1650Super_XCBlackGaming = soup_kabum_GTX1650Super_XCBlackGaming.find(itemprop='name').get_text()
price_kabum_GTX1650Super_XCBlackGaming = soup_kabum_GTX1650Super_XCBlackGaming.find(itemprop='price').get('content')
print(title_kabum_GTX1650Super_XCBlackGaming)
print(price_kabum_GTX1650Super_XCBlackGaming)


try:
    kabum_GTX1660_GigabyteOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=101039'
except:
    kabum_GTX1660_GigabyteOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101039'


page_kabum_GTX1660_GigabyteOC = requests.get(kabum_GTX1660_GigabyteOC, headers=headers)
soup_kabum_GTX1660_GigabyteOC = BeautifulSoup(page_kabum_GTX1660_GigabyteOC.content,'html.parser')


title_kabum_GTX1660_GigabyteOC = soup_kabum_GTX1660_GigabyteOC.find(itemprop='name').get_text()
price_kabum_GTX1660_GigabyteOC = soup_kabum_GTX1660_GigabyteOC.find(itemprop='price').get('content')
print(title_kabum_GTX1660_GigabyteOC)
print(price_kabum_GTX1660_GigabyteOC)



try:
    kabum_GTX1660Super_GigabyteOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=105132'
except:
    kabum_GTX1660Super_GigabyteOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=105132'


page_kabum_GTX1660Super_GigabyteOC = requests.get(kabum_GTX1660Super_GigabyteOC, headers=headers)
soup_kabum_GTX1660Super_GigabyteOC = BeautifulSoup(page_kabum_GTX1660Super_GigabyteOC.content,'html.parser')


title_kabum_GTX1660Super_GigabyteOC = soup_kabum_GTX1660Super_GigabyteOC.find(itemprop='name').get_text()
price_kabum_GTX1660Super_GigabyteOC = soup_kabum_GTX1660Super_GigabyteOC.find(itemprop='price').get('content')
print(title_kabum_GTX1660Super_GigabyteOC)
print(price_kabum_GTX1660Super_GigabyteOC)


try:
    kabum_GTX1660Ti_GamingX = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=100855'
except:
    kabum_GTX1660Ti_GamingX = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=100855'


page_kabum_GTX1660Ti_GamingX = requests.get(kabum_GTX1660Ti_GamingX, headers=headers)
soup_kabum_GTX1660Ti_GamingX = BeautifulSoup(page_kabum_GTX1660Ti_GamingX.content,'html.parser')


title_kabum_GTX1660Ti_GamingX = soup_kabum_GTX1660Ti_GamingX.find(itemprop='name').get_text()
price_kabum_GTX1660Ti_GamingX = soup_kabum_GTX1660Ti_GamingX.find(itemprop='price').get('content')
print(title_kabum_GTX1660Ti_GamingX)
print(price_kabum_GTX1660Ti_GamingX)


try:
    kabum_RTX2060_Gaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=110397'
except:
    kabum_RTX2060_Gaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=110397'


page_kabum_RTX2060_Gaming = requests.get(kabum_RTX2060_Gaming, headers=headers)
soup_kabum_RTX2060_Gaming = BeautifulSoup(page_kabum_RTX2060_Gaming.content,'html.parser')


title_kabum_RTX2060_Gaming = soup_kabum_RTX2060_Gaming.find(itemprop='name').get_text()
price_kabum_RTX2060_Gaming = soup_kabum_RTX2060_Gaming.find(itemprop='price').get('content')
print(title_kabum_RTX2060_Gaming)
print(price_kabum_RTX2060_Gaming)


try:
    kabum_RTX2060_GamingOCPro = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=100371'
except:
    kabum_RTX2060_GamingOCPro = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=100371'


page_kabum_RTX2060_GamingOCPro = requests.get(kabum_RTX2060_GamingOCPro, headers=headers)
soup_kabum_RTX2060_GamingOCPro = BeautifulSoup(page_kabum_RTX2060_GamingOCPro.content,'html.parser')


title_kabum_RTX2060_GamingOCPro = soup_kabum_RTX2060_GamingOCPro.find(itemprop='name').get_text()
price_kabum_RTX2060_GamingOCPro= soup_kabum_RTX2060_GamingOCPro.find(itemprop='price').get('content')
print(title_kabum_RTX2060_GamingOCPro)
print(price_kabum_RTX2060_GamingOCPro)




try:
    kabum_RTX2060Super_ROGStrix = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=100371'
except:
    kabum_RTX2060Super_ROGStrix = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=100371'


page_kabum_RTX2060Super_ROGStrix = requests.get(kabum_RTX2060Super_ROGStrix, headers=headers)
soup_kabum_RTX2060Super_ROGStrix = BeautifulSoup(page_kabum_RTX2060Super_ROGStrix.content,'html.parser')


title_kabum_RTX2060Super_ROGStrix = soup_kabum_RTX2060Super_ROGStrix.find(itemprop='name').get_text()
price_kabum_RTX2060Super_ROGStrix = soup_kabum_RTX2060Super_ROGStrix.find(itemprop='price').get('content')
print(title_kabum_RTX2060Super_ROGStrix)
print(price_kabum_RTX2060Super_ROGStrix)












