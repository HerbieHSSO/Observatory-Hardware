import requests
from bs4 import BeautifulSoup
import smtplib
import openpyxl
from openpyxl import Workbook
from datetime import date
from win10toast import ToastNotifier


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
toaster = ToastNotifier()
#CPUs:

try:
    

    kabum_R51600AF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=107545'

except:
    kabum_R51600AF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=107545'
page_kabum_R51600AF = requests.get(kabum_R51600AF, headers=headers)
soup_kabum_R51600AF = BeautifulSoup(page_kabum_R51600AF.content,'html.parser')


title_kabum_R51600AF = soup_kabum_R51600AF.find(itemprop='name').get_text()
price_kabum_R51600AF = soup_kabum_R51600AF.find(itemprop='price').get('content')

print(title_kabum_R51600AF)
    
print(price_kabum_R51600AF)


try:
    try:
        status_kabum_R51600AF = soup_kabum_R51600AF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_R51600AF)
    except:
        status_kabum_R51600AF = soup_kabum_R51600AF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_R51600AF)


except:
    status_kabum_R51600AF = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - R5 1600AF')






try:
    kabum_R32200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=94723'

        
except:
    kabum_R32200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=94723'


page_kabum_R32200G = requests.get(kabum_R32200G, headers=headers)
soup_kabum_R32200G = BeautifulSoup(page_kabum_R32200G.content,'html.parser')

title_kabum_R32200G = soup_kabum_R32200G.find(itemprop='name').get_text()
price_kabum_R32200G = soup_kabum_R32200G.find(itemprop='price').get('content')
print(title_kabum_R32200G)
print_price_kabum_R32200G = print(price_kabum_R32200G)
try:
    try:
        status_kabum_R32200G = soup_kabum_R32200G.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_R32200G)
    except:
        status_kabum_R32200G = soup_kabum_R32200G.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_R32200G)


except:
    
    status_kabum_R32200G = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - R3 2200G')
    







try:
    
    kabum_R52600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=95557'
except:
    kabum_R52600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=95557'
page_kabum_R52600 = requests.get(kabum_R52600, headers=headers)
soup_kabum_R52600 = BeautifulSoup(page_kabum_R52600.content,'html.parser')

title_kabum_R52600 = soup_kabum_R52600.find(itemprop='name').get_text()
price_kabum_R52600 = soup_kabum_R52600.find(itemprop='price').get('content')
print(title_kabum_R52600)
print(price_kabum_R52600)
try:
    try:
        status_kabum_R52600 = soup_kabum_R52600.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_R52600)
    except:
        status_kabum_R52600 = soup_kabum_R52600.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_R52600)


except:

    status_kabum_R52600 = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - R5 2600', "TEST")








try:
    

    kabum_R53600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102438'
except:
    kabum_R53600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102438'
    
page_kabum_R53600 = requests.get(kabum_R53600, headers=headers)
soup_kabum_R53600 = BeautifulSoup(page_kabum_R53600.content,'html.parser')

title_kabum_R53600 = soup_kabum_R53600.find(itemprop='name').get_text()
price_kabum_R53600 = soup_kabum_R53600.find(itemprop='price').get('content')

print(title_kabum_R53600)
print(price_kabum_R53600)

try:
    try:
        status_kabum_R53600 = soup_kabum_R53600.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_R53600)
    except:
        status_kabum_R53600 = soup_kabum_R53600.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_R53600)


except:
    status_kabum_R53600 = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - R5 3600', "Kabum")












try:
    
    kabum_R72700 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=95564'
except:
    kabum_R72700 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=95564'
    
page_kabum_R72700 = requests.get(kabum_R72700, headers=headers)
soup_kabum_R72700 = BeautifulSoup(page_kabum_R72700.content,'html.parser')

title_kabum_R72700 = soup_kabum_R72700.find(itemprop='name').get_text()
price_kabum_R72700 = soup_kabum_R72700.find(itemprop='price').get('content')
print(title_kabum_R72700)
print(price_kabum_R72700)
try:
    try:
        status_kabum_R72700 = soup_kabum_R72700.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_R72700)
    except:
        status_kabum_R72700 = soup_kabum_R72700.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_R72700)


