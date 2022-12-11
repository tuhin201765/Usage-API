import requests
r = requests.get('https://www.arbeitnow.com/api/job-board-api')
if r.status_code == 200:
    data = r.json()
    ip = data.get('ip')
    region = data.get('data')[1].get('slug')
    title = data.get('data')[1].get('title')
    url = data.get('data')[1].get('url')
    print(region)
    print(title)
    print(url)



