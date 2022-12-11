import requests
# r = requests.get('https://jsonplaceholder.typicode.com/users')
# # print(r.status_code)
# # print(r.json())
# if r.status_code == 200:
#     res = r.json()
#     print(res)

r = requests.get('https://api.ipify.org?format=json')


if r.status_code == 200:
    data = r.json()
    ip = data.get('ip')
    print('Your ip address is :', ip)