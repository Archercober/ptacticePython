import urllib.request
import re
import time
import requests
# to get a mail address
urlm='http://www.yopmail.com/zh/email-generator.php'
urlr='http://www.n2ping.com/'
pattern=re.compile(r'value=\"(.+)&#64')

address=urllib.request.urlopen(urlm)
content=str(address.read(),'utf-8')
mail=re.findall(pattern,content)
email=mail[0]+'@yopmail.com'


#the simiulation of lincn register
url_post='http://www.51linkcn.com/auth/send-active-mail HTTP/1.1'

print (email)  