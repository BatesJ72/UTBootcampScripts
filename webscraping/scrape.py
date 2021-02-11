import requests

BASE_URL = "https://austin.craigslist.org/search/sss"

BASE_PARAMS = {
    "query": "tv+stand+mid+century",
}

r = requests.get(BASE_URL, params=BASE_PARAMS)

# print(r.status_code)
# print(r.text)

with open("html_request.html", "w+") as f:
    f.write(r.text)