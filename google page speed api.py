import requests

api_key = 'AIzaSyDt3mgW_tG3TYaamT4a783ZaEX5aDD-bqw'
test_api = input('Enter your title: ')
api = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={test_api}&key= {api_key}'
res = requests.get(api)
if res.status_code ==200:
    data = res.json()
    cls_score = data.get('loadingExperience').get('metrics').get('FIRST_INPUT_DELAY_MS').get('percentile')
    print(cls_score)

else:
    print('Something wrong')