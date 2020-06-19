import requests
from bs4 import BeautifulSoup
import smtplib
import openpyxl
from openpyxl import Workbook
from datetime import date

#CPUs:
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

try:
    kabum_i39100F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=101918'
except:
    kabum_i39100F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101918'
page_kabum_i39100F = requests.get(kabum_i39100F, headers=headers)
soup_kabum_i39100F = BeautifulSoup(page_kabum_i39100F.content,'html.parser')

title_kabum_i39100F = soup_kabum_i39100F.find(itemprop='name').get_text()
price_kabum_i39100F = soup_kabum_i39100F.find(itemprop='price').get('content')
print(title_kabum_i39100F)
print(price_kabum_i39100F)

try:
    kabum_i59400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=99683'
except:
    kabum_i59400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=99683'
page_kabum_i59400F = requests.get(kabum_i59400F, headers=headers)
soup_kabum_i59400F = BeautifulSoup(page_kabum_i59400F.content,'html.parser')


title_kabum_i59400F = soup_kabum_i59400F.find(itemprop='name').get_text()
price_kabum_i59400F = soup_kabum_i59400F.find(itemprop='price').get('content')
print(title_kabum_i59400F)
print(price_kabum_i59400F)
try:
    
    kabum_i59600K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98765'
except:
    kabum_i59600K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98765'
    

page_kabum_i59600K = requests.get(kabum_i59600K, headers=headers)
soup_kabum_i59600K = BeautifulSoup(page_kabum_i59600K.content,'html.parser')


title_kabum_i59600K = soup_kabum_i59600K.find(itemprop='name').get_text()
price_kabum_i59600K = soup_kabum_i59600K.find(itemprop='price').get('content')
print(title_kabum_i59600K)
print(price_kabum_i59600K)

try:
    
    kabum_i59600KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102809'
except:
    kabum_i59600KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102809'


page_kabum_i59600KF = requests.get(kabum_i59600KF, headers=headers)
soup_kabum_i59600KF = BeautifulSoup(page_kabum_i59600KF.content,'html.parser')


title_kabum_i59600KF = soup_kabum_i59600KF.find(itemprop='name').get_text()
price_kabum_i59600KF = soup_kabum_i59600KF.find(itemprop='price').get('content')
print(title_kabum_i59600KF)
print(price_kabum_i59600KF)


try:
    kabum_i79700F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=104144'
except:
    kabum_i79700F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=104144'

page_kabum_i79700F = requests.get(kabum_i79700F, headers=headers)
soup_kabum_i79700F = BeautifulSoup(page_kabum_i79700F.content,'html.parser')


title_kabum_i79700F = soup_kabum_i79700F.find(itemprop='name').get_text()
price_kabum_i79700F = soup_kabum_i79700F.find(itemprop='price').get('content')
print(title_kabum_i79700F)
print(price_kabum_i79700F)

try:
    kabum_i79700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=98808'
except:
    kabum_i79700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98808'
    
page_kabum_i79700K = requests.get(kabum_i79700K, headers=headers)
soup_kabum_i79700K = BeautifulSoup(page_kabum_i79700K.content,'html.parser')

title_kabum_i79700K = soup_kabum_i79700K.find(itemprop='name').get_text()
price_kabum_i79700K = soup_kabum_i79700K.find(itemprop='price').get('content')
print(title_kabum_i79700K)
print(price_kabum_i79700K)
try:
    kabum_i79700KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=98808'
except:
    kabum_i79700KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98808'
page_kabum_i79700KF = requests.get(kabum_i79700KF, headers=headers)
soup_kabum_i79700KF = BeautifulSoup(page_kabum_i79700KF.content,'html.parser')

title_kabum_i79700KF = soup_kabum_i79700KF.find(itemprop='name').get_text()
price_kabum_i79700KF = soup_kabum_i79700KF.find(itemprop='price').get('content')
print(title_kabum_i79700KF)
print(price_kabum_i79700KF)
try:
    
    kabum_i99900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=98994'
except:
    kabum_i99900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98994'
