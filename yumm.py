from urllib2 import urlopen
from json import load 
from codes import api_key, api_id

terms_list = ""
params =''

# sample functional query:
# 	http://api.yummly.com/v1/api/recipes?_app_id=___ ###SAMPLE ID___ &_app_key=___ SAMPLE KEY __ &q=strawberry+beer+

# search_url = http://api.yummly.com/v1/api/recipes?_app_id=api_id&_app_key=api_key"

search_input=raw_input('what ingredients do you want to search for -> ')

if ',' in search_input:
	terms_list = search_input.split(',')
else:
	terms_list = search_input.split()

print 'TERMS LIST IS:', terms_list

for item in terms_list:
	params = params+item+'+'

url =' http://api.yummly.com/v1/api/recipes?_app_id='
url += api_id+'&_app_key='+api_key
url +='&q='+params

print url


