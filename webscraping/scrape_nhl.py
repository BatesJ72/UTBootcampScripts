import requests

BASE_URL = "https://www.nhl.com/news/this-date-in-nhl-history-november-5/c-283308796"

BASE_PARAMS = {
    
}

r = requests.get(BASE_URL, params=BASE_PARAMS)

# print(r.status_code)
# print(r.text)

with open("html_request.html", "w+") as f:
    f.write(r.text)