import requests
from requests import Session
from pprint import pprint as pp
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '5e8ae130-977b-41aa-aef0-dfac5ab682a2',
}
r = requests.get(url , headers=headers)
class api:
  def __init__(self,token):
    self.apiurl= 'https://pro-api.coinmarketcap.com'
    self.headers= {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '5e8ae130-977b-41aa-aef0-dfac5ab682a2',}
    self.session=Session()
    self.session.headers.update(self.headers)
  def allcoins(self):
    self.apiurl+'/v1/cryptocurrency/map'
    a =self.session.get(url)
    data = r.json()['data']
    return data
  def getPrice(self,symbol):
    url=self.apiurl+ '/v1/cryptocurrency/quotes/latest'
    param={'symbol':symbol}
    a =self.session.get(url,params=param)
    data = r.json()['data']
    return data
apikey=api('5e8ae130-977b-41aa-aef0-dfac5ab682a2')

pp(apikey.getPrice('BTC'))