except:
    status_kabum_R72700 = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - R5 2700', "Kabum")









try:
    
    kabum_R73700X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102436'
except:
    kabum_R73700X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102436'
page_kabum_R73700X = requests.get(kabum_R73700X, headers=headers)
soup_kabum_R73700X = BeautifulSoup(page_kabum_R73700X.content,'html.parser')

title_kabum_R73700X = soup_kabum_R73700X.find(itemprop='name').get_text()
price_kabum_R73700X = soup_kabum_R73700X.find(itemprop='price').get('content')
print(title_kabum_R73700X)
print(price_kabum_R73700X)
try:
    try:
        status_kabum_R73700X = soup_kabum_R73700X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_R73700X)
    except:
        status_kabum_R73700X = soup_kabum_R73700X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_R73700X)


except:
    status_kabum_R73700X = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - R7 3700X', "Kabum")







try:
    
    kabum_R73800X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102435'
except:
    kabum_R73800X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102435'
page_kabum_R73800X = requests.get(kabum_R73800X, headers=headers)
soup_kabum_R73800X = BeautifulSoup(page_kabum_R73800X.content,'html.parser')

title_kabum_R73800X = soup_kabum_R73800X.find(itemprop='name').get_text()
price_kabum_R73800X = soup_kabum_R73800X.find(itemprop='price').get('content')
print(title_kabum_R73800X)
print(price_kabum_R73800X)

try:
    try:
        status_kabum_R73800X = soup_kabum_R73800X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_R73800X)
    except:
        status_kabum_R73800X = soup_kabum_R73800X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_R73800X)


except:
    status_kabum_R73800X = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - R7 3800X', "Kabum")











try:
    kabum_R93900X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102434'
except:
    kabum_R93900X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102434'
page_kabum_R93900X = requests.get(kabum_R93900X, headers=headers)
soup_kabum_R93900X = BeautifulSoup(page_kabum_R93900X.content,'html.parser')
title_kabum_R93900X = soup_kabum_R93900X.find(itemprop='name').get_text()
price_kabum_R93900X = soup_kabum_R93900X.find(itemprop='price').get('content')
print(title_kabum_R93900X)
print(price_kabum_R93900X)

try:
    try:
        status_kabum_R93900X = soup_kabum_R93900X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_R93900X)
    except:
        status_kabum_R93900X = soup_kabum_R93900X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_R93900X)
except:
    status_kabum_R93900X = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - R9 3900X', "Kabum")





try:
    kabum_R33300X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=113391'
except:
    kabum_R33300X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=113391'

page_kabum_R33300X = requests.get(kabum_R33300X, headers=headers)
soup_kabum_R33300X = BeautifulSoup(page_kabum_R33300X.content,'html.parser')
title_kabum_R33300X = soup_kabum_R33300X.find(itemprop='name').get_text()
price_kabum_R33300X = soup_kabum_R33300X.find(itemprop='price').get('content')
print(title_kabum_R33300X)
print(price_kabum_R33300X)

try:
    try:
        status_kabum_R33300X = soup_kabum_R33300X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_R33300X)
    except:
        status_kabum_R33300X = soup_kabum_R33300X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_R33300X)

except:
    status_kabum_R33300X = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - R3 3300X', "Kabum")
        

try:
    kabum_R33200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102248'
except:
    kabum_R33200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102248'


page_kabum_R33200G = requests.get(kabum_R33200G, headers=headers)
soup_kabum_R33200G = BeautifulSoup(page_kabum_R33200G.content,'html.parser')
title_kabum_R33200G = soup_kabum_R33200G.find(itemprop='name').get_text()
price_kabum_R33200G = soup_kabum_R33200G.find(itemprop='price').get('content')
print(title_kabum_R33200G)
print(price_kabum_R33200G)

try:
    try:
        status_kabum_R33200G = soup_kabum_R33200G.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_R33200G)
    except:
        status_kabum_R33200G = soup_kabum_R33200G.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_R33200G)

except:
    status_kabum_R33200G = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - R3 3200G', "Kabum")




