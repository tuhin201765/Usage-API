import requests
r = requests.get('https://api.ipify.org?format=json')
if r.status_code == 200:
    data = r.json()
    ip = data.get('ip')
loc_url = f'https://ipapi.co/{ip}/json/'
res = requests.get(loc_url)
if res.status_code >= 200:
    ip_details = res.json()
    print(ip_details)
    region = ip_details.get('region')
    country = ip_details.get('country_name')
    postal = ip_details.get('postal')
    wifi = ip_details.get('org')
    sentence = f"Ip {(ip)} holder live in {region},{country}.Here postal code is {postal} and currently using {wifi}."
    print(sentence)





