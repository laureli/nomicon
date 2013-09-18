from urllib2 import urlopen
from json import load 
from codes import api_key, api_id

# API endpoint is:  http://api.yummly.com/v1

# sample functional query:
# 	http://api.yummly.com/v1/api/recipes?_app_id=32f5db9e&_app_key=9e8925d2e0663780addbb173657dda52&q=strawberry+beer+

# search_url = http://api.yummly.com/v1/api/recipes?_app_id=api_id&_app_key=api_key"

search_terms=raw_input('what ingredients do you want to search for -> ')
# remove non-alpha characters -->
# split words apart
# add + to the end of the word
# concatenate into a string and save it as parameters

parameters = "" # will actually be the output of search terms

url = 'http://api.yummly.com/v1/api/recipe/recipe-id?_app_id='
url += api_id+'&_app_key='+api_key
url +='&q='+parameters

print api_key

print url

print search_terms