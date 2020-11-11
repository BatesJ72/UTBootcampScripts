import requests

BASE_URL = "https://newjersey.craigslist.org/search/sss"

BASE_PARAMS = {
    "sort": "rel",
    "query": "guitar"
}

r= requests.get(BASE_URL, params=BASE_PARAMS)

print(r.status_code)
print(r.text)