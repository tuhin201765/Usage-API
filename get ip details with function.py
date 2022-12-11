import requests
def res_data(url):
    res = requests.get(url) #(--------access 7 & 10 line.)
    if res.status_code >= 200:
        data= res.json()
        return data
api_url = res_data('https://api.ipify.org?format=json')
ip = api_url.get('ip')

location_url = res_data(f'https://ipapi.co/{ip}/json/')
region = location_url.get('region')
country = location_url.get('country_name')
postal = location_url.get('postal')
wifi = location_url.get('org')
sentence = f"Ip {[ip]} holder live in {region},{country}.Here postal code is {postal} and currently using {wifi}."
print(sentence)