try:
    kabum_R53600X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102437'
except:
    kabum_R53600X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102437'



page_kabum_R53600X = requests.get(kabum_R53600X, headers=headers)
soup_kabum_R53600X = BeautifulSoup(page_kabum_R53600X.content,'html.parser')

title_kabum_R53600X = soup_kabum_R53600X.find(itemprop='name').get_text()
price_kabum_R53600X = soup_kabum_R53600X.find(itemprop='price').get('content')

print(title_kabum_R53600X)
print(price_kabum_R53600X)
try:
    try:
        status_kabum_R53600X = soup_kabum_R53600X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_R53600X)
    except:
        status_kabum_R53600X = soup_kabum_R53600X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_R53600X)
except:
    status_kabum_R53600X = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - R5 3600X', "Kabum")

#GPUs:

try:
    kabum_Rx5704gb_PhantomGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102833'
except:
    kabum_Rx5704gb_PhantomGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102833'


page_kabum_Rx5704gb_PhantomGaming = requests.get(kabum_Rx5704gb_PhantomGaming,  headers=headers)
soup_kabum_Rx5704gb_PhantomGaming = BeautifulSoup(page_kabum_Rx5704gb_PhantomGaming.content,'html.parser')

title_kabum_Rx5704gb_PhantomGaming = soup_kabum_Rx5704gb_PhantomGaming.find(itemprop='name').get_text()
price_kabum_Rx5704gb_PhantomGaming = soup_kabum_Rx5704gb_PhantomGaming.find(itemprop='price').get('content')

print(title_kabum_Rx5704gb_PhantomGaming)
print(price_kabum_Rx5704gb_PhantomGaming)
try:
    try:
        status_kabum_Rx5704gb_PhantomGaming = soup_kabum_Rx5704gb_PhantomGaming.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_Rx5704gb_PhantomGaming)
    except:
        status_kabum_Rx5704gb_PhantomGaming = soup_kabum_Rx5704gb_PhantomGaming.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_Rx5704gb_PhantomGaming)

except:
    status_kabum_Rx5704gb_PhantomGaming = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - Rx5708gb Phantom Gaming', "Kabum")

try:
    kabum_Rx5708gb_PhantomGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102832'
except:
    kabum_Rx5708gb_PhantomGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102832'

 
page_kabum_Rx5708gb_PhantomGaming = requests.get(kabum_Rx5708gb_PhantomGaming, headers=headers)
soup_kabum_Rx5708gb_PhantomGaming = BeautifulSoup(page_kabum_Rx5708gb_PhantomGaming.content,'html.parser')

title_kabum_Rx5708gb_PhantomGaming = soup_kabum_Rx5708gb_PhantomGaming.find(itemprop='name').get_text()
price_kabum_Rx5708gb_PhantomGaming = soup_kabum_Rx5708gb_PhantomGaming.find(itemprop='price').get('content')

print(title_kabum_Rx5708gb_PhantomGaming)
print(price_kabum_Rx5708gb_PhantomGaming)


try:
    try:
        status_kabum_Rx5708gb_PhantomGaming = soup_kabum_Rx5708gb_PhantomGaming.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_Rx5708gb_PhantomGaming)
    except:
        status_kabum_Rx5708gb_PhantomGaming = soup_kabum_Rx5708gb_PhantomGaming.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_Rx5708gb_PhantomGaming)
except:
    status_kabum_Rx5708gb_PhantomGaming = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - Rx5708gb Phantom Gaming', "Kabum")
 







try:
    kabum_Rx5704gb_Gaming4G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=88748'

except:
    kabum_Rx5704gb_Gaming4G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=88748'

page_kabum_Rx5704gb_Gaming4G = requests.get(kabum_Rx5704gb_Gaming4G, headers=headers)
soup_kabum_Rx5704gb_Gaming4G = BeautifulSoup(page_kabum_Rx5704gb_Gaming4G.content,'html.parser')

title_kabum_Rx5704gb_Gaming4G = soup_kabum_Rx5704gb_Gaming4G.find(itemprop='name').get_text()
price_kabum_Rx5704gb_Gaming4G = soup_kabum_Rx5704gb_Gaming4G.find(itemprop='price').get('content')



