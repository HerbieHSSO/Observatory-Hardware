import requests
from bs4 import BeautifulSoup
import smtplib
import openpyxl
from openpyxl import Workbook
from datetime import date


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

try:
    i39100F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=101918'
except:
    i39100F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101918'
page_i39100F = requests.get(i39100F, headers=headers)
soup_i39100F = BeautifulSoup(page_i39100F.content,'html.parser')

title_i39100F = soup_i39100F.find(itemprop='name').get_text()
price_i39100F = soup_i39100F.find(itemprop='price').get('content')
print(title_i39100F)
print(price_i39100F)

try:
    i59400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=99683'
except:
    i59400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=99683'
page_i59400F = requests.get(i59400F, headers=headers)
soup_i59400F = BeautifulSoup(page_i59400F.content,'html.parser')


title_i59400F = soup_i59400F.find(itemprop='name').get_text()
price_i59400F = soup_i59400F.find(itemprop='price').get('content')
print(title_i59400F)
print(price_i59400F)
try:
    
    i59600K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98765'
except:
    i59600K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98765'
    

page_i59600K = requests.get(i59600K, headers=headers)
soup_i59600K = BeautifulSoup(page_i59600K.content,'html.parser')


title_i59600K = soup_i59600K.find(itemprop='name').get_text()
price_i59600K = soup_i59600K.find(itemprop='price').get('content')
print(title_i59600K)
print(price_i59600K)

try:
    
    i59600KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102809'
except:
    i59600KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102809'


page_i59600KF = requests.get(i59600KF, headers=headers)
soup_i59600KF = BeautifulSoup(page_i59600KF.content,'html.parser')


title_i59600KF = soup_i59600KF.find(itemprop='name').get_text()
price_i59600KF = soup_i59600KF.find(itemprop='price').get('content')
print(title_i59600KF)
print(price_i59600KF)


try:
    i79700F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=104144'
except:
    i79700F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=104144'

page_i79700F = requests.get(i79700F, headers=headers)
soup_i79700F = BeautifulSoup(page_i79700F.content,'html.parser')


title_i79700F = soup_i79700F.find(itemprop='name').get_text()
price_i79700F = soup_i79700F.find(itemprop='price').get('content')
print(title_i79700F)
print(price_i79700F)

try:
    i79700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=98808'
except:
    i79700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98808'
    
page_i79700K = requests.get(i79700K, headers=headers)
soup_i79700K = BeautifulSoup(page_i79700K.content,'html.parser')

title_i79700K = soup_i79700K.find(itemprop='name').get_text()
price_i79700K = soup_i79700K.find(itemprop='price').get('content')
print(title_i79700K)
print(price_i79700K)
try:
    i79700KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=98808'
except:
    i79700KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98808'
page_i79700KF = requests.get(i79700KF, headers=headers)
soup_i79700KF = BeautifulSoup(page_i79700KF.content,'html.parser')

title_i79700KF = soup_i79700KF.find(itemprop='name').get_text()
price_i79700KF = soup_i79700KF.find(itemprop='price').get('content')
print(title_i79700KF)
print(price_i79700KF)
try:
    
    i99900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=98994'
except:
    i99900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98994'
page_i99900K = requests.get(i99900K, headers=headers)
soup_i99900K = BeautifulSoup(page_i99900K.content,'html.parser')

title_i99900K = soup_i99900K.find(itemprop='name').get_text()
price_i99900K = soup_i99900K.find(itemprop='price').get('content')
print(title_i99900K)
print(price_i99900K)

try:
    i99900KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102808'
except:
    i99900KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102808'

page_i99900KF = requests.get(i99900KF, headers=headers)
soup_i99900KF = BeautifulSoup(page_i99900KF.content,'html.parser')

title_i99900KF = soup_i99900KF.find(itemprop='name').get_text()
price_i99900KF = soup_i99900KF.find(itemprop='price').get('content')
print(title_i99900KF)
print(price_i99900KF)


try:
    i310100 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112989'
except:
    i310100 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112989'

page_i310100 = requests.get(i310100, headers=headers)
soup_i310100 = BeautifulSoup(page_i310100.content,'html.parser')

title_i310100 = soup_i310100.find(itemprop='name').get_text()
price_i310100 = soup_i310100.find(itemprop='price').get('content')
print(title_i310100)
print(price_i310100)


try:
    i510400 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112990'
except:
    i510400 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112990'



page_i510400 = requests.get(i510400, headers=headers)
soup_i510400 = BeautifulSoup(page_i510400.content,'html.parser')


title_i510400 = soup_i510400.find(itemprop='name').get_text()
price_i510400 = soup_i510400.find(itemprop='price').get('content')
print(title_i510400)
print(price_i510400)
try:
    i510400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112991'
except:
    i510400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112991'

page_i510400F = requests.get(i510400F, headers=headers)
soup_i510400F = BeautifulSoup(page_i510400F.content,'html.parser')


title_i510400F = soup_i510400F.find(itemprop='name').get_text()
price_i510400F = soup_i510400F.find(itemprop='price').get('content')
print(title_i510400F)
print(price_i510400F)


try:
    i710700 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112994'
except:
    i710700 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112994'

page_i710700 = requests.get(i710700, headers=headers)
soup_i710700 = BeautifulSoup(page_i710700.content,'html.parser')

title_i710700 = soup_i710700.find(itemprop='name').get_text()
price_i710700 = soup_i710700.find(itemprop='price').get('content')
print(title_i710700)
print(price_i710700)


try:
    i710700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112996'
except:
    i710700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112996'


page_i710700K = requests.get(i710700K, headers=headers)
soup_i710700K = BeautifulSoup(page_i710700K.content,'html.parser')

title_i710700K = soup_i710700K.find(itemprop='name').get_text()
price_i710700K = soup_i710700K.find(itemprop='price').get('content')
print(title_i710700K)
print(price_i710700K)



try:
    i910900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=113000'
except:
    i910900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=113000'
page_i910900K = requests.get(i910900K, headers=headers)
soup_i910900K = BeautifulSoup(page_i910900K.content,'html.parser')

title_i910900K = soup_i910900K.find(itemprop='name').get_text()
price_i910900K = soup_i910900K.find(itemprop='price').get('content')
print(title_i910900K)
print(price_i910900K)











