page_kabum_i99900K = requests.get(kabum_i99900K, headers=headers)
soup_kabum_i99900K = BeautifulSoup(page_kabum_i99900K.content,'html.parser')

title_kabum_i99900K = soup_kabum_i99900K.find(itemprop='name').get_text()
price_kabum_i99900K = soup_kabum_i99900K.find(itemprop='price').get('content')
print(title_kabum_i99900K)
print(price_kabum_i99900K)

try:
    kabum_i99900KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102808'
except:
    kabum_i99900KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102808'

page_kabum_i99900KF = requests.get(kabum_i99900KF, headers=headers)
soup_kabum_i99900KF = BeautifulSoup(page_kabum_i99900KF.content,'html.parser')

title_kabum_i99900KF = soup_kabum_i99900KF.find(itemprop='name').get_text()
price_kabum_i99900KF = soup_kabum_i99900KF.find(itemprop='price').get('content')
print(title_kabum_i99900KF)
print(price_kabum_i99900KF)


try:
    kabum_i310100 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112989'
except:
    kabum_i310100 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112989'

page_kabum_i310100 = requests.get(kabum_i310100, headers=headers)
soup_kabum_i310100 = BeautifulSoup(page_kabum_i310100.content,'html.parser')

title_kabum_i310100 = soup_kabum_i310100.find(itemprop='name').get_text()
price_kabum_i310100 = soup_kabum_i310100.find(itemprop='price').get('content')
print(title_kabum_i310100)
print(price_kabum_i310100)


try:
    kabum_i510400 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112990'
except:
    kabum_i510400 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112990'



page_kabum_i510400 = requests.get(kabum_i510400, headers=headers)
soup_kabum_i510400 = BeautifulSoup(page_kabum_i510400.content,'html.parser')


title_kabum_i510400 = soup_kabum_i510400.find(itemprop='name').get_text()
price_kabum_i510400 = soup_kabum_i510400.find(itemprop='price').get('content')
print(title_kabum_i510400)
print(price_kabum_i510400)
try:
    kabum_i510400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112991'
except:
    kabum_i510400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112991'

page_kabum_i510400F = requests.get(kabum_i510400F, headers=headers)
soup_kabum_i510400F = BeautifulSoup(page_kabum_i510400F.content,'html.parser')


title_kabum_i510400F = soup_kabum_i510400F.find(itemprop='name').get_text()
price_kabum_i510400F = soup_kabum_i510400F.find(itemprop='price').get('content')
print(title_kabum_i510400F)
print(price_kabum_i510400F)


try:
    kabum_i710700 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112994'
except:
    kabum_i710700 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112994'

page_kabum_i710700 = requests.get(kabum_i710700, headers=headers)
soup_kabum_i710700 = BeautifulSoup(page_kabum_i710700.content,'html.parser')

title_kabum_i710700 = soup_kabum_i710700.find(itemprop='name').get_text()
price_kabum_i710700 = soup_kabum_i710700.find(itemprop='price').get('content')
print(title_kabum_i710700)
print(price_kabum_i710700)


try:
    kabum_i710700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112996'
except:
    kabum_i710700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112996'


page_kabum_i710700K = requests.get(kabum_i710700K, headers=headers)
soup_kabum_i710700K = BeautifulSoup(page_kabum_i710700K.content,'html.parser')

title_kabum_i710700K = soup_kabum_i710700K.find(itemprop='name').get_text()
price_kabum_i710700K = soup_kabum_i710700K.find(itemprop='price').get('content')
print(title_kabum_i710700K)
print(price_kabum_i710700K)



try:
    kabum_i910900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=113000'
except:
    kabum_i910900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=113000'
page_kabum_i910900K = requests.get(kabum_i910900K, headers=headers)
soup_kabum_i910900K = BeautifulSoup(page_kabum_i910900K.content,'html.parser')

title_kabum_i910900K = soup_kabum_i910900K.find(itemprop='name').get_text()
price_kabum_i910900K = soup_kabum_i910900K.find(itemprop='price').get('content')
print(title_kabum_i910900K)
print(price_kabum_i910900K)











































