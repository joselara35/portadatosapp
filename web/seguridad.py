import requests

cabeceras = {'cache-control': 'no-cache', 'accept': 'text/html'} 
r = requests.get('http://unblog.xyz', headers=cabeceras)