print(title_kabum_Rx5704gb_Gaming4G)
print(price_kabum_Rx5704gb_Gaming4G)



try:
    try:
        status_kabum_Rx5704gb_Gaming4G = soup_kabum_Rx5704gb_Gaming4G.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_Rx5704gb_Gaming4G)
    except:
        status_kabum_Rx5704gb_Gaming4G = soup_kabum_Rx5704gb_Gaming4G.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_Rx5704gb_Gaming4G)
except:
    status_kabum_Rx5704gb_Gaming4G = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - Rx5704gb Gaming4G', 'Kabum')
    





try:
    kabum_Rx5708gb_Gaming8G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102040'

except:
    kabum_Rx5708gb_Gaming8G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102040'
    




page_kabum_Rx5708gb_Gaming8G = requests.get(kabum_Rx5708gb_Gaming8G, headers=headers)
soup_kabum_Rx5708gb_Gaming8G = BeautifulSoup(page_kabum_Rx5708gb_Gaming8G.content,'html.parser')

title_kabum_Rx5708gb_Gaming8G = soup_kabum_Rx5708gb_Gaming8G.find(itemprop='name').get_text()
price_kabum_Rx5708gb_Gaming8G = soup_kabum_Rx5708gb_Gaming8G.find(itemprop='price').get('content')



print(title_kabum_Rx5708gb_Gaming8G)
print(price_kabum_Rx5708gb_Gaming8G)

try:
    try:
        status_kabum_Rx5708gb_Gaming8G = soup_kabum_Rx5708gb_Gaming8G.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_Rx5708gb_Gaming8G)
    except:
        status_kabum_Rx5708gb_Gaming8G = soup_kabum_Rx5708gb_Gaming8G.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_Rx5708gb_Gaming8G)
except:
    status_kabum_Rx5708gb_Gaming8G = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - Rx 5708gb Gaming8G', 'Kabum')
    


try:
    kabum_Rx5704gb_XFXRSXXX = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=93572'
except:
    kabum_Rx5704gb_XFXRSXXX = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=93572'

page_kabum_Rx5704gb_XFXRSXXX = requests.get(kabum_Rx5704gb_XFXRSXXX, headers=headers)
soup_kabum_Rx5704gb_XFXRSXXX = BeautifulSoup(page_kabum_Rx5704gb_XFXRSXXX.content,'html.parser')

title_kabum_Rx5704gb_XFXRSXXX = soup_kabum_Rx5704gb_XFXRSXXX.find(itemprop='name').get_text()
price_kabum_Rx5704gb_XFXRSXXX = soup_kabum_Rx5704gb_XFXRSXXX.find(itemprop='price').get('content')



print(title_kabum_Rx5704gb_XFXRSXXX)
print(price_kabum_Rx5704gb_XFXRSXXX)

try:
    try:
        status_kabum_Rx5704gb_XFXRSXXX = soup_kabum_Rx5704gb_XFXRSXXX.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_Rx5704gb_XFXRSXXX)
    except:
        status_kabum_Rx5704gb_XFXRSXXX = soup_kabum_Rx5704gb_XFXRSXXX.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_Rx5704gb_XFXRSXXX)
except:
    status_kabum_Rx5704gb_XFXRSXXX = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - Rx 5708gb XFX', 'Kabum')



try:
    kabum_Rx590_Gaming8G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=104002'


except:
    kabum_Rx590_Gaming8G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=104002'


page_kabum_Rx590_Gaming8G = requests.get(kabum_Rx590_Gaming8G, headers=headers)
soup_kabum_Rx590_Gaming8G = BeautifulSoup(page_kabum_Rx590_Gaming8G.content,'html.parser')

title_kabum_Rx590_Gaming8G = soup_kabum_Rx590_Gaming8G.find(itemprop='name').get_text()
price_kabum_Rx590_Gaming8G = soup_kabum_Rx590_Gaming8G.find(itemprop='price').get('content')



print(title_kabum_Rx590_Gaming8G)
print(price_kabum_Rx590_Gaming8G)

