import requests
import json
import pickle


url = 'http://localhost:5000'


data = pickle.load(open('data.pkl', 'rb'))

response = requests.post(url + '/results',json = data)
res = response.json()
print('Engine rating : {}'.format(res['output']))
print('\n\n Data : {}'.format(res['data']))
print()
print(res['values'])

