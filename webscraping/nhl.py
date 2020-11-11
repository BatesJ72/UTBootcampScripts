import requests

r = requests.get("https://www.nhl.com/news/this-date-in-nhl-history-november-10/c-283498080?tid=279684992")

# print(r.status_code)
# print(r.text)

with open("html_request.txt", "w+") as f:
    f.write(r.text)