try:
    try:
        status_kabum_Rx590_Gaming8G = soup_kabum_Rx590_Gaming8G.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_Rx590_Gaming8G)
    except:
        status_kabum_Rx590_Gaming8G = soup_kabum_Rx590_Gaming8G.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_Rx590_Gaming8G)
except:
    status_kabum_Rx590_Gaming8G = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - Rx5908gb Gaming8G', 'Kabum')
    




try:
    kabum_Rx5500XT4gb_GamingOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=109644'

except:
    kabum_Rx5500XT4gb_GamingOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=109644'


page_kabum_Rx5500XT4gb_GamingOC = requests.get(kabum_Rx5500XT4gb_GamingOC, headers=headers)
soup_kabum_Rx5500XT4gb_GamingOC = BeautifulSoup(page_kabum_Rx5500XT4gb_GamingOC.content,'html.parser')

title_kabum_Rx5500XT_GamingOC = soup_kabum_Rx5500XT4gb_GamingOC.find(itemprop='name').get_text()
price_kabum_Rx5500XT4gb_GamingOC = soup_kabum_Rx5500XT4gb_GamingOC.find(itemprop='price').get('content')
print(title_kabum_Rx5500XT_GamingOC)
print(price_kabum_Rx5500XT4gb_GamingOC)

try:
    try:
        status_kabum_Rx5500XT4gb_GamingOC = soup_kabum_Rx5500XT4gb_GamingOC.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_Rx5500XT4gb_GamingOC)
    except:
        status_kabum_Rx5500XT4gb_GamingOC = soup_kabum_Rx5500XT4gb_GamingOC.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_Rx5500XT4gb_GamingOC)
except:
    status_kabum_Rx5500XT4gb_GamingOC = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - Rx5500XT4gb GamingOC', 'Kabum')
    









try:
    kabum_Rx5500XT8gb_Pulse = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=109852'

except:
    kabum_Rx5500XT8gb_Pulse = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=109852'


page_kabum_Rx5500XT8gb_Pulse = requests.get(kabum_Rx5500XT8gb_Pulse, headers=headers)
soup_kabum_Rx5500XT8gb_Pulse = BeautifulSoup(page_kabum_Rx5500XT8gb_Pulse.content,'html.parser')

title_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT8gb_Pulse.find(itemprop='name').get_text()
price_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT8gb_Pulse.find(itemprop='price').get('content')

print(title_kabum_Rx5500XT8gb_Pulse)
print(price_kabum_Rx5500XT8gb_Pulse)



try:
    try:
        status_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT8gb_Pulse.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_Rx5500XT8gb_Pulse)
    except:
        status_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT8gb_Pulse.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_Rx5500XT8gb_Pulse)
except:
    status_kabum_Rx5500XT8gb_Pulse = print('PROMOÇÃO')
    toaster.show_toast('PROMOÇÃO - Rx5500XT8gb Pulse', 'Kabum')







try:
    kabum_Rx5500XT8gb_Pulse = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=109852'

except:
    kabum_Rx5500XT8gb_Pulse = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=109852'


page_kabum_Rx5500XT8gb_Pulse = requests.get(kabum_Rx5500XT8gb_Pulse, headers=headers)
soup_kabum_Rx5500XT8gb_Pulse = BeautifulSoup(page_kabum_Rx5500XT8gb_Pulse.content,'html.parser')

title_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT8gb_Pulse.find(itemprop='name').get_text()
price_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT8gb_Pulse.find(itemprop='price').get('content')

print(title_kabum_Rx5500XT8gb_Pulse)
print(price_kabum_Rx5500XT8gb_Pulse)



try:
    try:
        status_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT8gb_Pulse.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
        print(status_kabum_Rx5500XT8gb_Pulse)
    except:
        status_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT8gb_Pulse.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")
        print(status_kabum_Rx5500XT8gb_Pulse)
except:
    status_kabum_Rx5500XT8gb_Pulse = 'PROMOÇÃO'
    toaster.show_toast('PROMOÇÃO - Rx5500XT8gb Pulse', 'Kabum')




































    
