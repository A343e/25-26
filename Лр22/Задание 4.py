import requests
link = 'https://browser-info.ru/'
respoce= requests.get(link).text
print(respoce)